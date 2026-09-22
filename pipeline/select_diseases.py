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

Every disease meeting the rule is included. There is no cap and no ranking
step, so there is no cut that could act as a quality filter in disguise.
Ordering is by ontology id purely for reproducibility.

Run this only when you want to regenerate the list:

    python pipeline/select_diseases.py

It writes pipeline/generated_diseases.py itself, as UTF-8. Redirecting stdout
instead would re-encode through the console codepage, which on Windows turns
names like Chediak-Higashi into invalid bytes.
"""
import json
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
MAX_DISEASES = None   # None means take everything meeting the rule
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
    """Screen candidates, caching as we go. Screening the whole ontology is a
    ten minute round trip, and nothing about it changes between runs, so it is
    written to disk and reused."""
    cache_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              "..", "data", "raw", "screen.json")
    out = {}
    if os.path.exists(cache_path):
        with open(cache_path, encoding="utf-8") as fh:
            out = json.load(fh)
        print("  %d candidates already screened" % len(out), file=sys.stderr)
    ids = sorted(set(ids) - set(out))
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
            with open(cache_path, "w", encoding="utf-8") as fh:
                json.dump(out, fh)
    with open(cache_path, "w", encoding="utf-8") as fh:
        json.dump(out, fh)
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
    passed = len(kept)
    if MAX_DISEASES:
        kept = kept[:MAX_DISEASES]

    print("screened %d, %d passed the rule, keeping %d"
          % (len(stats), passed, len(kept)), file=sys.stderr)

    lines = [
        '"""Diseases selected programmatically by pipeline/select_diseases.py.',
        "",
        "Rule: at least %d associated genes and at least %d known drug."
        % (MIN_TARGETS, MIN_KNOWN_DRUGS),
        "Every disease meeting it is included. Not hand-picked, not capped.",
        '"""',
        "",
        "GENERATED = [",
    ]
    for efo, stat in kept:
        name = stat["name"].replace('"', "'")
        lines.append('    ("%s", "%s"),  # %d genes, %d known drugs'
                     % (efo, name, stat["targets"], stat["drugs"]))
    lines.append("]")

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "generated_diseases.py")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")
    print("wrote %s" % out_path, file=sys.stderr)


if __name__ == "__main__":
    main()
