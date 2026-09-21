"""Does the engine actually rank real treatments highly, and does the method
earn its complexity?

For every drug already approved for a disease, we compute where our score
places it among all candidates for that disease. A useful engine puts them
near the top; a useless one scatters them uniformly, giving a median rank
percentile around 50%.

Every known drug in the candidate pool is evaluated, not just the ones that
scored well -- ranking only the winners would inflate the result.

Three rankings are compared over the identical candidate pool:

  ours         degree-weighted paths, damping exponent 0.4
  no damping   the same paths counted equally, exponent 0
  popularity   drugs ranked by how many genes they hit, ignoring the disease

The third is the one that matters. If a disease-agnostic popularity ranking
scored as well as ours, the biology in this project would be decoration.

There is no train/test split, and that is deliberate. The damping exponent is
fixed at the value published in the Rephetio paper and nothing is fitted, so
there are no learned parameters that could overfit. What protects this
measurement from leakage is the exclusion of the `clinical` datatype in
score.py, not hiding rows from a training set.
"""
import json
import os
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diseases import ALL
from score import (W, LEAKY_DATATYPES, build_drug_gene_index, compute_totals,
                   known_parent_ids, load)

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def positions(ranked_ids, known):
    """Rank percentile of each known drug within the ranked candidate pool."""
    pool = len(ranked_ids)
    return [((i + 1) / pool, i + 1) for i, pid in enumerate(ranked_ids) if pid in known]


def evaluate(disease_node, drugs_of_gene, genes_of_drug, interactions):
    totals, _c, _g = compute_totals(disease_node, drugs_of_gene, genes_of_drug,
                                    interactions)
    if not totals:
        return None
    known = known_parent_ids(disease_node)
    pool_ids = set(totals)
    if not known & pool_ids:
        return None

    ours = [pid for pid, _v in sorted(totals.items(), key=lambda kv: -kv[1])]

    flat, _c2, _g2 = compute_totals(disease_node, drugs_of_gene, genes_of_drug,
                                    interactions, damping=0.0)
    nodamp = [pid for pid, _v in sorted(flat.items(), key=lambda kv: -kv[1])]

    # disease-agnostic: how many genes does this drug hit, full stop
    popularity = sorted(pool_ids, key=lambda pid: -len(genes_of_drug.get(pid, ())))

    return {
        "pool": len(ours),
        "oursRanked": ours,
        "ours": positions(ours, known),
        "nodamp": positions(nodamp, known),
        "popularity": positions(popularity, known),
    }


def summarise(values):
    if not values:
        return {"pairs": 0}
    pcts = [p for p, _r in values]
    return {
        "pairs": len(pcts),
        "topFivePercent": round(sum(1 for p in pcts if p <= 0.05) / len(pcts), 4),
        "topTenPercent": round(sum(1 for p in pcts if p <= 0.10) / len(pcts), 4),
        "topQuarter": round(sum(1 for p in pcts if p <= 0.25) / len(pcts), 4),
        "medianPercentile": round(statistics.median(pcts), 4),
    }


def main():
    diseases = load("diseases")
    genes = load("genes")
    interactions = load("interactions", required=False)
    drugs = load("drugs")
    drugs_of_gene, genes_of_drug = build_drug_gene_index(genes)

    per_disease = []
    buckets = {"ours": [], "nodamp": [], "popularity": []}
    rare_ours = []
    top_hits = top_five = 0

    for efo, name, rarity in ALL:
        node = diseases.get(efo)
        if not node:
            continue
        out = evaluate(node, drugs_of_gene, genes_of_drug, interactions)
        if not out:
            continue
        for key in buckets:
            buckets[key].extend(out[key])
        pcts = [p for p, _r in out["ours"]]
        if rarity == "rare":
            rare_ours.extend(out["ours"])
        best_rank = min(r for _p, r in out["ours"])
        if best_rank == 1:
            top_hits += 1
        if best_rank <= 5:
            top_five += 1
        best_drug = drugs.get(out["oursRanked"][best_rank - 1], {})
        per_disease.append({
            "id": efo,
            "name": name,
            "rarity": rarity,
            "candidatePool": out["pool"],
            "knownEvaluated": len(pcts),
            "bestRank": best_rank,
            "bestDrug": (best_drug.get("name") or "").title(),
            "medianPercentile": round(statistics.median(pcts), 4),
        })
        print("  %-38s pool %4d  known %3d  best #%-4d (%s)  median %5.1f%%"
              % (name[:38], out["pool"], len(pcts), best_rank,
                 (best_drug.get("name") or "?").title()[:20], 100 * statistics.median(pcts)))

    summary = {
        "dampingExponent": W,
        "excludedDatatypes": sorted(LEAKY_DATATYPES),
        "interactionHop": bool(interactions),
        "diseasesEvaluated": len(per_disease),
        "knownPairsEvaluated": len(buckets["ours"]),
        "diseasesWhereTopCandidateIsKnown": top_hits,
        "diseasesWhereKnownInTopFive": top_five,
        "rareOnly": summarise(rare_ours),
        "methods": {k: summarise(v) for k, v in buckets.items()},
    }
    ours = summary["methods"]["ours"]
    summary.update({
        "topFivePercent": ours["topFivePercent"],
        "topTenPercent": ours["topTenPercent"],
        "topQuarter": ours["topQuarter"],
        "medianPercentile": ours["medianPercentile"],
        "enrichmentOverChanceTopTen": round(ours["topTenPercent"] / 0.10, 2),
        "randomBaselineMedian": 0.5,
    })

    with open(os.path.join(ROOT, "web", "data", "validation.json"), "w",
              encoding="utf-8") as fh:
        json.dump({"summary": summary, "perDisease": per_disease}, fh, indent=1)

    print()
    print("%d known drug-disease pairs across %d diseases"
          % (summary["knownPairsEvaluated"], summary["diseasesEvaluated"]))
    print("top-ranked candidate is already a known treatment: %d of %d diseases"
          % (top_hits, summary["diseasesEvaluated"]))
    print("a known treatment appears in our top 5: %d of %d diseases"
          % (top_five, summary["diseasesEvaluated"]))
    print()
    print("%-12s %9s %9s %9s %9s" % ("method", "top 5%", "top 10%", "top 25%", "median"))
    for key, label in (("ours", "ours"), ("nodamp", "no damping"),
                       ("popularity", "popularity")):
        m = summary["methods"][key]
        print("%-12s %8.1f%% %8.1f%% %8.1f%% %8.1f%%"
              % (label, 100 * m["topFivePercent"], 100 * m["topTenPercent"],
                 100 * m["topQuarter"], 100 * m["medianPercentile"]))
    print("%-12s %8.1f%% %8.1f%% %8.1f%% %8.1f%%" % ("random", 5.0, 10.0, 25.0, 50.0))


if __name__ == "__main__":
    main()
