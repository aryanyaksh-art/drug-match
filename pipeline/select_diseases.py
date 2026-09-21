"""Choose the disease set by a stated rule instead of by hand.

The first version of this project used 100 diseases we picked ourselves. That
invites a fair objection: did we choose the ones we knew would work? This
script removes the choice. It walks the disease ontology under a fixed set of
therapeutic areas, applies a filter written down in advance, and takes
everything that qualifies in a deterministic order.

The rule, fixed before looking at any result:

    keep a disease if it has at least MIN_TARGETS associated genes
    and at least MIN_KNOWN_DRUGS drugs already known to treat it

The gene threshold is so there is something to reason over. The drug threshold
is so the disease can appear in validation at all -- a disease with no known
treatment cannot tell us whether our ranking is any good.

Ordering is by ontology id, which has nothing to do with how well a disease
scores, so the cut at MAX_DISEASES is not a quality filter in disguise.

Run this only when you want to regenerate the list:

    python pipeline/select_diseases.py > pipeline/generated_diseases.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import gql, alias
from diseases import NAMES as CURATED

THERAPEUTIC_AREAS = [
    ("OTAR_0000018", "genetic, familial or congenital disease"),
    ("MONDO_0005071", "nervous system disorder"),
    ("OTAR_0000006", "musculoskeletal or connective tissue disease"),
    ("EFO_0005741", "infectious disease"),
    ("MONDO_0004992", "cancer or benign tumor"),
    ("EFO_0000319", "cardiovascular disease"),
    ("EFO_0009605", "pancreas disease"),
    ("MONDO_0002025", "psychiatric disorder"),
    ("EFO_0010282", "gastrointestinal disease"),
    ("MONDO_0005087", "immune system disease"),
]

MIN_TARGETS = 50
MIN_KNOWN_DRUGS = 1
MAX_DISEASES = 320
COUNT_BATCH = 25


def descendants():
    found = set()
    for efo, name in THERAPEUTIC_AREAS:
        data = gql('query { d: disease(efoId: "%s") { descendants } }' % efo)
        node = data.get("d")
        kids = (node or {}).get("descendants") or []
        found.update(kids)
        print("  %-52s %6d descendants" % (name[:52], len(kids)), file=sys.stderr)
    return found


def counts_for(ids):
    out = {}
    ids = sorted(ids)
    for start in range(0, len(ids), COUNT_BATCH):
        chunk = ids[start:start + COUNT_BATCH]
        parts = []
        for i, efo in enumerate(chunk):
            parts.append('''
  %s: disease(efoId: "%s") {
    id name
    associatedTargets(page: {index: 0, size: 1}) { count }
    drugAndClinicalCandidates { count }
  }''' % (alias("c", i), efo))
        data = gql("query {" + "\n".join(parts) + "\n}")
        for i, efo in enumerate(chunk):
            node = data.get(alias("c", i))
            if not node:
                continue
            out[efo] = {
                "name": node["name"],
                "targets": node["associatedTargets"]["count"],
                "drugs": node["drugAndClinicalCandidates"]["count"],
            }
        if start % (COUNT_BATCH * 20) == 0:
            print("  screened %d/%d" % (start, len(ids)), file=sys.stderr)
    return out


def main():
    print("walking therapeutic areas...", file=sys.stderr)
    pool = descendants()
    pool -= set(CURATED)
    print("%d candidate diseases to screen" % len(pool), file=sys.stderr)

    stats = counts_for(pool)
    kept = [(efo, s) for efo, s in stats.items()
            if s["targets"] >= MIN_TARGETS and s["drugs"] >= MIN_KNOWN_DRUGS]
    kept.sort(key=lambda kv: kv[0])          # by id: unrelated to quality
    kept = kept[:MAX_DISEASES]

    print("%d passed the filter, keeping %d" % (len(stats), len(kept)), file=sys.stderr)

    print('"""Diseases selected programmatically by pipeline/select_diseases.py.')
    print()
    print("Rule: at least %d associated genes and at least %d known drug,"
          % (MIN_TARGETS, MIN_KNOWN_DRUGS))
    print("ordered by ontology id and cut at %d. Not hand-picked." % MAX_DISEASES)
    print('"""')
    print()
    print("GENERATED = [")
    for efo, s in kept:
        name = s["name"].replace('"', "'")
        print('    ("%s", "%s"),  # %d genes, %d known drugs'
              % (efo, name, s["targets"], s["drugs"]))
    print("]")


if __name__ == "__main__":
    main()
