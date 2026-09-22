# Handoff

Written for a new session picking this up cold, human or Claude. Read this
before touching anything. Every number below was pulled directly from the
JSON files on disk on 2026-09-22, not recalled from memory, specifically
because an earlier session misquoted one of these numbers by eye and had
to correct it later. Don't repeat that: if you need a number, read the
JSON, don't recall the conversation.

## What this project is

Off The Shelf ranks already-approved drugs against diseases that have no
treatment, and shows the biological path connecting each suggestion. Built
for a TFSS HOSA club Biotechnology entry (originally framed as a tryout
task to join the club, not a formal competition). The user is Aryan
(aryanyaksh19@gmail.com), working with a partner named Sweta who may be
building an independent, separate version to compare against.

**Live site:** https://off-the-shelf-phi.vercel.app
**Repo:** https://github.com/aryanyaksh-art/off-the-shelf
**Local copy:** `C:\Users\aryan\OneDrive\Desktop\offtheshelf`, tracks
`origin/main`, pushes auto-deploy via a connected Vercel project
(`aryanyaksh-4231s-projects/off-the-shelf`, project id
`prj_W1gx3c9YnEpGxm8GPGUKk26UBQIt`). No manual deploy step needed: commit
and push to `main` and Vercel builds it.

## Repo layout

```
LICENSE, README.md, vercel.json, .gitignore    at root
docs/            CITATIONS.md, diagrams/, this file
pipeline/        the data pipeline, see pipeline/README.md for run order
web/             the deployed site (only this folder ships; vercel.json
                 sets outputDirectory: web)
```

`pipeline/diseases.py` holds the 100 hand-curated diseases (68 rare, 32
common) and is imported by every other pipeline script. Nothing else is
hand-picked: `pipeline/select_diseases.py` screens the Open Targets
ontology under 18 therapeutic areas against a fixed rule (>=50 associated
genes, >=1 known drug, no cap) and writes `pipeline/generated_diseases.py`
itself. That file is regenerated, not hand-edited.

## The method, in one paragraph

A drug reaches a disease through `drug -> targets -> gene -> associated
with -> disease` (2 hops), or `drug -> targets -> gene A -> interacts with
-> gene B -> associated with -> disease` (3 hops, added because the
disease-causing gene usually has no drug against it: HGD for alkaptonuria
and MECP2 for Rett both have zero). Every path a drug has into a disease is
summed, damped by `deg(drug)^0.4 * deg(gene)^0.4` (Rephetio's published
exponent, never tuned). The `clinical` and `known_drug` evidence
datatypes are excluded from scoring because Open Targets derives them
from known-drug evidence, which would leak the answer.

## Current numbers, verified against disk on 2026-09-22

Dataset: **2,549 diseases** (100 curated + 2,449 auto-selected), **599**
shipped to the browsable site, all 2,549 used for every validation figure.
**16,197** known drug-disease pairs tested across **1,682** evaluable
diseases (the other diseases had no known drug reach the candidate pool).

| Metric | Value |
|---|---|
| Median rank percentile (ours) | **37.1%** (random = 50%) |
| No damping (w=0) | 41.9% |
| Popularity baseline (ignores disease) | 58.0%, worse than random |
| Top-10% enrichment over chance | 1.76x |
| Bootstrap 95% CI (2000 resamples) | [35.6%, 38.3%], excludes random |
| Rare-disease-only median | 27.0% (n=478 pairs) |
| Top candidate is a known treatment | 196 of 1,682 diseases |
| Known treatment in top 5 | 527 of 1,682 diseases |
| Negative control (mismatched disease pairs) | 46.2%, tightening toward 50% |
| Conservative floor (all literature evidence removed) | 36.6%, still clear of chance |

**Evidence ablation** (positive delta = removing it hurts the score; this
is where an earlier session misread the sign once, so verify from
`web/data/analysis.json` if quoting):

```
animal_model         +0.0064   worst to remove, though the effect is small
rna_expression        +0.0007
affected_pathway      -0.0002
genetic_literature     -0.0002
literature              -0.0021
somatic_mutation         -0.0072
genetic_association       -0.0216   removing it actually improves the median
```

No single datatype dominates at this scale. The literature-leak worry from
early small-sample runs (a 4.7-point effect at 100 diseases) shrank to 0.2
points at 2,549 and is best read as small-sample noise, not a real risk.

**Interaction hop**, measured across all diseases: helps overall (832
improve, 634 worsen), and the benefit concentrates on rare diseases as
predicted before testing:

| Group | Direct only | With hop | Change |
|---|---|---|---|
| Rare | 32.1% | 26.9% | -5.2pp |
| Common | 33.3% | 30.5% | -2.9pp |
| Auto-selected | 39.4% | 38.1% | -1.3pp |

**Sparsity finding**: the original guess was that broad ontology terms
("cancer" as a category) explain the auto-selected set's worse
performance. That guess was wrong. Bucketing by associated-gene count, the
sparsest quartile does worst (40.1%) and the richest does best (35.3%).
Evidence volume is the limiting factor, not how broadly a disease is
named. This is why the curated set looked artificially good: Duchenne has
2,533 associated genes, alkaptonuria 441. Well-studied diseases, picked
without realizing that was the selection criterion.

**Genetic concordance check** (`pipeline/mechanism_direction.py`, scoped
to the curated 100 diseases only, 1,910 disease-gene pairs, 165 with
usable non-drug-derived direction evidence): already-approved drugs are
genetically concordant with independent human-genetics direction-of-effect
data **40.4%** of the time (n=47) vs **21.1%** for novel candidates
(n=147), two-proportion z-test p=0.0083. Excludes the `clinical_precedence`
datasource unconditionally, since it is itself derived from known drugs
and would make the check circular.

**Clinical trial cross-check** (`pipeline/trial_check.py`, top novel
candidate per curated disease, live ClinicalTrials.gov API): **14 of 100**
already have a registered trial. This number can drift slightly between
runs since it hits a live external API.

**Novelty audit** (`pipeline/audit_novelty.py`, fuzzy match against each
drug's own `approvedFor` field): **28 of 3,933** curated-disease
candidates flagged as possibly-already-approved. One fully verified case:
elivaldogene autotemcel (Skysona, FDA-approved for X-linked
adrenoleukodystrophy in 2022) was surfaced as novel because Open Targets
links the disease to a different, stale ChEMBL entry
(`CHEMBL3990046`, an old development-code duplicate) for the same real
drug. This flag now ships live on the site as `possiblyAlreadyApproved`
on each candidate, computed in `score.py`, not just documented after the
fact.

## Demo diseases (verified current)

- **Alkaptonuria**: nitisinone ranks 2 of 120. Real treatment, found by
  routing through the HGD-interacts-with-HPD hop since HGD itself has no
  drug. This is the strongest demo.
- **Huntington disease**: metformin ranks 1 of 352.
- **Angelman syndrome**: gaboxadol ranks 185 of 345, median 53.6%, worse
  than random. Deliberately kept in the set and flagged honestly on the
  site rather than hidden. Good to show on purpose, to demonstrate the
  tool knows its own limits.

## Frontend

Static site, no framework, no build step. `web/index.html` +
`web/style.css` + `web/app.js`, reads only precomputed JSON from
`web/data/`, makes zero network calls at runtime.

**Design**: light hero (cream `#F7F3EA`, near-black ink `#17140F`, tan
accent `#9C5B2E` light / `#C99B6B` dark) transitioning into a dark
substance zone (`#15130F`) for results and validation content. The split
is intentional and fixed, not tied to OS dark-mode preference (the old
`prefers-color-scheme` media query was removed). Applied via a `.dark`
wrapper class overriding the same CSS custom properties every component
already reads, so cards/badges/evidence-bars re-theme automatically with
no per-component changes needed.

**Hero image**: `web/assets/dna-hero.jpg`, an AI-generated photorealistic
DNA helix render (Gamma's `generate_image` tool, type=photo), regenerated
twice to get a textured/grainy surface and a floating (no cast shadow)
composition with the left third left plain for text to sit on. Full-bleed
background via `position:absolute; object-fit:cover`, with a left-to-right
scrim gradient for text legibility.

**Fonts**: Inter (body), Space Grotesk (brand, section headers, card
titles, nav), Instrument Serif (hero h1 only, weight 400, no other weight
ships for this family).

**Callouts**: three stat callouts on the hero image (disease count, known
pairs tested, rare-disease median), each a real dot marker positioned on
the actual visible helix plus a pill-card label connected by an SVG line
overlay. Numbers populate live from `index.json`/`validation.json` via
`renderHeroStats()` in app.js, never hardcoded.

**Copy style**: every visible and generated string follows a "stop slop"
rule set the user gave explicitly: active voice, no em dashes ever, no
filler openers, no repeated rhetorical-question headers, state facts
directly, vary sentence rhythm. Apply this to any future copy changes on
the site. It does not extend to code comments or commit messages, though
the user's personal "never use em dashes" preference is a good one to
just keep following everywhere going forward.

**A real bug found and fixed mid-session**: setting `display:flex` on
`.hero` (for its nav/content column layout) combined with `.wrap`'s
existing `margin:0 auto` caused `.wrap.wide` to shrink-wrap to its content
instead of stretching to its intended 1120px width. This is a known
flexbox interaction: explicit auto margins on a flex item with
`align-items:stretch` can suppress the stretch and center a
content-sized box instead. Fixed with `.hero>.wrap.wide{width:100%}`. If
you add more flex containers to the hero, watch for this again.

## Known tool quirks from this session

The Browser pane's screenshot capture (`mcp__Claude_Browser__computer`
with `action: screenshot`) was frequently unreliable: blank cream frames,
stale captures, or a tab reporting `innerWidth: 0` after being
re-navigated with `navigate`. The fix that worked reliably was opening a
**fresh tab** with `tabs_create` before testing, rather than reusing a tab
that had already been navigated multiple times. When screenshots are
unreliable, DOM inspection via `javascript_tool` (`getBoundingClientRect`,
`getComputedStyle`, `get_page_text`) is more trustworthy and was used for
most of this session's visual verification. Confirmed independently: the
user's own real Chrome browser rendered every version correctly when they
checked it themselves, so this was a pane-capture issue, not a site bug.

## What's not done

- **Prospective/time-split validation** was proposed early on (hold out
  drugs by approval date, test whether the method would have predicted
  them using only earlier evidence) but never built. Would be the
  strongest remaining rigor upgrade if there's time.
- **Expert review** of a handful of top novel candidates by an actual
  biologist or researcher was suggested, not done.
- The trial cross-check and novelty audit are both scoped to the curated
  100 diseases only, not the full 2,549. Expanding either is
  straightforward but was judged not worth the added runtime for the
  marginal value.
- **The slideshow** is explicitly out of scope for this codebase. The
  user and a friend are building it separately.
- Three PRD statistics still need real citations: the "7,000 rare
  diseases" and "300 million people" figures are sourced in
  `docs/CITATIONS.md` (the 300M figure is solid; the 7,000 figure comes
  from a different source than the 300M one and should be cited
  separately). The "only 5% have an FDA-approved treatment" claim could
  not be traced to a primary source. Recommended fix in
  `docs/CITATIONS.md`: say "the large majority have no approved
  treatment" instead, which the data supports and can't be challenged.

## Reproducing any number in this doc

```bash
cd pipeline
python select_diseases.py   # only if you want to regenerate the disease list
python fetch.py             # ~15-20 min cold, resumable, caches to data/raw/
python score.py
python validate.py
python analysis.py
python mechanism_direction.py
python trial_check.py
python audit_novelty.py
```

Full run order and what each script reads/writes:
[pipeline/README.md](../pipeline/README.md).
