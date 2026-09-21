"""The disease set Off The Shelf covers.

Rare diseases are the point of the project. The common ones are here for
validation density: rare diseases have too few known approved drugs to
measure ranking quality against on their own.

IDs were resolved once from the Open Targets search API and hard-coded so
the pipeline is reproducible and does not depend on search ranking.
"""

RARE = [
    ("MONDO_0010679", "Duchenne muscular dystrophy"),
    ("MONDO_0010726", "Rett syndrome"),
    ("MONDO_0008753", "Alkaptonuria"),
    ("MONDO_0010526", "Fabry disease"),
    ("MONDO_0004976", "Amyotrophic lateral sclerosis"),
    ("MONDO_0009061", "Cystic fibrosis"),
    ("MONDO_0007739", "Huntington disease"),
    ("MONDO_0011382", "Sickle cell disease"),
    ("MONDO_0001516", "Spinal muscular atrophy"),
    ("MONDO_0100339", "Friedreich ataxia"),
    ("MONDO_0010200", "Wilson disease"),
    ("MONDO_0018150", "Gaucher disease"),
    ("MONDO_0009290", "Pompe disease"),
    ("MONDO_0007947", "Marfan syndrome"),
    ("MONDO_0018975", "Neurofibromatosis type 1"),
    ("MONDO_0001734", "Tuberous sclerosis"),
    ("MONDO_0009861", "Phenylketonuria"),
    ("MONDO_0007037", "Achondroplasia"),
    ("MONDO_0007113", "Angelman syndrome"),
    ("MONDO_0008300", "Prader-Willi syndrome"),
]

COMMON = [
    ("MONDO_0005148", "Type 2 diabetes mellitus"),
    ("MONDO_0008383", "Rheumatoid arthritis"),
    ("MONDO_0004979", "Asthma"),
    ("MONDO_0005044", "Hypertension"),
    ("MONDO_0005180", "Parkinson disease"),
    ("MONDO_0004975", "Alzheimer disease"),
    ("MONDO_0005083", "Psoriasis"),
    ("MONDO_0005011", "Crohn disease"),
    ("MONDO_0005027", "Epilepsy"),
    ("MONDO_0004989", "Breast carcinoma"),
]

ALL = [(i, n, "rare") for i, n in RARE] + [(i, n, "common") for i, n in COMMON]

RARITY = {i: r for i, _, r in ALL}
NAMES = {i: n for i, n, _ in ALL}
