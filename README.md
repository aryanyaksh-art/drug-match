# Off The Shelf

Finds already-approved drugs that could treat diseases with no good treatment, and shows the biology behind each suggestion.

Type a disease, get a ranked list of existing drugs, each with the `drug → gene → disease` path that explains why.

Built for the TFSS HOSA club, Biotechnology prompt.

---

## What it actually does

Every candidate is reached by a two-step path: a drug **targets a gene**, and that gene is **associated with the disease**. The engine sums every such path a drug has into a disease.

Paths are not counted equally. A gene that hundreds of drugs hit — or a drug that hits hundreds of genes — carries little information, because everything connects through it. Each path is therefore damped by the connectivity of the nodes it crosses:

```
score(drug, disease) = Σ   assoc(gene, disease)
                     genes  ────────────────────────────────────
                            deg(drug)^0.4 · deg(gene)^0.4
```

`w = 0.4` is the damping exponent published in Project Rephetio. Nothing is trained — it is a fixed formula, not a fitted model.

### The leakage problem, and what we do about it

Open Targets scores gene–disease associations partly from a `clinical` evidence type, which is derived from **known drug evidence**. Duchenne muscular dystrophy scores 0.96 against NR3C1 largely *because* deflazacort already exists.

Scoring on that would mean reading the answer off the back of the book, and it would make any validation meaningless. So `clinical` and `known_drug` are excluded from the association score. Everything the ranking uses comes from genetics, animal models, expression and text mining.

This is why no train/test split is needed: there are no fitted parameters to overfit, and leakage is handled at the evidence level instead.

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

`fetch.py` is resumable — it skips anything already cached, so a failed run can just be re-run.

The web app reads **only** precomputed JSON. It never calls an API, so it works with the wifi off. That is deliberate: a demo should not be able to fail because of a venue's network.

---

## Layout

```
pipeline/diseases.py   the 30 diseases covered, with resolved MONDO ids
pipeline/fetch.py      Open Targets GraphQL, batched with aliases
pipeline/score.py      degree-weighted path scoring
pipeline/validate.py   ranks known treatments to measure quality
data/raw/              cached API responses (not deployed)
web/                   the site, self-contained and deployable as-is
```

Twenty of the thirty diseases are rare. The ten common ones are included for **validation density** — rare diseases have too few known approved drugs to measure ranking quality against on their own.

---

## Credits

- Method after [Himmelstein et al., *Systematic integration of biomedical knowledge prioritizes drugs for repurposing* (Project Rephetio), eLife 2017](https://doi.org/10.7554/eLife.26726)
- Data from the [Open Targets Platform](https://platform.opentargets.org/)
- Related modern work: [Huang et al., TxGNN, *Nature Medicine* 2024](https://doi.org/10.1038/s41591-024-03233-x)

This is a simplified reimplementation of published ideas, not new research.

---

## Disclaimer

This is a hypothesis generator for researchers, not medical advice. Nothing here has been tested in patients for the disease it is listed under. Every candidate shown would require laboratory work and clinical trials before it could be used.
