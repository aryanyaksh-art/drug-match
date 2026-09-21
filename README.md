# Off The Shelf

Finds already-approved drugs that could treat diseases with no good treatment, and shows the biology behind each suggestion.

Type a disease, get a ranked list of existing drugs, each with the drug to gene to disease path that explains why.

Built for the TFSS HOSA club, Biotechnology prompt.

---

## The idea

Making a new drug takes over a decade. Meanwhile roughly two thousand drugs are already approved and already proven safe in people. For some disease with no treatment, one of them might already work and nobody has checked.

You cannot test every drug against every disease, so you need a way to guess which pairs deserve a scientist's time. Drugs work by hitting genes; diseases are linked to genes; so a drug that hits a gene linked to a disease is worth a look.

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

A gene that hundreds of drugs hit, or a drug that hits hundreds of genes, carries almost no information because everything connects through it. So each path is damped by the connectivity of the nodes it crosses. `w = 0.4` is the damping exponent published in Project Rephetio. Nothing is trained — it is a fixed formula, not a fitted model.

### Why the third hop exists

The gene that causes a rare disease usually has no drug against it. That is a large part of why the disease has no treatment. Alkaptonuria is caused by a broken HGD gene, and HGD has zero approved drugs. Rett syndrome's MECP2 has zero.

So a method that only looks at a disease's own genes finds nothing for exactly the diseases this project is about. Allowing one protein-interaction step fixes that: HGD interacts at 0.999 with HPD, and HPD's drug is nitisinone — the real approved treatment for alkaptonuria, which works by inhibiting HPD one step upstream of the broken enzyme.

Adding that hop moved nitisinone from rank 27 of 33 to **rank 2 of 119**.

Measured across every disease rather than that one case, the hop helps, but modestly and unevenly — 142 diseases improve, 124 worsen. The benefit concentrates exactly where the reasoning said it should:

| group | direct paths only | with the hop | change |
|---|---|---|---|
| rare | 33.8% | 28.4% | −5.4% |
| common | 33.7% | 31.1% | −2.6% |
| auto-selected | 39.0% | 38.3% | −0.7% |

Longer paths are not penalised by an invented constant. They damp naturally, because the interaction score is always below 1 and the third node introduces another degree term.

### The leakage problem

Open Targets scores gene–disease associations partly from a `clinical` evidence type, which is derived from **known drug evidence**. Duchenne muscular dystrophy scores 0.96 against NR3C1 largely *because* deflazacort already exists.

Scoring on that would mean reading the answer off the back of the book, and it would make any validation meaningless. So `clinical` and `known_drug` are excluded. Everything the ranking uses comes from genetics, animal models, expression and text mining.

This is also why no train/test split is needed: there are no fitted parameters to overfit, and leakage is handled at the evidence level instead.

---

## Does it work?

Measured against **4,089 drug–disease pairs already known to work**, across 307 diseases. Three rankings are compared over the identical candidate pool:

| method | top 5% | top 10% | top 25% | median |
|---|---|---|---|---|
| **ours** | **10.9%** | **18.3%** | **39.4%** | **33.5%** |
| no damping (w = 0) | 8.8% | 14.9% | 34.4% | 40.0% |
| popularity, disease ignored | 3.3% | 6.6% | 18.2% | 59.6% |
| random | 5.0% | 10.0% | 25.0% | 50.0% |

The popularity row is the important one. Ranking drugs by how many genes they hit, ignoring the disease entirely, does **worse than random**. So the biology is doing the work, not the arithmetic.

Bootstrapping over diseases — not over pairs, which are correlated within a disease — puts the median at **33.9%, 95% CI [31.8%, 36.4%]**. The interval excludes random.

For **59 of 307** diseases the single top-ranked candidate is already a real treatment, and for **118 of 307** one appears in the top five.

**Rare diseases are the best-served group**, at a 27.9% median against 33.5% overall. That is the point of the project, and it is not an accident — see the interaction hop below.

### Where it falls down

Eighty-nine of 307 diseases rank worse than random. They are not evenly spread:

| group | worse than random |
|---|---|
| rare, hand-curated | 7 of 68 |
| common, hand-curated | 2 of 32 |
| auto-selected | 80 of ~207 |

The auto-selected set is where the method struggles, and it drags the headline down from the 31.1% we saw on the curated set alone. Many of those diseases are broad ontology terms — "deafness", "peritoneal fibrosis" — where the disease definition is too vague for gene association to mean much.

That gap only became visible once we stopped choosing diseases ourselves, which is the argument for having stopped.

Two further honest notes:

- **Text mining carries more signal than any other evidence type.** That is uncomfortable, because papers co-mention a gene and a disease partly *because* a drug already links them, so literature evidence may quietly re-import what we excluded. Removing all literature-derived evidence moves the median to 36.4% — worse, but still clear of chance. The result does not rest on it.
- **The negative control does not fully collapse.** Scoring each disease against a different disease's known drugs gives 44.2%, not a clean 50%, because many diseases share common treatments so some drugs rank well everywhere.

Run `python pipeline/analysis.py` to reproduce all of this.

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

`fetch.py` is resumable — it skips anything already cached, so a failed run can just be re-run. A cold run takes about ten minutes.

The web app reads **only** precomputed JSON. It never calls an API, so it works with the wifi off. That is deliberate: a demo should not be able to fail because of a venue's network.

---

## Layout

```
pipeline/diseases.py   the curated 100 diseases, with resolved MONDO ids
pipeline/select_diseases.py  picks 320 more by a rule fixed in advance
pipeline/analysis.py   sensitivity, bootstrap, ablation, negative control
pipeline/fetch.py      Open Targets GraphQL, batched with aliases
pipeline/score.py      degree-weighted path scoring, 2-hop and 3-hop
pipeline/validate.py   ranks known treatments, compares against two baselines
data/raw/              cached API responses (not deployed)
web/                   the site, self-contained and deployable as-is
diagrams/              SVG diagrams for the presentation
CITATIONS.md           sources, verified rather than recalled
```

The set is 420 diseases: 68 rare and 32 common that we chose, plus 320 selected programmatically. The common ones are included for **validation density** — rare diseases have too few known approved drugs to measure ranking quality against on their own.

The 320 are chosen by `select_diseases.py`, which screens all 15,717 diseases under ten therapeutic areas against a rule written down before any result was seen: at least 50 associated genes and at least one known drug, ordered by ontology id. That ordering has nothing to do with quality, so the cut is not a hidden quality filter. The point is that nobody can ask whether we picked diseases we knew would work.

---

## Credits

- Method after [Himmelstein et al., *Systematic integration of biomedical knowledge prioritizes drugs for repurposing* (Project Rephetio), eLife 2017](https://doi.org/10.7554/eLife.26726)
- Data from the [Open Targets Platform](https://platform.opentargets.org/); protein interaction scores originate from STRING
- Related modern work: [Huang et al., TxGNN, *Nature Medicine* 2024](https://doi.org/10.1038/s41591-024-03233-x)

This is a simplified reimplementation of published ideas, not new research.

See [CITATIONS.md](CITATIONS.md) for sources behind every factual claim.

---

## Disclaimer

This is a hypothesis generator for researchers, not medical advice. Nothing here has been tested in patients for the disease it is listed under. Every candidate shown would require laboratory work and clinical trials before it could be used.
