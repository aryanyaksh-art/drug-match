"""The disease set Off The Shelf covers.

Rare diseases are the point of the project. The common ones are here for
validation density: rare diseases have too few known approved drugs to
measure ranking quality against on their own.

IDs were resolved once from the Open Targets search API and hard-coded so
the pipeline is reproducible and does not depend on search ranking. Where
search returned a phenotype term (HP_*) or a gene ahead of the disease,
the disease term was chosen by hand -- e.g. hypertension is MONDO_0005044,
not the phenotype HP_0000822.
"""

RARE = [
    # neuromuscular and neurodegenerative
    ("MONDO_0010679", "Duchenne muscular dystrophy"),
    ("MONDO_0004976", "Amyotrophic lateral sclerosis"),
    ("MONDO_0001516", "Spinal muscular atrophy"),
    ("MONDO_0100339", "Friedreich ataxia"),
    ("MONDO_0007739", "Huntington disease"),
    ("MONDO_0015626", "Charcot-Marie-Tooth disease"),
    ("MONDO_0000437", "Spinocerebellar ataxia"),
    ("MONDO_0009688", "Myasthenia gravis"),
    # neurodevelopmental
    ("MONDO_0010726", "Rett syndrome"),
    ("MONDO_0007113", "Angelman syndrome"),
    ("MONDO_0008300", "Prader-Willi syndrome"),
    ("MONDO_0010383", "Fragile X syndrome"),
    ("MONDO_0100135", "Dravet syndrome"),
    ("MONDO_0016532", "Lennox-Gastaut syndrome"),
    ("MONDO_0001734", "Tuberous sclerosis"),
    ("MONDO_0018975", "Neurofibromatosis type 1"),
    ("MONDO_0021107", "Narcolepsy"),
    # metabolic and storage
    ("MONDO_0008753", "Alkaptonuria"),
    ("MONDO_0010526", "Fabry disease"),
    ("MONDO_0018150", "Gaucher disease"),
    ("MONDO_0009290", "Pompe disease"),
    ("MONDO_0009861", "Phenylketonuria"),
    ("MONDO_0010200", "Wilson disease"),
    ("MONDO_0018982", "Niemann-Pick disease type C"),
    ("MONDO_0010100", "Tay-Sachs disease"),
    ("MONDO_0018868", "Metachromatic leukodystrophy"),
    ("MONDO_0018544", "X-linked adrenoleukodystrophy"),
    ("MONDO_0001586", "Mucopolysaccharidosis type I"),
    ("MONDO_0010674", "Mucopolysaccharidosis type II"),
    ("MONDO_0016239", "Cystinosis"),
    ("MONDO_0004737", "Homocystinuria"),
    ("MONDO_0009563", "Maple syrup urine disease"),
    ("MONDO_0010703", "Ornithine transcarbamylase deficiency"),
    ("MONDO_0018116", "Galactosemia"),
    ("MONDO_0002413", "Glycogen storage disease type I"),
    ("MONDO_0009723", "Leigh syndrome"),
    ("MONDO_0010789", "MELAS syndrome"),
    ("MONDO_0013282", "Alpha-1 antitrypsin deficiency"),
    ("MONDO_0006507", "Hereditary hemochromatosis"),
    # blood
    ("MONDO_0011382", "Sickle cell disease"),
    ("MONDO_0019402", "Beta thalassemia"),
    ("MONDO_0010602", "Hemophilia A"),
    ("MONDO_0100244", "Paroxysmal nocturnal hemoglobinuria"),
    ("MONDO_0018634", "Transthyretin amyloidosis"),
    # connective tissue and skeletal
    ("MONDO_0007947", "Marfan syndrome"),
    ("MONDO_0007037", "Achondroplasia"),
    ("MONDO_0020066", "Ehlers-Danlos syndrome"),
    ("MONDO_0019019", "Osteogenesis imperfecta"),
    ("MONDO_0007606", "Fibrodysplasia ossificans progressiva"),
    ("MONDO_0018997", "Noonan syndrome"),
    # skin and autoimmune
    ("MONDO_0006541", "Epidermolysis bullosa"),
    ("MONDO_0008219", "Pemphigus vulgaris"),
    ("MONDO_0005100", "Systemic sclerosis"),
    ("MONDO_0010030", "Sjogren syndrome"),
    ("MONDO_0007191", "Behcet disease"),
    ("MONDO_0019623", "Hereditary angioedema"),
    # kidney
    ("MONDO_0018965", "Alport syndrome"),
    ("MONDO_0100313", "Focal segmental glomerulosclerosis"),
    ("MONDO_0004691", "Autosomal dominant polycystic kidney disease"),
    ("MONDO_0002474", "Primary hyperoxaluria"),
    # eye
    ("MONDO_0019200", "Retinitis pigmentosa"),
    ("MONDO_0018998", "Leber congenital amaurosis"),
    ("MONDO_0019353", "Stargardt disease"),
    ("MONDO_0019501", "Usher syndrome"),
    # lung, liver, other
    ("MONDO_0009061", "Cystic fibrosis"),
    ("EFO_0000768", "Idiopathic pulmonary fibrosis"),
    ("MONDO_0015924", "Pulmonary arterial hypertension"),
    ("MONDO_0005388", "Primary biliary cholangitis"),
]

COMMON = [
    ("MONDO_0005148", "Type 2 diabetes mellitus"),
    ("MONDO_0005147", "Type 1 diabetes mellitus"),
    ("MONDO_0008383", "Rheumatoid arthritis"),
    ("MONDO_0004979", "Asthma"),
    ("MONDO_0005044", "Hypertension"),
    ("MONDO_0005180", "Parkinson disease"),
    ("MONDO_0004975", "Alzheimer disease"),
    ("MONDO_0005083", "Psoriasis"),
    ("MONDO_0005011", "Crohn disease"),
    ("MONDO_0005027", "Epilepsy"),
    ("MONDO_0004989", "Breast carcinoma"),
    ("MONDO_0005002", "Chronic obstructive pulmonary disease"),
    ("MONDO_0005101", "Ulcerative colitis"),
    ("MONDO_0005301", "Multiple sclerosis"),
    ("MONDO_0007915", "Systemic lupus erythematosus"),
    ("MONDO_0005306", "Ankylosing spondylitis"),
    ("MONDO_0005393", "Gout"),
    ("MONDO_0005298", "Osteoporosis"),
    ("MONDO_0005252", "Heart failure"),
    ("MONDO_0004981", "Atrial fibrillation"),
    ("MONDO_0005010", "Coronary artery disease"),
    ("MONDO_0005300", "Chronic kidney disease"),
    ("MONDO_0011122", "Obesity"),
    ("MONDO_0005277", "Migraine"),
    ("MONDO_0002009", "Major depressive disorder"),
    ("MONDO_0005090", "Schizophrenia"),
    ("MONDO_0004985", "Bipolar disorder"),
    ("MONDO_0004980", "Atopic dermatitis"),
    ("MONDO_0005178", "Osteoarthritis"),
    ("MONDO_0005041", "Glaucoma"),
    ("MONDO_0005150", "Age-related macular degeneration"),
    ("MONDO_0005105", "Melanoma"),
]

ALL = [(i, n, "rare") for i, n in RARE] + [(i, n, "common") for i, n in COMMON]

RARITY = {i: r for i, _, r in ALL}
NAMES = {i: n for i, n, _ in ALL}

assert len(NAMES) == len(ALL), "duplicate disease id in the list"
