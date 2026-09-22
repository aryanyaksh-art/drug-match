<p align="center">
  <img src="web/assets/dna-hero.jpg" alt="Textured 3D render of a DNA double helix" width="100%">
</p>

# Off The Shelf

**[Live site: off-the-shelf-phi.vercel.app](https://off-the-shelf-phi.vercel.app)** · [How it works](#how-the-ranking-works) · [Does it work?](#does-it-work) · [License: MIT](LICENSE) · [Handoff doc for a new session](docs/HANDOFF.md)

Finds already-approved drugs that could treat diseases with no good treatment, and shows the biology behind each suggestion.

Type a disease, get a ranked list of existing drugs, each with the drug to gene to disease path that explains why.

Built for the TFSS HOSA club, Biotechnology prompt.

---

## The idea

Making a new drug takes over a decade. Meanwhile roughly two thousand drugs are already approved and already proven safe in people. For some disease with no treatment, one of them might already work and nobody has checked.

You cannot test every drug against every disease, so you need a way to guess which pairs deserve a scientist's time. Drugs work by hitting genes. Diseases are linked to genes. A drug that hits a gene linked to a disease is worth a look.

## How the ranking works

Every candidate is reached by a path. Two shapes count:

```
2 hops   drug --targets--> GENE --associated with--> disease
3 hops   drug --targets--> GENE A --interacts with--> GENE B --associated with--> disease
```

We sum every path a drug has into a disease. Paths are not counted equally:

```
score(drug, disease) = Σ   assoc(gene, disease)
                     paths ────────────────────────────
                            deg(drug)^0.4 · deg(gene)^0.4
```

A gene that hundreds of drugs hit, or a drug that hits hundreds of genes, carries almost no information because everything connects through it. So each path is damped by the connectivity of the nodes it crosses. `w = 0.4` is the damping exponent published in Project Rephetio. Nothing is trained. It is a fixed formula, not a fitted model.

### Why the third hop exists

The gene that causes a rare disease usually has no drug against it. That is a large part of why the disease has no treatment. Alkaptonuria is caused by a broken HGD gene, and HGD has zero approved drugs. Rett syndrome's MECP2 has zero.

So a method that only looks at a disease's own genes finds nothing for exactly the diseases this project is about. Allowing one protein-interaction step fixes that: HGD interacts at 0.999 with HPD, and HPD's drug is nitisinone, the real approved treatment for alkaptonuria, which works by inhibiting HPD one step upstream of the broken enzyme.

Adding that hop moved nitisinone from rank 27 of 33 to **rank 2 of 119**.

Measured across every disease rather than that one case, the hop helps, and more clearly at this scale: 650 diseases improve, 456 worsen. The benefit still concentrates where the reasoning said it should:

| group | direct paths only | with the hop | change |
|---|---|---|---|
| rare | 32.1% | 26.9% | −5.2% |
| common | 33.3% | 30.5% | −2.9% |
| auto-selected | 39.4% | 38.1% | −1.3% |

Rare diseases still gain roughly twice what common ones do, holding steady across every scale we've tested: 68 curated rare diseases, then 100, then thousands of auto-selected ones added around them.

Longer paths are not penalised by an invented constant. They damp naturally, because the interaction score is always below 1 and the third node introduces another degree term.

### The leakage problem

Open Targets scores gene–disease associations partly from a `clinical` evidence type, which is derived from **known drug evidence**. Duchenne muscular dystrophy scores 0.96 against NR3C1 largely *because* deflazacort already exists.

Scoring on that would mean reading the answer off the back of the book, and it would make any validation meaningless. So `clinical` and `known_drug` are excluded. Everything the ranking uses comes from genetics, animal models, expression and text mining.

This is also why no train/test split is needed: there are no fitted parameters to overfit, and leakage is handled at the evidence level instead.

---

## Does it work?

Measured against **16,197 drug–disease pairs already known to work**, across 1,682 diseases (of 2,549 total; the rest had no known drug reach the candidate pool). Three rankings are compared over the identical candidate pool:

| method | top 5% | top 10% | top 25% | median |
|---|---|---|---|---|
| **ours** | **9.5%** | **17.6%** | **36.8%** | **37.1%** |
| no damping (w = 0) | 8.5% | 15.6% | 33.5% | 41.9% |
| popularity, disease ignored | 4.0% | 8.4% | 20.8% | 58.0% |
| random | 5.0% | 10.0% | 25.0% | 50.0% |

Popularity, ranking drugs by how many genes they hit while ignoring the disease entirely, still does **worse than random** at 4.5x the scale. So the biology is doing the work, not the arithmetic.

Bootstrapping over diseases puts the median at **37.1%, 95% CI [35.6%, 38.3%]**. The interval excludes random.

For **196 of 1,682** diseases the single top-ranked candidate is already a real treatment, and for **527 of 1,682** one appears in the top five.

**Rare diseases remain the best-served group**, at a 27.0% median against 37.1% overall. The gap has held steady across every sample size we've tried.

### The headline keeps getting worse as the sample grows, on purpose

| Diseases | Median rank percentile |
|---|---|
| 100 (curated only) | 31.1% |
| 420 (100 curated + 320 auto-selected) | 33.5% |
| 1,887 (100 curated + 1,787 auto-selected) | 36.8% |
| 2,549 (100 curated + 2,449 auto-selected, 18 areas, no cap) | **37.1%** |

Every disease added past the curated 100 was added by a rule fixed in advance, not by us. The rule cannot tell whether a disease is easy or hard for the method. It only checks that enough data exists to test on. So the honest trend is that our curated set was flattering the result, and the number moves toward the truth as more of that flattery is diluted out. We are showing the whole trend rather than only the final number.

What does **not** move as the sample grows: popularity stays worse than random, damping still helps over no damping, rare diseases stay the best-served group, and alkaptonuria and Huntington remain the same two demos.

### Where it falls down

| group | worse than random |
|---|---|
| rare, hand-curated | 9 of 57 (16%) |
| common, hand-curated | 2 of 32 (6%) |
| auto-selected | 546 of 1,593 (34%) |

We tested *why* the auto-selected set does worse. The first guess was that broad ontology terms are categories rather than diseases. "Cancer" is not a thing you treat, and we thought that breadth would explain the failures. **That guess was wrong.** Bucketing every disease by how many genes are associated with it, the sparsest quartile does worst (40.1% at ~50-390 genes) and the richest quartile does best (35.3% at 2,500+ genes). The trend has held, and sharpened slightly, at every scale we've tested (a 4.8-point gap now, vs 2.8 at 420 diseases). It runs the opposite direction from the breadth guess. The limiting factor is how much is known about a disease, not how broadly it is named. That also explains why our curated set looked good in the first place: Duchenne has 2,533 associated genes, alkaptonuria 441. We had unknowingly picked well-studied diseases.

Two further honest notes, updated at this scale:

- **The literature-leak concern kept shrinking as the sample grew, and is now essentially gone.** At 100 diseases removing all literature-derived evidence cost 4.7 points; at 1,887 it cost 0.7; at 2,549 it costs 0.2. At this scale, `animal_model` is the single datatype whose removal hurts the score most, though the effect is tiny (0.6 points). Removing `genetic_association` actually improves the median slightly (2.2 points), which is a real, mildly surprising finding worth sitting with rather than a mistake we are correcting. No datatype dominates the ranking anymore. We are reporting the shift rather than picking whichever run supports the cleaner story. The honest read is that the original worry was mostly small-sample noise.
- **The negative control keeps tightening toward a clean 50% as the sample grows**, 42.5% at 100 diseases, 44.2% at 420, 46.3% at 1,887, 46.2% at 2,549. That is consistent with the small-sample gap being partly noise from diseases sharing common treatments in a smaller pool.

Run `python pipeline/analysis.py` to reproduce all of this.

---

## A sharper, independent check: does the mechanism point the right way?

Everything above asks "is this drug connected to this disease". This asks a harder question: for genes where human genetics tells us the *direction* of effect -- does losing this gene's function cause the disease, or protect against it -- does the drug's actual mechanism push in the direction that would help?

This echoes a well-known finding: [Nelson et al., *Nature Genetics* 2015](https://doi.org/10.1038/ng.3314) found that approved drugs are markedly more likely than chance to have a mechanism genetically concordant with their target disease. We built a simplified version of that check on our own data.

**The leakage trap here is worse than the one already solved.** Open Targets' direction-of-effect fields are populated for many pairs by `clinical_precedence` -- which is just "a drug with this mechanism is already approved for this disease," restated as evidence. Using it would make the whole check circular. We exclude `clinical_precedence` unconditionally and use only `eva` (ClinVar), `gene2phenotype`, `orphanet`, `genomics_england`, `gene_burden` and `uniprot_variants` -- independent human genetics, never drug history.

Scoped to the curated 100 diseases only, on the (disease, gene) pairs that actually appear in their scored candidate paths:

| | Genetic concordance |
|---|---|
| Already-approved drugs | **40.4%** (19 of 47 assessable) |
| Our novel candidates | **21.1%** (31 of 147 assessable) |

Two-proportion z-test: z = 2.64, p = 0.008. Real drugs are genetically concordant almost twice as often as our candidates, and that gap is unlikely to be noise despite the small sample.

**This is the honest reading:** genetic concordance is a real, independent signal our current ranking does not use. It did not have to line up with the literature -- it does, on the first alphabetical examples: **lumacaftor, tezacaftor, ivacaftor and elexacaftor for cystic fibrosis** (the real CFTR-modulator drug class) and **the urate-transporter inhibitors for gout** both fall out correctly, with the script having no built-in knowledge of what these drugs are.

**Caveats, stated plainly:** only 165 of 1,903 candidate pairs (8.7%) had unambiguous, non-drug-derived direction evidence at all -- most genes simply do not have this data. The sample (47 known, 147 novel) is small. This is reported as a diagnostic finding, not folded into the live ranking score, precisely because a signal this data-sparse should not be allowed to silently reweight a validated result days before a deadline. Filtering or boosting candidates by concordance where the data exists is a legitimate next step, not yet done.

Run `python pipeline/mechanism_direction.py` to reproduce this.

---

## Has the field already tried our top candidates?

For the single top-ranked novel candidate on each of the 100 curated diseases, we checked ClinicalTrials.gov directly (the public v2 API, no key needed) for a trial matching that exact drug and disease.

**16 of 100 already have a registered trial.** Two are worth naming specifically: **tofersen for Charcot-Marie-Tooth disease** (recruiting) and **tovorafenib for Noonan syndrome** (active) -- the second is mechanistically sound on its face, since Noonan syndrome is a RAS/MAPK pathway disorder and tovorafenib acts on that same pathway. Neither outcome should be oversold: a trial existing does not mean the drug works, and it does not mean our method predicted something novel -- only that the idea has already occurred to someone else too, which is a real form of external agreement worth having.

Run `python pipeline/trial_check.py` to reproduce this; results are in `web/data/trial_check.json`.

## Is "novel" always actually novel? One confirmed case says no.

Our candidates are drugs *not* in a disease's own known-drug list from Open Targets. That list, and a drug's own `approvedFor` field, come from different edges in the same database and do not always agree.

**One fully verified case:** for X-linked adrenoleukodystrophy, our engine surfaced **elivaldogene autotemcel** (marketed as Skysona, FDA-approved for ALD in 2022) as a "novel" candidate. It is not novel -- it is the real approved treatment. The bug is upstream: Open Targets correctly marks that exact ChEMBL record (`CHEMBL4594333`) as `APPROVAL` with ALD in its own `approvedFor` list, but the disease-side link for ALD instead points to a *different* ChEMBL entry, `CHEMBL3990046`, an old development-code synonym ("elivaldogene tavalentivec") still sitting at `PHASE_3`. Two database records for the same real-world drug, never resolved to each other -- our pipeline trusted the wrong edge.

A broader automated sweep, matching every curated disease's novel candidates against each drug's own `approvedFor` field, flags **28 of 3,933 entries (0.7%)**. We are not claiming all 28 are the same class of bug as the ALD case -- some are generic-category overlap in ChEMBL's own tagging (a drug tagged approved for "arthritis" broadly, flagged against a candidate list for osteoarthritis specifically), which is a real ambiguity in the source data, not necessarily an error. We did not hand-verify all 28 the way we verified ALD. Reported as a lower bound on a real problem, not a confirmed bug count.

We are naming this rather than quietly filtering it out, because a project that claims perfect novelty-detection and gets caught on one example looks far worse than one that found and disclosed the limitation itself.

Run `python pipeline/audit_novelty.py` to reproduce this; results are in `web/data/novelty_audit.json`.

---

## Running it

```bash
pip install requests
python pipeline/fetch.py      # pulls from Open Targets, caches to data/raw/
python pipeline/score.py      # ranks candidates  -> web/data/results/
python pipeline/validate.py   # measures quality  -> web/data/validation.json
```

Then serve the site:

```bash
cd web && python -m http.server
```

`fetch.py` is resumable. It skips anything already cached, so a failed run can just be re-run. A cold run takes about ten minutes. See [pipeline/README.md](pipeline/README.md) for the full run order, including the diagnostic scripts this quickstart skips.

The web app reads **only** precomputed JSON. It never calls an API, so it works with the wifi off. That is deliberate: a demo should not be able to fail because of a venue's network.

---

## Layout

```
pipeline/diseases.py   the curated 100 diseases, with resolved MONDO ids
pipeline/select_diseases.py  picks 320 more by a rule fixed in advance
pipeline/analysis.py   sensitivity, bootstrap, ablation, negative control
pipeline/mechanism_direction.py  genetic-concordance check (independent of the main score)
pipeline/trial_check.py  cross-checks top candidates against ClinicalTrials.gov
pipeline/audit_novelty.py  audits whether "novel" candidates really are
pipeline/fetch.py      Open Targets GraphQL, batched with aliases
pipeline/score.py      degree-weighted path scoring, 2-hop and 3-hop
pipeline/validate.py   ranks known treatments, compares against two baselines
data/raw/              cached API responses (not deployed)
web/                   the site, self-contained and deployable as-is
docs/diagrams/         SVG diagrams for the presentation
docs/CITATIONS.md      sources, verified rather than recalled
```

The set is 2,549 diseases: 68 rare and 32 common that we chose, plus 2,449 selected programmatically, every disease under 18 therapeutic areas meeting the rule, with no cap. The common ones are included for **validation density**: rare diseases have too few known approved drugs to measure ranking quality against on their own.

The 2,449 are chosen by `select_diseases.py`, which screens all 17,940 diseases under 18 therapeutic areas against a rule written down before any result was seen: at least 50 associated genes and at least one known drug. There is no cap. Every disease meeting the rule is included, so there is no cut that could be mistaken for a quality filter. The point is that nobody can ask whether we picked diseases we knew would work, because we did not pick them at all.

The area list started at 10 and grew to 18 (adding skin, eye, endocrine, urinary, reproductive, hematologic and ear disorders) once we went looking for more coverage. That pass also caught a real bug: one area id had been mislabeled "immune system disease" while actually pointing at respiratory system disorder, so immune system disease was never really screened as its own category until it was fixed. Separately, three other ids that worked in an earlier run started returning nothing at all. Open Targets appears to periodically merge or deprecate ontology terms, so an id that resolves today is not guaranteed to keep resolving. Re-resolved to their current equivalents rather than silently dropping those areas.

The website ships a bounded subset of the auto-selected diseases (data is ~65KB per disease; shipping all 2,449 would mean a multi-hundred-megabyte deployment for no benefit to someone searching it). Validation and every analysis figure use the full 2,549. The site footer states both numbers so nobody mistakes what is browsable for what was measured.

---

## Credits

- Method after [Himmelstein et al., *Systematic integration of biomedical knowledge prioritizes drugs for repurposing* (Project Rephetio), eLife 2017](https://doi.org/10.7554/eLife.26726)
- Data from the [Open Targets Platform](https://platform.opentargets.org/); protein interaction scores originate from STRING
- Related modern work: [Huang et al., TxGNN, *Nature Medicine* 2024](https://doi.org/10.1038/s41591-024-03233-x)

This is a simplified reimplementation of published ideas, not new research.

See [docs/CITATIONS.md](docs/CITATIONS.md) for sources behind every factual claim.

---

## Disclaimer

This is a hypothesis generator for researchers, not medical advice. Nothing here has been tested in patients for the disease it is listed under. Every candidate shown would require laboratory work and clinical trials before it could be used.
