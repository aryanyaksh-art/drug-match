"""Is "novel" always actually novel?

Our candidates are drugs NOT in the disease's own drugAndClinicalCandidates
list. That list comes from a disease-to-drug edge in Open Targets. Each
drug's OWN record separately carries its own approvedFor list, built from
Drug.indications rather than from the disease side. These two should agree.
When they do not, our "novel" label is wrong -- not because our method
failed, but because the upstream database has two records, or two edges,
that disagree with each other about the same real-world drug.

This is checked entirely from data already cached; no new fetch. It found
one clean, manually verified case worth naming directly: elivaldogene
autotemcel (marketed as Skysona, FDA-approved for X-linked
adrenoleukodystrophy in 2022) is CHEMBL4594333, correctly marked APPROVAL
with approvedFor including ALD. But the disease-side edge for ALD points to
CHEMBL3990046, "elivaldogene tavalentivec" -- an old development-code name
for what appears to be the same product, still sitting at PHASE_3. Because
the two ChEMBL IDs never resolved to each other, our engine had no way to
know CHEMBL4594333 was already the answer, and surfaced it as new.

The broader sweep below is honestly noisier than that one case. Disease
names are matched with word-overlap and substring rules, which catches some
further real duplicate-ID bugs but also flags plenty of legitimate ambiguity
-- a drug tagged generically as approved for "arthritis" is not obviously
wrong to exclude from a specific-osteoarthritis candidate list, and we have
not manually verified each hit the way we verified the ALD case. Report the
aggregate as what it is: a lower bound on a real problem, mixed with matching
noise, not a confirmed bug count.
"""
import json
import os
import re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
RESULTS = os.path.join(ROOT, "web", "data", "results")
DRUGS = os.path.join(ROOT, "data", "raw", "drugs.json")
OUT = os.path.join(ROOT, "web", "data", "novelty_audit.json")

STOPWORDS = {"disease", "syndrome", "type", "of", "the", "and"}


def norm(s):
    return re.sub(r"[^a-z0-9 ]", "", s.lower()).strip()


def words(s):
    return set(norm(s).split()) - STOPWORDS


def main():
    with open(DRUGS, encoding="utf-8") as fh:
        drugs = json.load(fh)

    flagged, checked = [], 0
    for fn in os.listdir(RESULTS):
        with open(os.path.join(RESULTS, fn), encoding="utf-8") as fh:
            d = json.load(fh)
        if d.get("rarity") not in ("rare", "common"):
            continue
        disease_name = norm(d["name"])
        disease_words = words(d["name"])
        for c in d["candidates"]:
            checked += 1
            meta = drugs.get(c["id"], {})
            for approved_for in meta.get("approvedFor", []):
                af_name, af_words = norm(approved_for), words(approved_for)
                if (disease_name in af_name or af_name in disease_name
                        or (len(disease_words) >= 2 and disease_words <= af_words)):
                    flagged.append({
                        "disease": d["name"], "drug": c["name"], "drugId": c["id"],
                        "candidateRank": c["rank"], "approvedForClaim": approved_for,
                    })
                    break

    print("checked %d novel-candidate entries across curated diseases" % checked)
    print("flagged as self-contradicted (fuzzy match, includes noise): %d (%.2f%%)"
          % (len(flagged), 100 * len(flagged) / checked))
    print()
    print("verified example, not just fuzzy-matched:")
    print("  X-linked adrenoleukodystrophy -> Elivaldogene Autotemcel (CHEMBL4594333)")
    print("  Open Targets marks this exact record APPROVAL with approvedFor=ALD.")
    print("  The disease-side edge instead points to CHEMBL3990046, an old")
    print("  development-code synonym ('elivaldogene tavalentivec') stuck at PHASE_3.")
    print("  Two ChEMBL records for the same real drug, never resolved to each other.")

    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump({
            "checked": checked, "flaggedCount": len(flagged),
            "verifiedExample": {
                "disease": "X-linked adrenoleukodystrophy",
                "drugSurfacedAsNovel": {"name": "Elivaldogene Autotemcel", "id": "CHEMBL4594333"},
                "staleDiseaseEdge": {"name": "Elivaldogene Tavalentivec", "id": "CHEMBL3990046",
                                     "stage": "PHASE_3"},
            },
            "flagged": flagged,
        }, fh, indent=1)
    print()
    print("written to web/data/novelty_audit.json")


if __name__ == "__main__":
    main()
