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

Longer paths are not penalised by an invented constant. They damp naturally, because the interaction score is always below 1 and the third node introduces another degree term.

### The leakage problem

Open Targets scores gene–disease associations partly from a `clinical` evidence type, which is derived from **known drug evidence**. Duchenne muscular dystrophy scores 0.96 against NR3C1 largely *because* deflazacort already exists.

Scoring on that would mean reading the answer off the back of the book, and it would make any validation meaningless. So `clinical` and `known_drug` are excluded. Everything the ranking uses comes from genetics, animal models, expression and text mining.

This is also why no train/test split is needed: there are no fitted parameters to overfit, and leakage is handled at the evidence level instead.

---

## Does it work?

Measured against **2,377 drug–disease pairs already known to work**, across 89 diseases. Three rankings are compared over the identical candidate pool:

| method | top 5% | top 10% | top 25% | median |
|---|---|---|---|---|
| **ours** | **12.3%** | **21.2%** | **42.3%** | **31.1%** |
| no damping (w = 0) | 9.4% | 16.5% | 35.9% | 38.7% |
| popularity, disease ignored | 2.9% | 5.3% | 16.7% | 60.3% |
| random | 5.0% | 10.0% | 25.0% | 50.0% |

The popularity row is the important one. Ranking drugs by how many genes they hit, ignoring the disease entirely, does **worse than random**. So the biology is doing the work, not the arithmetic.

Also: for **35 of 89** diseases the single top-ranked candidate is already a real treatment, and for **60 of 89** a real treatment appears in the top five.

**Rare diseases score better than common ones** — a 27.8% median against 31.1% overall — which is the point of the project.

### What it gets wrong

Nine of 89 diseases still rank worse than random, Angelman syndrome worst among them. They are left in the set rather than trimmed; cherry-picking the disease list would be the easiest way to fake a better number and the easiest thing to get caught doing. The interface flags thin results and explains why.

Two diseases could not be evaluated at all, because no drug already known to treat them reached the candidate pool.

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
pipeline/diseases.py   the 100 diseases covered, with resolved MONDO ids
pipeline/fetch.py      Open Targets GraphQL, batched with aliases
pipeline/score.py      degree-weighted path scoring, 2-hop and 3-hop
pipeline/validate.py   ranks known treatments, compares against two baselines
data/raw/              cached API responses (not deployed)
web/                   the site, self-contained and deployable as-is
diagrams/              SVG diagrams for the presentation
CITATIONS.md           sources, verified rather than recalled
```

Sixty-eight of the hundred diseases are rare. The common ones are included for **validation density** — rare diseases have too few known approved drugs to measure ranking quality against on their own.

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
