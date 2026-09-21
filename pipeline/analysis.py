"""Five checks that go beyond "is it better than random".

A single headline number invites fair questions, and this answers them from
the cached data, without touching the network.

  1. Sensitivity   Is 0.4 a lucky value for the damping exponent?
                   We sweep it and report the whole curve. We do NOT then
                   pick the best one -- 0.4 stays, because it is the value
                   the Rephetio paper published. Reporting a sweep is
                   honest; choosing from it would be fitting.

  2. Confidence    Is the result stable, or an accident of which diseases
                   we happened to include? Bootstrap over diseases -- not
                   over drug-disease pairs, because pairs inside one
                   disease are correlated and resampling them would give a
                   falsely narrow interval.

  3. Ablation      Which evidence types actually carry the signal? Drop
                   each in turn and watch the median move.

  4. Negative      Score every disease against a DIFFERENT disease's known
     control       drugs. If the method is real, performance must collapse
                   toward random. If it does not, something is leaking.

  5. Conservative  Text mining turns out to carry the most signal, which is
     floor         uncomfortable, because papers co-mention a gene and a
                   disease partly BECAUSE a drug already links them. So we
                   also report what survives with all literature-derived
                   evidence removed. That number is the one to quote if
                   anyone presses on it.
"""
import json
import os
import random
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import score as scoring
from diseases import ALL
from score import build_drug_gene_index, compute_totals, known_parent_ids, load

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BOOTSTRAP_ROUNDS = 2000
SEED = 20260921


def percentiles_for(disease_node, drugs_of_gene, genes_of_drug, interactions,
                    damping=None, known_override=None):
    totals, _c, _g = compute_totals(disease_node, drugs_of_gene, genes_of_drug,
                                    interactions, damping=damping)
    if not totals:
        return []
    known = known_override if known_override is not None else known_parent_ids(disease_node)
    ranked = sorted(totals.items(), key=lambda kv: -kv[1])
    pool = len(ranked)
    return [(i + 1) / pool for i, (pid, _v) in enumerate(ranked) if pid in known]


def sweep(diseases, drugs_of_gene, genes_of_drug, interactions):
    """Per-disease median percentiles, one list per disease."""
    out = []
    for efo, _name, _rarity in ALL:
        node = diseases.get(efo)
        if not node:
            continue
        out.append((efo, node))
    return out


def median_of(per_disease_pcts):
    flat = [p for pcts in per_disease_pcts for p in pcts]
    return statistics.median(flat) if flat else None


def main():
    diseases = load("diseases")
    genes = load("genes")
    interactions = load("interactions", required=False)
    drugs_of_gene, genes_of_drug = build_drug_gene_index(genes)
    nodes = sweep(diseases, drugs_of_gene, genes_of_drug, interactions)
    print("%d diseases loaded" % len(nodes))
    report = {}

    # ---- 1. damping sensitivity -------------------------------------------
    print()
    print("1. sensitivity to the damping exponent")
    print("   %-8s %-10s" % ("w", "median"))
    curve = []
    for w in (0.0, 0.2, 0.4, 0.6, 0.8, 1.0):
        pcts = [percentiles_for(n, drugs_of_gene, genes_of_drug, interactions, damping=w)
                for _efo, n in nodes]
        med = median_of(pcts)
        curve.append({"w": w, "median": round(med, 4)})
        marker = "   <- published value, the one we use" if abs(w - 0.4) < 1e-9 else ""
        print("   %-8.1f %-10.3f%s" % (w, med, marker))
    report["dampingSweep"] = curve

    # ---- 2. bootstrap over diseases ---------------------------------------
    base = [percentiles_for(n, drugs_of_gene, genes_of_drug, interactions)
            for _efo, n in nodes]
    usable = [p for p in base if p]
    point = median_of(usable)
    rng = random.Random(SEED)
    medians = []
    for _ in range(BOOTSTRAP_ROUNDS):
        sample = [usable[rng.randrange(len(usable))] for _ in range(len(usable))]
        m = median_of(sample)
        if m is not None:
            medians.append(m)
    medians.sort()
    lo = medians[int(0.025 * len(medians))]
    hi = medians[int(0.975 * len(medians))]
    print()
    print("2. bootstrap over diseases (%d rounds, resampling diseases not pairs)"
          % BOOTSTRAP_ROUNDS)
    print("   median percentile %.1f%%, 95%% CI [%.1f%%, %.1f%%]"
          % (100 * point, 100 * lo, 100 * hi))
    print("   random would be 50.0%% -- the interval %s"
          % ("excludes it" if hi < 0.5 else "DOES NOT exclude it"))
    report["bootstrap"] = {"median": round(point, 4), "ci95": [round(lo, 4), round(hi, 4)],
                           "rounds": BOOTSTRAP_ROUNDS, "excludesRandom": hi < 0.5}

    # ---- 3. evidence ablation ---------------------------------------------
    present = set()
    for _efo, node in nodes:
        for row in node["associatedTargets"]["rows"]:
            for entry in row.get("datatypeScores") or []:
                present.add(entry["id"])
    present -= scoring.LEAKY_DATATYPES
    print()
    print("3. evidence ablation -- median when each type is removed")
    print("   %-24s %-10s %s" % ("removed", "median", "change"))
    original = set(scoring.LEAKY_DATATYPES)
    ablation = []
    for datatype in sorted(present):
        scoring.LEAKY_DATATYPES = original | {datatype}
        pcts = [percentiles_for(n, drugs_of_gene, genes_of_drug, interactions)
                for _efo, n in nodes]
        med = median_of(pcts)
        delta = med - point
        ablation.append({"datatype": datatype, "median": round(med, 4),
                         "delta": round(delta, 4)})
        print("   %-24s %-10.3f %+.3f%s" % (datatype, med, delta,
              "  <- removing this hurts most" if delta > 0.02 else ""))
    scoring.LEAKY_DATATYPES = original
    report["ablation"] = ablation

    # ---- 4. negative control ----------------------------------------------
    print()
    print("4. negative control -- each disease scored against another disease's known drugs")
    shifted = []
    for i, (_efo, node) in enumerate(nodes):
        other = nodes[(i + 1) % len(nodes)][1]
        shifted.append(percentiles_for(node, drugs_of_gene, genes_of_drug, interactions,
                                       known_override=known_parent_ids(other)))
    shuffled_med = median_of(shifted)
    print("   real pairings:     %.1f%%" % (100 * point))
    print("   mismatched pairs:  %.1f%%" % (100 * shuffled_med))
    print("   random:            50.0%")
    verdict = ("collapses to near random, as it must"
               if shuffled_med > 0.42 else "DOES NOT collapse -- investigate for leakage")
    print("   %s" % verdict)
    report["negativeControl"] = {"real": round(point, 4),
                                 "mismatched": round(shuffled_med, 4),
                                 "collapses": shuffled_med > 0.42}

    # ---- 5. conservative floor -------------------------------------------
    # Text mining carries the most signal, and that is uncomfortable: papers
    # co-mention a gene and a disease partly BECAUSE a drug already links
    # them, so literature evidence may quietly re-import the known-drug
    # information we worked to exclude. The honest response is not to argue
    # about it but to report what survives without it.
    scoring.LEAKY_DATATYPES = original | {"literature", "genetic_literature"}
    pcts = [percentiles_for(n, drugs_of_gene, genes_of_drug, interactions)
            for _efo, n in nodes]
    floor = median_of(pcts)
    scoring.LEAKY_DATATYPES = original
    print()
    print("5. conservative floor -- all literature-derived evidence also removed")
    print("   median percentile %.1f%% (headline %.1f%%, random 50.0%%)"
          % (100 * floor, 100 * point))
    print("   %s" % ("still clearly better than chance"
                     if floor < 0.45 else "NOT clearly better than chance"))
    report["conservativeFloor"] = {"median": round(floor, 4),
                                   "betterThanChance": floor < 0.45}

    with open(os.path.join(ROOT, "web", "data", "analysis.json"), "w",
              encoding="utf-8") as fh:
        json.dump(report, fh, indent=1)
    print()
    print("written to web/data/analysis.json")


if __name__ == "__main__":
    main()
