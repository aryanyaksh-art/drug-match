# Citations

Sources for every factual claim we make. Verified against PubMed rather than
recalled, because these are the numbers a judge is most likely to challenge.

## Population burden of rare disease

> "263-446 million persons affected globally at any point in time"

Nguengang Wakap S, Lambert DM, Olry A, et al. *Estimating cumulative point
prevalence of rare diseases: analysis of the Orphanet database.*
European Journal of Human Genetics, 2020;28(2):165-173.
https://doi.org/10.1038/s41431-019-0508-0

What it actually says, exactly:

- **6,172** unique rare diseases catalogued in Orphanet
- **71.9%** of them genetic, **69.9%** exclusively paediatric onset
- Global point prevalence **3.5-5.9%** of the population
- Which equals **263-446 million people** worldwide
- Explicitly **excludes** rare cancers, infectious diseases and poisonings

**The "300 million" figure is fine to use** -- it sits inside that range and is
what EURORDIS quotes -- but cite it as "an estimated 300 million, within a
published range of 263-446 million" rather than as a precise count.

## The "more than 7,000 rare diseases" figure

This does **not** come from the paper above, which counts 6,172. The 7,000+
figure is the NIH GARD / NCATS count, which uses different inclusion rules.

Cite it to NCATS directly (https://rarediseases.info.nih.gov/) and do not
attribute both numbers to the same source. If a judge asks why the counts
differ, the answer is that "rare" is defined differently between jurisdictions
-- the paper notes national definitions ranging from 5 to 80 per 100,000.

## The "only 5% have an FDA-approved treatment" figure

**We have not pinned this to a primary source, and should say so or drop it.**

It is very widely repeated and traces to NCATS and FDA statements rather than
to a single peer-reviewed analysis we could verify. Options, in order of
preference:

1. Attribute it directly to NCATS as an agency statement, not to a study
2. Soften to "the large majority of rare diseases have no approved treatment",
   which follows from the Orphanet data and is safe
3. Leave it out

Do not present it as a research finding without a source in hand. Of our three
headline numbers this is the weakest, and it is the one worth ten minutes of
searching before the presentation.

## Method

Himmelstein DS, Lizee A, Hessler C, et al. *Systematic integration of
biomedical knowledge prioritizes drugs for repurposing.* eLife, 2017;6:e26726.
https://doi.org/10.7554/eLife.26726

The source of the degree-weighted path count and the damping exponent w = 0.4
that we use unchanged.

## Related modern work

Huang K, Chandak P, Wang Q, et al. *A foundation model for clinician-centered
drug repurposing.* Nature Medicine, 2024;30:3601-3613.
https://doi.org/10.1038/s41591-024-03233-x

Cited as context for where this field has gone. We do not implement it.

## Data source

Open Targets Platform. https://platform.opentargets.org/

Gene-disease associations, drug-target relationships, protein interactions
and known drug indications. Accessed September 2026 via the public GraphQL
API. Disease terms use the MONDO/EFO ontology; protein interaction scores in
our three-hop paths come from STRING via Open Targets.

## Attribution note

Article metadata above was retrieved from PubMed.
