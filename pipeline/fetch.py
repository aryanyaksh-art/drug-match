"""Pull everything Off The Shelf needs from the Open Targets Platform API.

Runs once, offline, and caches every response under data/raw/. Nothing in
the shipped web app ever touches the network -- that is deliberate, so a
demo cannot be broken by venue wifi.

Requests are batched with GraphQL aliases because one call per gene would
be ~2000 round trips.
"""
import json
import os
import sys
import time

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diseases import ALL

API = "https://api.platform.opentargets.org/api/v4/graphql"
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
RAW = os.path.join(ROOT, "data", "raw")

TARGETS_PER_DISEASE = 50
DISEASE_BATCH = 4
GENE_BATCH = 20
DRUG_BATCH = 25
INTERACTION_BATCH = 12
GENES_FOR_INTERACTIONS = 25   # top associated genes per disease to expand from
INTERACTION_MIN_SCORE = 0.75  # STRING high-confidence cutoff
PARTNERS_PER_GENE = 8


def gql(query, tries=4):
    for attempt in range(tries):
        try:
            r = requests.post(API, json={"query": query}, timeout=90)
            if r.status_code == 200:
                body = r.json()
                if "errors" in body:
                    raise RuntimeError(body["errors"][0].get("message", "graphql error"))
                return body["data"]
            if r.status_code in (429, 500, 502, 503, 504):
                raise RuntimeError("http %s" % r.status_code)
            r.raise_for_status()
        except Exception as exc:
            if attempt == tries - 1:
                raise
            wait = 2 ** attempt
            print("    retry in %ss (%s)" % (wait, exc))
            time.sleep(wait)


def cache_path(kind):
    return os.path.join(RAW, kind + ".json")


def load_cache(kind):
    p = cache_path(kind)
    if os.path.exists(p):
        with open(p, encoding="utf-8") as fh:
            return json.load(fh)
    return {}


def save_cache(kind, data):
    os.makedirs(RAW, exist_ok=True)
    with open(cache_path(kind), "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=1)


def alias(prefix, i):
    return "%s%d" % (prefix, i)


def fetch_diseases():
    cache = load_cache("diseases")
    todo = [d for d in ALL if d[0] not in cache]
    print("diseases: %d cached, %d to fetch" % (len(cache), len(todo)))
    for start in range(0, len(todo), DISEASE_BATCH):
        chunk = todo[start:start + DISEASE_BATCH]
        parts = []
        for i, (efo, _name, _rarity) in enumerate(chunk):
            parts.append("""
  %s: disease(efoId: "%s") {
    id name description
    associatedTargets(page: {index: 0, size: %d}) {
      count
      rows { score target { id approvedSymbol approvedName } datatypeScores { id score } }
    }
    drugAndClinicalCandidates {
      count
      rows { maxClinicalStage drug { id name parentMolecule { id name } } }
    }
  }""" % (alias("d", i), efo, TARGETS_PER_DISEASE))
        data = gql("query {" + "\n".join(parts) + "\n}")
        for i, (efo, name, _rarity) in enumerate(chunk):
            node = data[alias("d", i)]
            if node is None:
                print("  !! no data for %s (%s)" % (name, efo))
                continue
            cache[efo] = node
            print("  %-34s %5d targets  %4d known drugs" % (
                name[:34], node["associatedTargets"]["count"],
                node["drugAndClinicalCandidates"]["count"]))
        save_cache("diseases", cache)
    return cache


def fetch_genes(disease_cache):
    wanted = set()
    for node in disease_cache.values():
        for row in node["associatedTargets"]["rows"]:
            wanted.add(row["target"]["id"])
    return fetch_genes_for(wanted)


def fetch_genes_for(wanted):
    """Drug lists for an explicit set of genes. Used both for the genes a
    disease is directly associated with and, later, for the interaction
    partners of those genes."""
    cache = load_cache("genes")
    todo = sorted(wanted - set(cache))
    print("genes: %d unique, %d cached, %d to fetch" % (len(wanted), len(cache), len(todo)))
    for start in range(0, len(todo), GENE_BATCH):
        chunk = todo[start:start + GENE_BATCH]
        parts = []
        for i, ens in enumerate(chunk):
            parts.append("""
  %s: target(ensemblId: "%s") {
    id approvedSymbol
    drugAndClinicalCandidates {
      count
      rows { maxClinicalStage drug { id name drugType maximumClinicalStage parentMolecule { id name } } }
    }
  }""" % (alias("g", i), ens))
        data = gql("query {" + "\n".join(parts) + "\n}")
        for i, ens in enumerate(chunk):
            node = data[alias("g", i)]
            cache[ens] = node if node else {"id": ens, "approvedSymbol": ens,
                                            "drugAndClinicalCandidates": {"count": 0, "rows": []}}
        save_cache("genes", cache)
        print("  %d/%d genes" % (min(start + GENE_BATCH, len(todo)), len(todo)))
    return cache


def top_genes_by_assoc(disease_node, limit):
    """Rank this disease's genes the way score.py does -- by evidence with the
    leaky clinical datatype removed -- so we expand from the genes that will
    actually matter, not the ones an unfiltered score happens to favour."""
    from score import assoc_score
    ranked = []
    for row in disease_node["associatedTargets"]["rows"]:
        a, _evidence = assoc_score(row.get("datatypeScores"))
        if a > 0:
            ranked.append((a, row["target"]["id"]))
    ranked.sort(reverse=True)
    return [gid for _a, gid in ranked[:limit]]


def fetch_interactions(disease_cache):
    """Protein-protein interaction partners for each disease's top genes.

    This is what lets the engine reach a disease whose own causal gene has no
    drug against it -- alkaptonuria's HGD and Rett's MECP2 both have zero, but
    both interact strongly with genes that are druggable.
    """
    wanted = set()
    for node in disease_cache.values():
        wanted.update(top_genes_by_assoc(node, GENES_FOR_INTERACTIONS))
    cache = load_cache("interactions")
    todo = sorted(wanted - set(cache))
    print("interactions: %d genes of interest, %d cached, %d to fetch"
          % (len(wanted), len(cache), len(todo)))
    for start in range(0, len(todo), INTERACTION_BATCH):
        chunk = todo[start:start + INTERACTION_BATCH]
        parts = []
        for i, ens in enumerate(chunk):
            parts.append("""
  %s: target(ensemblId: "%s") {
    id approvedSymbol
    interactions(scoreThreshold: %s, page: {index: 0, size: %d}) {
      count
      rows { score sourceDatabase targetB { id approvedSymbol } }
    }
  }""" % (alias("x", i), ens, INTERACTION_MIN_SCORE, PARTNERS_PER_GENE))
        data = gql("query {" + "\n".join(parts) + "\n}")
        for i, ens in enumerate(chunk):
            node = data.get(alias("x", i))
            rows = []
            if node and node.get("interactions"):
                seen = set()
                for row in node["interactions"]["rows"]:
                    partner = row.get("targetB") or {}
                    pid = partner.get("id")
                    if not pid or pid == ens or pid in seen:
                        continue
                    seen.add(pid)
                    rows.append({"id": pid, "symbol": partner.get("approvedSymbol"),
                                 "score": row["score"], "source": row.get("sourceDatabase")})
            cache[ens] = {"id": ens, "partners": rows}
        save_cache("interactions", cache)
        print("  %d/%d genes" % (min(start + INTERACTION_BATCH, len(todo)), len(todo)))
    return cache


def partner_gene_ids(interaction_cache):
    ids = set()
    for node in interaction_cache.values():
        for partner in node["partners"]:
            ids.add(partner["id"])
    return ids


def fetch_drugs(gene_cache):
    wanted = set()
    for node in gene_cache.values():
        for row in node["drugAndClinicalCandidates"]["rows"]:
            drug = row.get("drug") or {}
            parent = drug.get("parentMolecule") or drug
            if parent.get("id"):
                wanted.add(parent["id"])
    cache = load_cache("drugs")
    todo = sorted(wanted - set(cache))
    print("drugs: %d unique, %d cached, %d to fetch" % (len(wanted), len(cache), len(todo)))
    for start in range(0, len(todo), DRUG_BATCH):
        chunk = todo[start:start + DRUG_BATCH]
        parts = []
        for i, chembl in enumerate(chunk):
            parts.append("""
  %s: drug(chemblId: "%s") {
    id name drugType maximumClinicalStage
    mechanismsOfAction { rows { mechanismOfAction actionType } }
    indications { rows { maxClinicalStage disease { id name } } }
    drugWarnings { warningType toxicityClass description }
  }""" % (alias("m", i), chembl))
        data = gql("query {" + "\n".join(parts) + "\n}")
        for i, chembl in enumerate(chunk):
            node = data[alias("m", i)]
            if node is None:
                continue
            moa = [r["mechanismOfAction"] for r in (node.get("mechanismsOfAction") or {}).get("rows", [])]
            inds = [r["disease"]["name"] for r in (node.get("indications") or {}).get("rows", [])
                    if r.get("maxClinicalStage") == "APPROVAL" and r.get("disease")]
            seen, approved_for = set(), []
            for name in inds:
                if name.lower() not in seen:
                    seen.add(name.lower())
                    approved_for.append(name)
            # Safety matters here: we are suggesting existing drugs for new
            # uses, and a reader deserves to know if one was withdrawn or
            # carries a black box warning before it is treated as a lead.
            warnings, seen_w = [], set()
            for row in (node.get("drugWarnings") or []):
                label = row.get("warningType")
                tox = row.get("toxicityClass") or row.get("description")
                key = (label, tox)
                if not label or key in seen_w:
                    continue
                seen_w.add(key)
                warnings.append({"type": label, "detail": tox})
            cache[chembl] = {
                "id": node["id"],
                "name": node["name"],
                "warnings": warnings[:6],
                "withdrawn": any(w["type"] == "Withdrawn" for w in warnings),
                "blackBox": any(w["type"] == "Black Box Warning" for w in warnings),
                "drugType": node.get("drugType"),
                "maximumClinicalStage": node.get("maximumClinicalStage"),
                "mechanisms": moa[:3],
                "approvedFor": approved_for[:4],
                "indicationCount": len(approved_for),
            }
        save_cache("drugs", cache)
        print("  %d/%d drugs" % (min(start + DRUG_BATCH, len(todo)), len(todo)))
    return cache


if __name__ == "__main__":
    os.makedirs(RAW, exist_ok=True)
    t0 = time.time()
    d = fetch_diseases()
    fetch_genes(d)
    x = fetch_interactions(d)
    g = fetch_genes_for(partner_gene_ids(x))
    fetch_drugs(g)
    print("done in %.0fs" % (time.time() - t0))
