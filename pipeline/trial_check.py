"""Has the field already independently arrived at our top candidates?

Everything else in this project asks whether our ranking agrees with drugs
already approved. This asks a different, useful question: for the drugs we
rank as NOVEL (not currently used for the disease), has anyone already
started testing that exact pairing in a real clinical trial?

Two outcomes, both informative:

  - A trial exists: either independent confirmation that the pairing is a
    reasonable idea, or evidence we are just rediscovering something already
    public. Either way, worth knowing before calling it "novel" on stage.
  - No trial exists: consistent with a genuinely unexplored candidate, or
    with the candidate being a bad idea nobody has bothered to test. This
    check cannot tell those apart -- it only tells you whether the idea has
    been tried, not whether it worked or was any good.

Uses the public ClinicalTrials.gov v2 API directly (no key required), for
the same reason score.py talks to Open Targets directly: reproducibility
without depending on this session's tool availability.

Scope: the single top-ranked NOVEL candidate for every curated disease
(rare + common), not the auto-selected set and not every candidate --
100 diseases is already 100 API calls, and going further would mean
querying thousands of candidates for a check that is meant to spot-audit
the highest-confidence suggestions, not exhaustively survey the field.
"""
import json
import os
import sys
import time

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diseases import NAMES, RARITY

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
RESULTS = os.path.join(ROOT, "web", "data", "results")
OUT = os.path.join(ROOT, "web", "data", "trial_check.json")

API = "https://clinicaltrials.gov/api/v2/studies"


def query(condition, intervention, tries=3):
    for attempt in range(tries):
        try:
            r = requests.get(API, params={
                "query.cond": condition,
                "query.intr": intervention,
                "pageSize": 5,
                "fields": "NCTId,BriefTitle,OverallStatus,Phase",
            }, timeout=25)
            if r.status_code == 200:
                return r.json().get("studies", [])
            if r.status_code == 429:
                raise RuntimeError("rate limited")
        except Exception:
            if attempt == tries - 1:
                return []
            time.sleep(2 ** attempt)
    return []


def top_novel_candidate(efo):
    path = os.path.join(RESULTS, efo + ".json")
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        d = json.load(fh)
    return d["candidates"][0] if d.get("candidates") else None


def main():
    curated = [efo for efo in NAMES if RARITY.get(efo) in ("rare", "common")]
    print("checking top novel candidate for %d curated diseases" % len(curated))

    results = []
    for i, efo in enumerate(curated):
        top = top_novel_candidate(efo)
        if not top:
            continue
        name = NAMES[efo]
        studies = query(name, top["name"])
        entry = {
            "disease": name, "diseaseId": efo, "rarity": RARITY[efo],
            "drug": top["name"], "rank": top["rank"], "score": top["score"],
            "trialsFound": len(studies),
            "trials": [{
                "nctId": s["protocolSection"]["identificationModule"].get("nctId"),
                "title": s["protocolSection"]["identificationModule"].get("briefTitle"),
                "status": s["protocolSection"].get("statusModule", {}).get("overallStatus"),
                "phase": s["protocolSection"].get("designModule", {}).get("phases"),
            } for s in studies[:3]],
        }
        results.append(entry)
        flag = "TRIAL EXISTS" if studies else "no trial found"
        print("  %-34s %-24s %s" % (name[:34], top["name"][:24], flag))
        if (i + 1) % 20 == 0:
            with open(OUT, "w", encoding="utf-8") as fh:
                json.dump(results, fh, indent=1)

    with_trials = [r for r in results if r["trialsFound"] > 0]
    print()
    print("%d of %d top novel candidates already have a registered trial for that exact disease"
          % (len(with_trials), len(results)))
    for r in with_trials:
        print("  %-34s %-24s -> %s (%s)" % (
            r["disease"][:34], r["drug"][:24],
            r["trials"][0]["nctId"], r["trials"][0]["status"]))

    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump({
            "scope": "top-ranked novel candidate per curated disease",
            "diseasesChecked": len(results),
            "withExistingTrial": len(with_trials),
            "results": results,
        }, fh, indent=1)
    print()
    print("written to web/data/trial_check.json")


if __name__ == "__main__":
    main()
