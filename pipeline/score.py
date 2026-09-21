"""Score approved drugs against diseases over drug -> gene -> disease paths.

Method is a simplified degree-weighted path count, the idea behind Project
Rephetio (Himmelstein et al., eLife 2017). A path through a hub gene that
everything connects to is worth less than a path through a specific one, so
each path is damped by the connectivity of the nodes it crosses.

The `clinical` datatype is deliberately excluded from the association score.
Open Targets derives it from known drug evidence, so including it would leak
the answer into the prediction and make validation meaningless.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diseases import ALL, NAMES, RARITY

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
RAW = os.path.join(ROOT, "data", "raw")
RESULTS = os.path.join(ROOT, "web", "data", "results")

W = 0.4                    # degree damping exponent, Rephetio's published value
LEAKY_DATATYPES = {"clinical", "known_drug"}
GENES_PER_DISEASE = 50
MAX_CANDIDATES = 40
MAX_PATHS_SHOWN = 3


def load(kind):
    with open(os.path.join(RAW, kind + ".json"), encoding="utf-8") as fh:
        return json.load(fh)


def assoc_score(datatype_scores):
    """Combine non-leaky evidence types. 1 - prod(1 - s) rewards independent
    lines of evidence without letting any single one saturate the result."""
    product = 1.0
    kept = []
    for entry in datatype_scores or []:
        if entry["id"] in LEAKY_DATATYPES:
            continue
        product *= (1.0 - float(entry["score"]))
        kept.append({"id": entry["id"], "score": round(float(entry["score"]), 4)})
    kept.sort(key=lambda e: -e["score"])
    return 1.0 - product, kept


def parent_of(drug):
    return (drug.get("parentMolecule") or drug)


def build_drug_gene_index(genes):
    """drug id -> set(gene id) and gene id -> set(drug id), approved drugs only."""
    drugs_of_gene, genes_of_drug = {}, {}
    for ens, node in genes.items():
        for row in node["drugAndClinicalCandidates"]["rows"]:
            drug = row.get("drug") or {}
            if drug.get("maximumClinicalStage") != "APPROVAL":
                continue
            pid = parent_of(drug).get("id")
            if not pid:
                continue
            drugs_of_gene.setdefault(ens, set()).add(pid)
            genes_of_drug.setdefault(pid, set()).add(ens)
    return drugs_of_gene, genes_of_drug


def known_parent_ids(disease_node):
    ids = set()
    for row in disease_node["drugAndClinicalCandidates"]["rows"]:
        drug = row.get("drug") or {}
        pid = parent_of(drug).get("id")
        if pid:
            ids.add(pid)
    return ids


def compute_totals(disease_node, drugs_of_gene, genes_of_drug):
    """The whole scoring step: every approved drug reachable from this
    disease's top genes, with its total score and its contributing paths.

    Returned untruncated so validation can rank the full candidate pool.
    """
    rows = disease_node["associatedTargets"]["rows"]
    scored_genes = []
    for row in rows:
        a, evidence = assoc_score(row.get("datatypeScores"))
        if a <= 0:
            continue
        scored_genes.append({
            "id": row["target"]["id"],
            "symbol": row["target"]["approvedSymbol"],
            "name": row["target"].get("approvedName"),
            "assoc": a,
            "evidence": evidence,
            "otScore": row["score"],
        })
    scored_genes.sort(key=lambda g: -g["assoc"])
    scored_genes = scored_genes[:GENES_PER_DISEASE]

    contributions = {}
    for gene in scored_genes:
        gene_drugs = drugs_of_gene.get(gene["id"], ())
        if not gene_drugs:
            continue
        gene_degree = len(gene_drugs) ** W
        for pid in gene_drugs:
            drug_degree = len(genes_of_drug.get(pid, ())) ** W
            value = gene["assoc"] / (gene_degree * drug_degree)
            contributions.setdefault(pid, []).append((value, gene))

    totals = {pid: sum(v for v, _ in paths) for pid, paths in contributions.items()}
    return totals, contributions, scored_genes


def score_disease(efo, disease_node, genes, drugs, drugs_of_gene, genes_of_drug):
    totals, contributions, scored_genes = compute_totals(
        disease_node, drugs_of_gene, genes_of_drug)
    if not totals:
        return None
    hi = max(totals.values())
    lo = min(totals.values())
    span = (hi - lo) or 1.0

    known = known_parent_ids(disease_node)
    ranked = sorted(totals.items(), key=lambda kv: -kv[1])
    rank_of = {pid: i + 1 for i, (pid, _) in enumerate(ranked)}

    def build(pid, total):
        meta = drugs.get(pid) or {}
        paths = sorted(contributions[pid], key=lambda p: -p[0])[:MAX_PATHS_SHOWN]
        return {
            "id": pid,
            "name": (meta.get("name") or pid).title(),
            "drugType": meta.get("drugType"),
            "approvedFor": meta.get("approvedFor", []),
            "indicationCount": meta.get("indicationCount", 0),
            "mechanisms": meta.get("mechanisms", []),
            "rank": rank_of[pid],
            "score": round((total - lo) / span, 4),
            "rawScore": round(total, 6),
            "geneCount": len(genes_of_drug.get(pid, ())),
            "paths": [{
                "gene": gene["symbol"],
                "geneId": gene["id"],
                "geneName": gene["name"],
                "assoc": round(gene["assoc"], 4),
                "contribution": round(value, 6),
                "drugsOnGene": len(drugs_of_gene.get(gene["id"], ())),
                "evidence": gene["evidence"],
            } for value, gene in paths],
        }

    candidates = [build(pid, total) for pid, total in ranked if pid not in known][:MAX_CANDIDATES]
    known_ranked = [build(pid, total) for pid, total in ranked if pid in known][:10]

    return {
        "id": efo,
        "name": NAMES.get(efo, disease_node["name"]),
        "rarity": RARITY.get(efo, "rare"),
        "description": (disease_node.get("description") or "")[:400],
        "associatedGeneCount": disease_node["associatedTargets"]["count"],
        "genesScored": len(scored_genes),
        "genesWithDrugs": sum(1 for g in scored_genes if drugs_of_gene.get(g["id"])),
        "knownDrugCount": disease_node["drugAndClinicalCandidates"]["count"],
        "candidatesConsidered": len(totals),
        "candidates": candidates,
        "knownRanked": known_ranked,
    }


def main():
    diseases = load("diseases")
    genes = load("genes")
    drugs = load("drugs")
    drugs_of_gene, genes_of_drug = build_drug_gene_index(genes)
    print("index: %d genes with approved drugs, %d distinct approved drugs"
          % (len(drugs_of_gene), len(genes_of_drug)))

    os.makedirs(RESULTS, exist_ok=True)
    index = []
    for efo, _name, _rarity in ALL:
        node = diseases.get(efo)
        if not node:
            continue
        result = score_disease(efo, node, genes, drugs, drugs_of_gene, genes_of_drug)
        if not result:
            print("  %-34s no scoreable paths" % NAMES[efo][:34])
            continue
        with open(os.path.join(RESULTS, efo + ".json"), "w", encoding="utf-8") as fh:
            json.dump(result, fh, indent=1)
        index.append({
            "id": efo,
            "name": result["name"],
            "rarity": result["rarity"],
            "candidates": len(result["candidates"]),
            "knownDrugCount": result["knownDrugCount"],
        })
        print("  %-34s %3d candidates  %3d known  %2d/%2d genes druggable"
              % (result["name"][:34], len(result["candidates"]), result["knownDrugCount"],
                 result["genesWithDrugs"], result["genesScored"]))

    with open(os.path.join(ROOT, "web", "data", "index.json"), "w", encoding="utf-8") as fh:
        json.dump({"diseases": index, "dampingExponent": W,
                   "excludedDatatypes": sorted(LEAKY_DATATYPES)}, fh, indent=1)
    print("wrote %d disease result files" % len(index))


if __name__ == "__main__":
    main()
