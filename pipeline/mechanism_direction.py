"""Does the drug's mechanism actually point the right way, genetically?

Everything so far asks "is this drug connected to this disease". This asks a
sharper question: for genes where we know the *direction* of genetic effect
(does losing function of this gene cause the disease, or protect against it?),
does the drug's mechanism push in the direction that would actually help?

This is a simplified echo of a real, well-known result: Nelson et al.,
"The support of human genetic evidence for approved drug indications",
Nature Genetics 2015 -- approved drugs are markedly more likely than chance
to have a mechanism that is genetically concordant with the disease.

The leakage trap here is worse than the one in score.py. Open Targets'
`directionOnTrait` / `directionOnTarget` fields are populated for many
gene-disease pairs by the `clinical_precedence` datasource -- which means
"a drug with this mechanism is already approved for this disease", restated
as if it were evidence. Using that would not just leak the answer, it would
make the entire check circular by construction. clinical_precedence is
excluded from every query in this script, unconditionally. Only rows from
eva (ClinVar), gene2phenotype, orphanet, genomics_england, gene_burden and
uniprot_variants are used -- independent human genetics, not drug history.

Scope: the curated 100 diseases only, and only the (disease, gene) pairs
that actually appear in their scored candidate paths. That is what makes
this a targeted few hundred queries instead of a second full-scale fetch.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import gql, alias

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
RESULTS = os.path.join(ROOT, "web", "data", "results")
OUT = os.path.join(ROOT, "web", "data", "concordance.json")

SAFE_DATASOURCES = ["eva", "gene2phenotype", "orphanet", "genomics_england",
                    "gene_burden", "uniprot_variants"]
EVIDENCE_BATCH = 15
MECHANISM_BATCH = 15
EVIDENCE_PAGE = 40

# actionType strings observed from ChEMBL, mapped to whether the drug pushes
# the target's function up or down. Anything not listed is left unmapped
# rather than guessed at.
INCREASES_FUNCTION = {
    "AGONIST", "PARTIAL AGONIST", "ACTIVATOR", "POSITIVE MODULATOR",
    "POSITIVE ALLOSTERIC MODULATOR", "STABILISER", "OPENER", "INDUCER",
    "SUBSTRATE",
}
DECREASES_FUNCTION = {
    "ANTAGONIST", "INHIBITOR", "BLOCKER", "NEGATIVE MODULATOR",
    "NEGATIVE ALLOSTERIC MODULATOR", "DEGRADER", "INVERSE AGONIST",
    "DISRUPTING AGENT", "SEQUESTERING AGENT", "RNAI INHIBITOR",
    "ANTISENSE INHIBITOR", "PROTEOLYTIC ENZYME",
}


def collect_scope():
    """Every (disease, gene) pair in a curated disease's results, and every
    drug id that appears there, so we only fetch what we can actually use."""
    pairs, drugs = set(), set()
    for fn in os.listdir(RESULTS):
        efo = fn[:-5]
        with open(os.path.join(RESULTS, fn), encoding="utf-8") as fh:
            d = json.load(fh)
        if d.get("rarity") not in ("rare", "common"):
            continue
        for entry in d["candidates"] + d["knownRanked"]:
            drugs.add(entry["id"])
            for p in entry["paths"]:
                pairs.add((efo, p["geneId"]))
    return sorted(pairs), sorted(drugs)


def fetch_direction(pairs):
    """(efo, gene) -> aggregated {"onTarget": "LoF"/"GoF", "onTrait": "risk"/"protect"}
    or None if evidence is missing, absent, or internally conflicting."""
    out = {}
    for start in range(0, len(pairs), EVIDENCE_BATCH):
        chunk = pairs[start:start + EVIDENCE_BATCH]
        parts = []
        for i, (efo, gene) in enumerate(chunk):
            ds = ", ".join('"%s"' % d for d in SAFE_DATASOURCES)
            parts.append('''
  %s: target(ensemblId: "%s") {
    evidences(efoIds: ["%s"], datasourceIds: [%s], size: %d) {
      rows { directionOnTrait directionOnTarget }
    }
  }''' % (alias("e", i), gene, efo, ds, EVIDENCE_PAGE))
        data = gql("query {" + "\n".join(parts) + "\n}")
        for i, (efo, gene) in enumerate(chunk):
            node = data.get(alias("e", i))
            rows = (node or {}).get("evidences", {}).get("rows", []) if node else []
            targets = {r["directionOnTarget"] for r in rows if r.get("directionOnTarget")}
            traits = {r["directionOnTrait"] for r in rows if r.get("directionOnTrait")}
            if len(targets) == 1 and len(traits) == 1:
                out[(efo, gene)] = {"onTarget": targets.pop(), "onTrait": traits.pop()}
        if start % (EVIDENCE_BATCH * 10) == 0:
            print("  direction: %d/%d pairs" % (min(start + EVIDENCE_BATCH, len(pairs)), len(pairs)))
    return out


def fetch_actions(drug_ids):
    """drug id -> {gene id: actionType string}, straight from ChEMBL mechanisms."""
    out = {}
    for start in range(0, len(drug_ids), MECHANISM_BATCH):
        chunk = drug_ids[start:start + MECHANISM_BATCH]
        parts = []
        for i, chembl in enumerate(chunk):
            parts.append('''
  %s: drug(chemblId: "%s") {
    mechanismsOfAction { rows { actionType targets { id } } }
  }''' % (alias("m", i), chembl))
        data = gql("query {" + "\n".join(parts) + "\n}")
        for i, chembl in enumerate(chunk):
            node = data.get(alias("m", i))
            rows = (node or {}).get("mechanismsOfAction", {}).get("rows", []) if node else []
            mapping = {}
            for r in rows:
                at = (r.get("actionType") or "").upper()
                for t in (r.get("targets") or []):
                    if t.get("id"):
                        mapping[t["id"]] = at
            out[chembl] = mapping
        if start % (MECHANISM_BATCH * 10) == 0:
            print("  mechanisms: %d/%d drugs" % (min(start + MECHANISM_BATCH, len(drug_ids)), len(drug_ids)))
    return out


def drug_direction(action_type):
    if action_type in INCREASES_FUNCTION:
        return "increases"
    if action_type in DECREASES_FUNCTION:
        return "decreases"
    return None


def concordant(genetics, drug_push):
    """Does the drug push the gene the way that would help, given the
    genetics of this gene-disease pair? True/False/None (not assessable)."""
    if not genetics or not drug_push:
        return None
    helpful_push = {
        ("risk", "LoF"): "increases",     # losing function causes disease -> restore it
        ("protect", "LoF"): "decreases",  # losing function protects -> mimic that loss
        ("risk", "GoF"): "decreases",     # gaining function causes disease -> reduce it
        ("protect", "GoF"): "increases",  # gaining function protects -> mimic that gain
    }.get((genetics["onTrait"], genetics["onTarget"]))
    if helpful_push is None:
        return None
    return drug_push == helpful_push


def main():
    pairs, drug_ids = collect_scope()
    print("scope: %d disease-gene pairs, %d drugs (curated diseases only)"
          % (len(pairs), len(drug_ids)))

    print("fetching independent genetic direction evidence...")
    directions = fetch_direction(pairs)
    print("  %d of %d pairs have unambiguous, non-drug-derived direction evidence"
          % (len(directions), len(pairs)))

    print("fetching drug mechanism-of-action per target...")
    actions = fetch_actions(drug_ids)

    known_results, novel_results = [], []
    for fn in os.listdir(RESULTS):
        efo = fn[:-5]
        with open(os.path.join(RESULTS, fn), encoding="utf-8") as fh:
            d = json.load(fh)
        if d.get("rarity") not in ("rare", "common"):
            continue
        for bucket, out_list in (("candidates", novel_results), ("knownRanked", known_results)):
            for entry in d[bucket]:
                mech = actions.get(entry["id"], {})
                for p in entry["paths"]:
                    genetics = directions.get((efo, p["geneId"]))
                    at = mech.get(p["geneId"])
                    push = drug_direction(at)
                    c = concordant(genetics, push)
                    if c is not None:
                        out_list.append({
                            "disease": efo, "drug": entry["name"], "gene": p["gene"],
                            "actionType": at, "genetics": genetics, "concordant": c,
                        })

    def rate(results):
        if not results:
            return None
        return sum(1 for r in results if r["concordant"]) / len(results)

    known_rate = rate(known_results)
    novel_rate = rate(novel_results)

    def two_proportion_z(x1, n1, x2, n2):
        if n1 == 0 or n2 == 0:
            return None, None
        p1, p2 = x1 / n1, x2 / n2
        p_pool = (x1 + x2) / (n1 + n2)
        se = math.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n2))
        if se == 0:
            return None, None
        z = (p1 - p2) / se
        p_val = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))
        return z, p_val

    known_hits = sum(1 for r in known_results if r["concordant"])
    novel_hits = sum(1 for r in novel_results if r["concordant"])
    z_stat, p_val = two_proportion_z(known_hits, len(known_results),
                                     novel_hits, len(novel_results))
    print()
    print("assessable triples: %d known-drug, %d novel-candidate" % (len(known_results), len(novel_results)))
    if known_rate is not None:
        print("genetic concordance among ALREADY-APPROVED drugs: %.1f%% (n=%d)"
              % (100 * known_rate, len(known_results)))
    if novel_rate is not None:
        print("genetic concordance among OUR NOVEL CANDIDATES:    %.1f%% (n=%d)"
              % (100 * novel_rate, len(novel_results)))
    if p_val is not None:
        print("two-proportion z-test: z=%.2f, two-sided p=%.4f%s"
              % (z_stat, p_val, "  (significant at p<0.05)" if p_val < 0.05 else ""))
    if known_rate is not None and novel_rate is not None:
        print()
        if known_rate > novel_rate + 0.05:
            print("Approved drugs are more often genetically concordant than our novel")
            print("candidates. That is the expected Nelson-et-al direction, and it means")
            print("genetic concordance is a real, independent signal we are not currently")
            print("using -- filtering candidates by it would be a legitimate improvement.")
        else:
            print("No clear gap between approved drugs and our candidates on this measure.")
            print("Either the sample is too small, or concordance is not adding signal")
            print("beyond what the existing ranking already captures.")

    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump({
            "scope": "curated rare + common diseases only",
            "safeDatasources": SAFE_DATASOURCES,
            "pairsWithDirection": len(directions),
            "pairsTotal": len(pairs),
            "knownConcordanceRate": known_rate,
            "novelConcordanceRate": novel_rate,
            "knownSampleSize": len(known_results),
            "novelSampleSize": len(novel_results),
            "zStatistic": z_stat, "pValue": p_val,
            "knownExamples": known_results[:40],
            "novelExamples": [r for r in novel_results if r["concordant"]][:40],
        }, fh, indent=1)
    print()
    print("written to web/data/concordance.json")


if __name__ == "__main__":
    main()
