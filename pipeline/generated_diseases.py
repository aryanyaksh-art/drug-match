"""Diseases selected programmatically by pipeline/select_diseases.py.

Rule: at least 50 associated genes and at least 1 known drug,
ordered by ontology id and cut at 320. Not hand-picked.
"""

GENERATED = [
    ("EFO_0000551", "intracranial hemorrhage"),  # 828 genes, 20 known drugs
    ("EFO_0000658", "plexiform neurofibroma"),  # 763 genes, 29 known drugs
    ("EFO_0001063", "deafness"),  # 2289 genes, 1 known drugs
    ("EFO_0001425", "ischemic cardiomyopathy"),  # 821 genes, 15 known drugs
    ("EFO_0002616", "macroglobulinemia"),  # 676 genes, 1 known drugs
    ("EFO_0002970", "muscular disease"),  # 6886 genes, 3 known drugs
    ("EFO_0003759", "pervasive developmental disorder - not otherwise specified"),  # 98 genes, 3 known drugs
    ("EFO_0003826", "salivary gland neoplasm"),  # 254 genes, 7 known drugs
    ("EFO_0003867", "rhabdomyolysis"),  # 510 genes, 7 known drugs
    ("EFO_0003899", "contracture"),  # 487 genes, 3 known drugs
    ("EFO_0003959", "cleft lip"),  # 942 genes, 6 known drugs
    ("EFO_0004149", "neuropathy"),  # 2484 genes, 12 known drugs
    ("EFO_0004229", "Dupuytren Contracture"),  # 394 genes, 6 known drugs
    ("EFO_0004251", "myeloproliferative disorder"),  # 1724 genes, 52 known drugs
    ("EFO_0004267", "biliary liver cirrhosis"),  # 872 genes, 5 known drugs
    ("EFO_0005288", "non-small cell lung adenocarcinoma"),  # 180 genes, 17 known drugs
    ("EFO_0005802", "cartilage disease"),  # 344 genes, 4 known drugs
    ("EFO_0007456", "pseudomyxoma peritonei"),  # 194 genes, 16 known drugs
    ("EFO_0007949", "acute-on-chronic liver failure"),  # 226 genes, 18 known drugs
    ("EFO_0008493", "cerebral small vessel disease"),  # 602 genes, 10 known drugs
    ("EFO_0008497", "chronic lung allograft dysfunction"),  # 126 genes, 19 known drugs
    ("EFO_0008526", "status epilepticus"),  # 958 genes, 28 known drugs
    ("EFO_0008532", "clinically amyopathic dermatomyositis"),  # 74 genes, 1 known drugs
    ("EFO_0008553", "femur fracture"),  # 174 genes, 5 known drugs
    ("EFO_0008556", "Methicillin-Resistant Staphylococcus Aureus Pneumonia"),  # 95 genes, 2 known drugs
    ("EFO_0008587", "gender identity disorder"),  # 393 genes, 3 known drugs
    ("EFO_0009048", "Intrahepatic cholestasis of pregnancy"),  # 475 genes, 4 known drugs
    ("EFO_0009093", "choroidal melanoma"),  # 186 genes, 2 known drugs
    ("EFO_0009104", "hyperuricemia"),  # 900 genes, 30 known drugs
    ("EFO_0009260", "non-melanoma skin carcinoma"),  # 508 genes, 5 known drugs
    ("EFO_0009361", "colorectal mucinous adenocarcinoma"),  # 75 genes, 3 known drugs
    ("EFO_0009364", "non-allergic rhinitis"),  # 57 genes, 9 known drugs
    ("EFO_0009510", "peripheral nerve injury"),  # 807 genes, 9 known drugs
    ("EFO_0009523", "fecal incontinence"),  # 87 genes, 24 known drugs
    ("EFO_0009541", "disease of peritoneum"),  # 1398 genes, 2 known drugs
    ("EFO_0009669", "flatulence"),  # 278 genes, 1 known drugs
    ("EFO_0009706", "latent autoimmune diabetes in adults"),  # 163 genes, 13 known drugs
    ("EFO_0009760", "non-proliferative diabetic retinopathy"),  # 342 genes, 23 known drugs
    ("EFO_0009783", "carotid atherosclerosis"),  # 675 genes, 2 known drugs
    ("EFO_0009784", "central serous retinopathy"),  # 102 genes, 19 known drugs
    ("EFO_0009854", "treatment resistant depression"),  # 312 genes, 23 known drugs
    ("EFO_0009881", "nonischemic cardiomyopathy"),  # 109 genes, 5 known drugs
    ("EFO_0009910", "chronic lung disease"),  # 644 genes, 15 known drugs
    ("EFO_0009959", "diverticular disease"),  # 734 genes, 1 known drugs
    ("EFO_0009963", "bipolar I disorder"),  # 260 genes, 41 known drugs
    ("EFO_0009964", "bipolar II disorder"),  # 71 genes, 10 known drugs
    ("EFO_0010098", "stress-related disorder"),  # 242 genes, 1 known drugs
    ("EFO_0010143", "chronic mountain sickness"),  # 53 genes, 5 known drugs
    ("EFO_0010445", "cocaine use disorder"),  # 244 genes, 46 known drugs
    ("EFO_0010638", "atopic asthma"),  # 488 genes, 7 known drugs
    ("EFO_0010702", "opioid use disorder"),  # 271 genes, 65 known drugs
    ("EFO_0010723", "ocular sarcoidosis"),  # 65 genes, 1 known drugs
    ("EFO_0011023", "concussion"),  # 384 genes, 23 known drugs
    ("EFO_0011052", "hepatotoxicity"),  # 158 genes, 7 known drugs
    ("EFO_0011057", "neurotoxicity"),  # 454 genes, 4 known drugs
    ("EFO_0020094", "Lambert-Eaton myasthenic syndrome"),  # 217 genes, 2 known drugs
    ("EFO_0020921", "hemorrhagic stroke"),  # 1883 genes, 9 known drugs
    ("EFO_0020983", "diffuse midline glioma"),  # 226 genes, 33 known drugs
    ("EFO_0020985", "central nervous system embryonal neoplasm"),  # 86 genes, 15 known drugs
    ("EFO_0022976", "inherited bone marrow failure syndrome"),  # 62 genes, 8 known drugs
    ("EFO_0700045", "cerebral malformation"),  # 1581 genes, 1 known drugs
    ("EFO_0700046", "congenital myotonia"),  # 62 genes, 2 known drugs
    ("EFO_0700059", "neuronal tumor"),  # 147 genes, 3 known drugs
    ("EFO_0700065", "hereditary ATTR amyloidosis"),  # 294 genes, 1 known drugs
    ("EFO_0801077", "cystic fibrosis-related diabetes"),  # 124 genes, 17 known drugs
    ("EFO_1000069", "Adamantinomatous Craniopharyngioma"),  # 103 genes, 2 known drugs
    ("EFO_1000178", "Chronic Eosinophilic Leukemia, Not Otherwise Specified"),  # 278 genes, 8 known drugs
    ("EFO_1000447", "Papillary Craniopharyngioma"),  # 55 genes, 2 known drugs
    ("EFO_1000466", "Penile Fibromatosis"),  # 107 genes, 1 known drugs
    ("EFO_1000603", "Unclassified Renal Cell Carcinoma"),  # 119 genes, 2 known drugs
    ("EFO_1000653", "sarcopenia"),  # 1691 genes, 31 known drugs
    ("EFO_1001012", "leptomeningeal metastasis"),  # 108 genes, 46 known drugs
    ("EFO_1001289", "Cholecystitis, Acute"),  # 100 genes, 5 known drugs
    ("EFO_1001311", "End Stage Liver Disease"),  # 315 genes, 6 known drugs
    ("EFO_1001390", "Peri-Implantitis"),  # 387 genes, 13 known drugs
    ("EFO_1001394", "Peritoneal Fibrosis"),  # 368 genes, 1 known drugs
    ("EFO_1001454", "amnesia"),  # 353 genes, 6 known drugs
    ("EFO_1001458", "diabetic cardiomyopathy"),  # 1203 genes, 6 known drugs
    ("EFO_1001480", "metastatic colorectal cancer"),  # 933 genes, 83 known drugs
    ("EFO_1001488", "influenza A (H1N1)"),  # 80 genes, 2 known drugs
    ("EFO_1001492", "atrophic macular degeneration"),  # 344 genes, 39 known drugs
    ("EFO_1001494", "psoriasis vulgaris"),  # 946 genes, 167 known drugs
    ("EFO_1001504", "small vessel stroke"),  # 135 genes, 3 known drugs
    ("EFO_1001513", "liver neoplasm"),  # 2316 genes, 3 known drugs
    ("EFO_1001514", "endometrial endometrioid carcinoma"),  # 264 genes, 6 known drugs
    ("EFO_1001515", "ovarian endometrioid carcinoma"),  # 221 genes, 3 known drugs
    ("EFO_1001761", "Angiofibroma"),  # 91 genes, 1 known drugs
    ("EFO_1001800", "Intervertebral Disc Displacement"),  # 351 genes, 1 known drugs
    ("EFO_1001829", "Posterior Leukoencephalopathy Syndrome"),  # 150 genes, 4 known drugs
    ("EFO_1001865", "ventilator-associated pneumonia"),  # 318 genes, 51 known drugs
    ("EFO_1001866", "ventral hernia"),  # 167 genes, 7 known drugs
    ("EFO_1001884", "dental phobia"),  # 52 genes, 13 known drugs
    ("EFO_1001927", "cutaneous squamous cell carcinoma"),  # 917 genes, 56 known drugs
    ("EFO_1001941", "bronchioloalveolar carcinoma"),  # 227 genes, 9 known drugs
    ("EFO_1001958", "high grade ovarian serous adenocarcinoma"),  # 56 genes, 1 known drugs
    ("EFO_1002002", "high altitude pulmonary edema"),  # 234 genes, 1 known drugs
    ("EFO_1002005", "lumbar disc herniation"),  # 344 genes, 18 known drugs
    ("EFO_1002027", "osteomalacia"),  # 146 genes, 2 known drugs
    ("EFO_1002028", "cicatricial alopecia"),  # 90 genes, 3 known drugs
    ("EFO_1002029", "chronic rhinosinusitis with nasal polyps"),  # 1122 genes, 22 known drugs
    ("EFO_1002030", "chronic rhinosinusitis without nasal polyps"),  # 416 genes, 6 known drugs
    ("HP_0000519", "Developmental cataract"),  # 300 genes, 2 known drugs
    ("HP_0000763", "Sensory neuropathy"),  # 325 genes, 3 known drugs
    ("HP_0000870", "Increased circulating prolactin concentration"),  # 84 genes, 5 known drugs
    ("HP_0000952", "Jaundice"),  # 565 genes, 3 known drugs
    ("HP_0001258", "Spastic paraplegia"),  # 1161 genes, 3 known drugs
    ("HP_0002043", "Esophageal stricture"),  # 76 genes, 12 known drugs
    ("HP_0002611", "Cholestatic liver disease"),  # 402 genes, 2 known drugs
    ("HP_0011141", "Age-related cataract"),  # 950 genes, 1 known drugs
    ("HP_0012076", "Borderline personality disorder"),  # 234 genes, 27 known drugs
    ("HP_0100309", "Subdural hemorrhage"),  # 221 genes, 15 known drugs
    ("MONDO_0000128", "giant axonal neuropathy"),  # 372 genes, 1 known drugs
    ("MONDO_0000153", "transposition of the great arteries"),  # 905 genes, 3 known drugs
    ("MONDO_0000159", "bone marrow failure syndrome"),  # 1160 genes, 12 known drugs
    ("MONDO_0000170", "microphthalmia, isolated, with coloboma"),  # 2294 genes, 1 known drugs
    ("MONDO_0000188", "GLUT1 deficiency syndrome"),  # 905 genes, 1 known drugs
    ("MONDO_0000212", "hypercalcemia, infantile"),  # 264 genes, 1 known drugs
    ("MONDO_0000257", "acute diarrhea"),  # 649 genes, 11 known drugs
    ("MONDO_0000270", "lower respiratory tract disorder"),  # 17617 genes, 1 known drugs
    ("MONDO_0000380", "paranasal sinus carcinoma"),  # 85 genes, 7 known drugs
    ("MONDO_0000386", "digestive system neuroendocrine tumor, grade 1/2"),  # 2794 genes, 33 known drugs
    ("MONDO_0000396", "spastic cerebral palsy"),  # 340 genes, 3 known drugs
    ("MONDO_0000402", "small cell carcinoma"),  # 4722 genes, 24 known drugs
    ("MONDO_0000447", "autosomal dominant polycystic liver disease"),  # 293 genes, 9 known drugs
    ("MONDO_0000448", "paraganglioma"),  # 1774 genes, 65 known drugs
    ("MONDO_0000450", "secondary progressive multiple sclerosis"),  # 607 genes, 8 known drugs
    ("MONDO_0000451", "primary progressive multiple sclerosis"),  # 411 genes, 4 known drugs
    ("MONDO_0000477", "focal dystonia"),  # 928 genes, 4 known drugs
    ("MONDO_0000481", "cervical dystonia"),  # 255 genes, 9 known drugs
    ("MONDO_0000500", "tongue squamous cell carcinoma"),  # 891 genes, 6 known drugs
    ("MONDO_0000503", "lung adenocarcinoma in situ"),  # 99 genes, 3 known drugs
    ("MONDO_0000510", "synucleinopathy"),  # 2832 genes, 1 known drugs
    ("MONDO_0000521", "salivary gland carcinoma"),  # 856 genes, 46 known drugs
    ("MONDO_0000527", "colon adenoma"),  # 900 genes, 2 known drugs
    ("MONDO_0000536", "pharyngeal squamous cell carcinoma"),  # 984 genes, 1 known drugs
    ("MONDO_0000548", "ovarian clear cell cancer"),  # 676 genes, 34 known drugs
    ("MONDO_0000568", "autoimmune disorder of central nervous system"),  # 4988 genes, 2 known drugs
    ("MONDO_0000594", "pervasive developmental disorder"),  # 5488 genes, 5 known drugs
    ("MONDO_0000607", "primary cutaneous T-cell non-Hodgkin lymphoma"),  # 2014 genes, 105 known drugs
    ("MONDO_0000616", "progesterone-receptor negative breast cancer"),  # 4741 genes, 2 known drugs
    ("MONDO_0000640", "central nervous system primitive neuroectodermal neoplasm"),  # 1830 genes, 8 known drugs
    ("MONDO_0000661", "alexithymia"),  # 69 genes, 1 known drugs
    ("MONDO_0000665", "apraxia"),  # 117 genes, 1 known drugs
    ("MONDO_0000702", "microscopic colitis"),  # 127 genes, 3 known drugs
    ("MONDO_0000703", "collagenous colitis"),  # 91 genes, 3 known drugs
    ("MONDO_0000704", "lymphocytic colitis"),  # 58 genes, 3 known drugs
    ("MONDO_0000726", "idiopathic scoliosis"),  # 1423 genes, 6 known drugs
    ("MONDO_0000744", "lung abscess"),  # 123 genes, 5 known drugs
    ("MONDO_0000771", "allergic respiratory disease"),  # 3093 genes, 3 known drugs
    ("MONDO_0000820", "cerebral cavernous malformation"),  # 1118 genes, 5 known drugs
    ("MONDO_0000837", "bone resorption disease"),  # 4021 genes, 2 known drugs
    ("MONDO_0000845", "fibrous dysplasia"),  # 1197 genes, 4 known drugs
    ("MONDO_0000872", "B-cell childhood acute lymphoblastic leukemia"),  # 104 genes, 32 known drugs
    ("MONDO_0000878", "cytomegalovirus retinitis"),  # 88 genes, 19 known drugs
    ("MONDO_0000903", "myoclonus-dystonia syndrome"),  # 501 genes, 2 known drugs
    ("MONDO_0000920", "duodenum cancer"),  # 1021 genes, 7 known drugs
    ("MONDO_0000956", "small intestine cancer"),  # 1172 genes, 7 known drugs
    ("MONDO_0000984", "thalassemia"),  # 2703 genes, 38 known drugs
    ("MONDO_0001020", "amblyopia"),  # 194 genes, 9 known drugs
    ("MONDO_0001039", "tonsillitis"),  # 603 genes, 12 known drugs
    ("MONDO_0001056", "gastric cancer"),  # 14520 genes, 378 known drugs
    ("MONDO_0001059", "gastric lymphoma"),  # 176 genes, 7 known drugs
    ("MONDO_0001063", "cardia cancer"),  # 217 genes, 8 known drugs
    ("MONDO_0001082", "lymph node cancer"),  # 5569 genes, 1 known drugs
    ("MONDO_0001103", "giardiasis"),  # 241 genes, 5 known drugs
    ("MONDO_0001126", "gastric ulcer"),  # 899 genes, 27 known drugs
    ("MONDO_0001162", "impulse control disorder"),  # 500 genes, 4 known drugs
    ("MONDO_0001170", "hemiplegia"),  # 1265 genes, 6 known drugs
    ("MONDO_0001187", "urinary bladder cancer"),  # 10839 genes, 88 known drugs
    ("MONDO_0001208", "acute respiratory failure"),  # 3883 genes, 52 known drugs
    ("MONDO_0001221", "esophageal varices"),  # 161 genes, 11 known drugs
    ("MONDO_0001235", "appendix cancer"),  # 301 genes, 4 known drugs
    ("MONDO_0001247", "social phobia"),  # 157 genes, 40 known drugs
    ("MONDO_0001251", "chronic apical periodontitis"),  # 89 genes, 2 known drugs
    ("MONDO_0001294", "Horner syndrome"),  # 586 genes, 2 known drugs
    ("MONDO_0001299", "diabetic autonomic neuropathy"),  # 53 genes, 3 known drugs
    ("MONDO_0001300", "autonomic neuropathy"),  # 749 genes, 4 known drugs
    ("MONDO_0001314", "chondrocalcinosis"),  # 484 genes, 7 known drugs
    ("MONDO_0001325", "penile cancer"),  # 355 genes, 23 known drugs
    ("MONDO_0001336", "familial hyperlipidemia"),  # 3716 genes, 49 known drugs
    ("MONDO_0001347", "facioscapulohumeral muscular dystrophy"),  # 826 genes, 8 known drugs
    ("MONDO_0001358", "bronchial disorder"),  # 6927 genes, 12 known drugs
    ("MONDO_0001369", "chronic laryngitis"),  # 181 genes, 1 known drugs
    ("MONDO_0001378", "urachus cancer"),  # 130 genes, 5 known drugs
    ("MONDO_0001382", "hepatorenal syndrome"),  # 155 genes, 14 known drugs
    ("MONDO_0001402", "vaginal cancer"),  # 242 genes, 28 known drugs
    ("MONDO_0001409", "esophagitis"),  # 1080 genes, 29 known drugs
    ("MONDO_0001416", "female reproductive organ cancer"),  # 17662 genes, 36 known drugs
    ("MONDO_0001437", "pulmonary alveolar proteinosis"),  # 1354 genes, 9 known drugs
    ("MONDO_0001442", "dysthymic disorder"),  # 212 genes, 9 known drugs
    ("MONDO_0001505", "alcoholic hepatitis"),  # 563 genes, 39 known drugs
    ("MONDO_0001517", "dysentery"),  # 644 genes, 3 known drugs
    ("MONDO_0001528", "vulva cancer"),  # 702 genes, 34 known drugs
    ("MONDO_0001572", "leiomyoma"),  # 2244 genes, 11 known drugs
    ("MONDO_0001577", "respiratory syncytial virus infectious disease"),  # 462 genes, 35 known drugs
    ("MONDO_0001583", "diabetic polyneuropathy"),  # 222 genes, 23 known drugs
    ("MONDO_0001590", "quadriplegia"),  # 111 genes, 5 known drugs
    ("MONDO_0001595", "choreatic disease"),  # 409 genes, 3 known drugs
    ("MONDO_0001606", "central nervous system leukemia"),  # 99 genes, 6 known drugs
    ("MONDO_0001627", "dementia"),  # 14795 genes, 96 known drugs
    ("MONDO_0001641", "severe pre-eclampsia"),  # 455 genes, 3 known drugs
    ("MONDO_0001657", "brain cancer"),  # 3868 genes, 63 known drugs
    ("MONDO_0001660", "proliferative diabetic retinopathy"),  # 586 genes, 24 known drugs
    ("MONDO_0001673", "diarrheal disease"),  # 2182 genes, 10 known drugs
    ("MONDO_0001676", "erythropoietic protoporphyria"),  # 521 genes, 12 known drugs
    ("MONDO_0001684", "exocrine pancreatic insufficiency"),  # 468 genes, 6 known drugs
    ("MONDO_0001707", "cardiac sarcoidosis"),  # 97 genes, 6 known drugs
    ("MONDO_0001708", "pulmonary sarcoidosis"),  # 568 genes, 30 known drugs
    ("MONDO_0001751", "cholestasis"),  # 3324 genes, 9 known drugs
    ("MONDO_0001780", "premature ejaculation"),  # 61 genes, 29 known drugs
    ("MONDO_0001824", "polyneuropathy"),  # 879 genes, 13 known drugs
    ("MONDO_0001835", "facial paralysis"),  # 1680 genes, 3 known drugs
    ("MONDO_0001879", "anus cancer"),  # 451 genes, 7 known drugs
    ("MONDO_0001941", "blindness (disorder)"),  # 1794 genes, 15 known drugs
    ("MONDO_0001942", "generalized anxiety disorder"),  # 466 genes, 61 known drugs
    ("MONDO_0001945", "postencephalitic Parkinson disease"),  # 477 genes, 2 known drugs
    ("MONDO_0001982", "Niemann-Pick disease"),  # 1601 genes, 3 known drugs
    ("MONDO_0002012", "methylmalonic acidemia"),  # 1550 genes, 3 known drugs
    ("MONDO_0002028", "personality disorder"),  # 349 genes, 1 known drugs
    ("MONDO_0002032", "colon carcinoma"),  # 9264 genes, 11 known drugs
    ("MONDO_0002038", "head and neck carcinoma"),  # 11037 genes, 23 known drugs
    ("MONDO_0002039", "cognitive disorder"),  # 15795 genes, 12 known drugs
    ("MONDO_0002045", "communicating hydrocephalus"),  # 400 genes, 1 known drugs
    ("MONDO_0002046", "alcohol abuse"),  # 1005 genes, 83 known drugs
    ("MONDO_0002050", "depressive disorder"),  # 6774 genes, 305 known drugs
    ("MONDO_0002076", "pneumothorax"),  # 424 genes, 7 known drugs
    ("MONDO_0002081", "musculoskeletal system disorder"),  # 18741 genes, 7 known drugs
    ("MONDO_0002087", "peritoneum cancer"),  # 727 genes, 88 known drugs
    ("MONDO_0002102", "cheilitis"),  # 217 genes, 3 known drugs
    ("MONDO_0002108", "thyroid cancer"),  # 12718 genes, 95 known drugs
    ("MONDO_0002113", "peritoneal carcinoma"),  # 577 genes, 20 known drugs
    ("MONDO_0002120", "neuroendocrine carcinoma"),  # 5284 genes, 90 known drugs
    ("MONDO_0002129", "bone cancer"),  # 14291 genes, 7 known drugs
    ("MONDO_0002135", "optic nerve disorder"),  # 3516 genes, 5 known drugs
    ("MONDO_0002142", "undifferentiated pleomorphic sarcoma"),  # 981 genes, 41 known drugs
    ("MONDO_0002158", "fallopian tube cancer"),  # 420 genes, 237 known drugs
    ("MONDO_0002165", "rectal neoplasm"),  # 4161 genes, 1 known drugs
    ("MONDO_0002169", "rectum adenocarcinoma"),  # 2314 genes, 58 known drugs
    ("MONDO_0002173", "neuroma"),  # 132 genes, 1 known drugs
    ("MONDO_0002177", "hyperinsulinism"),  # 5392 genes, 3 known drugs
    ("MONDO_0002183", "enthesopathy"),  # 232 genes, 2 known drugs
    ("MONDO_0002203", "constipation disorder"),  # 354 genes, 17 known drugs
    ("MONDO_0002211", "B cell deficiency"),  # 3038 genes, 3 known drugs
    ("MONDO_0002236", "ocular cancer"),  # 6891 genes, 1 known drugs
    ("MONDO_0002258", "pharyngitis"),  # 235 genes, 44 known drugs
    ("MONDO_0002268", "dyspepsia"),  # 392 genes, 45 known drugs
    ("MONDO_0002269", "gastroenteritis"),  # 6051 genes, 8 known drugs
    ("MONDO_0002271", "colon adenocarcinoma"),  # 8634 genes, 35 known drugs
    ("MONDO_0002321", "sensory peripheral neuropathy"),  # 2658 genes, 2 known drugs
    ("MONDO_0002352", "larynx cancer"),  # 2272 genes, 8 known drugs
    ("MONDO_0002358", "laryngeal carcinoma"),  # 2205 genes, 18 known drugs
    ("MONDO_0002367", "kidney cancer"),  # 14731 genes, 108 known drugs
    ("MONDO_0002400", "synovitis"),  # 651 genes, 12 known drugs
    ("MONDO_0002412", "disorder of glycogen metabolism"),  # 5435 genes, 2 known drugs
    ("MONDO_0002420", "tic disorder"),  # 635 genes, 11 known drugs
    ("MONDO_0002429", "idiopathic interstitial pneumonia"),  # 1223 genes, 1 known drugs
    ("MONDO_0002443", "bruxism"),  # 72 genes, 7 known drugs
    ("MONDO_0002444", "melancholia"),  # 86 genes, 3 known drugs
    ("MONDO_0002447", "endometrial carcinoma"),  # 12249 genes, 119 known drugs
    ("MONDO_0002465", "bronchiolitis"),  # 1286 genes, 27 known drugs
    ("MONDO_0002471", "bursitis"),  # 72 genes, 16 known drugs
    ("MONDO_0002491", "substance abuse"),  # 1890 genes, 2 known drugs
    ("MONDO_0002494", "substance-related disorder"),  # 4453 genes, 3 known drugs
    ("MONDO_0002501", "brain glioblastoma"),  # 1099 genes, 11 known drugs
    ("MONDO_0002507", "gingival overgrowth"),  # 607 genes, 1 known drugs
    ("MONDO_0002508", "gingivitis"),  # 520 genes, 37 known drugs
    ("MONDO_0002514", "hepatobiliary neoplasm"),  # 16145 genes, 9 known drugs
    ("MONDO_0002516", "digestive system cancer"),  # 19732 genes, 12 known drugs
    ("MONDO_0002522", "tenosynovial giant cell tumor"),  # 465 genes, 11 known drugs
    ("MONDO_0002525", "inherited lipid metabolism disorder"),  # 8689 genes, 103 known drugs
    ("MONDO_0002529", "skin squamous cell carcinoma"),  # 2858 genes, 20 known drugs
    ("MONDO_0002545", "spinal cord disorder"),  # 7470 genes, 2 known drugs
    ("MONDO_0002547", "nerve sheath neoplasm"),  # 2548 genes, 1 known drugs
    ("MONDO_0002561", "lysosomal storage disease"),  # 7404 genes, 8 known drugs
    ("MONDO_0002571", "primary central nervous system lymphoma"),  # 845 genes, 97 known drugs
    ("MONDO_0002572", "aspiration pneumonitis"),  # 123 genes, 9 known drugs
    ("MONDO_0002598", "germinoma"),  # 192 genes, 7 known drugs
    ("MONDO_0002602", "central nervous system disorder"),  # 20195 genes, 21 known drugs
    ("MONDO_0002614", "bone inflammation disease"),  # 10201 genes, 1 known drugs
    ("MONDO_0002635", "periodontal disorder"),  # 3845 genes, 39 known drugs
    ("MONDO_0002639", "glossopharyngeal nerve disorder"),  # 280 genes, 1 known drugs
    ("MONDO_0002647", "laryngitis"),  # 238 genes, 2 known drugs
    ("MONDO_0002656", "skin carcinoma"),  # 3152 genes, 7 known drugs
    ("MONDO_0002659", "uveal cancer"),  # 4935 genes, 1 known drugs
    ("MONDO_0002670", "ampulla of vater adenocarcinoma"),  # 211 genes, 14 known drugs
    ("MONDO_0002679", "cerebral infarction"),  # 1316 genes, 15 known drugs
    ("MONDO_0002691", "liver cancer"),  # 16051 genes, 111 known drugs
    ("MONDO_0002708", "retinitis"),  # 515 genes, 3 known drugs
    ("MONDO_0002714", "central nervous system cancer"),  # 13255 genes, 76 known drugs
    ("MONDO_0002715", "uterine cancer"),  # 16058 genes, 52 known drugs
    ("MONDO_0002728", "rhabdoid tumor"),  # 1293 genes, 20 known drugs
    ("MONDO_0002729", "rhabdoid tumor of the kidney"),  # 93 genes, 11 known drugs
    ("MONDO_0002746", "fallopian tube adenocarcinoma"),  # 58 genes, 13 known drugs
    ("MONDO_0002752", "ovarian adenocarcinoma"),  # 13818 genes, 15 known drugs
    ("MONDO_0002760", "bladder squamous cell carcinoma"),  # 80 genes, 3 known drugs
    ("MONDO_0002771", "pulmonary fibrosis"),  # 5323 genes, 56 known drugs
    ("MONDO_0002806", "bronchogenic carcinoma"),  # 216 genes, 3 known drugs
    ("MONDO_0002815", "acute myocarditis"),  # 141 genes, 2 known drugs
    ("MONDO_0002817", "adrenal gland cancer"),  # 4988 genes, 8 known drugs
    ("MONDO_0002836", "urethra transitional cell carcinoma"),  # 64 genes, 3 known drugs
    ("MONDO_0002887", "bile duct disorder"),  # 10381 genes, 1 known drugs
    ("MONDO_0002898", "skin cancer"),  # 6410 genes, 28 known drugs
    ("MONDO_0002911", "brain stem glioma"),  # 731 genes, 27 known drugs
    ("MONDO_0002921", "congenital structural myopathy"),  # 3765 genes, 1 known drugs
    ("MONDO_0002926", "clear cell sarcoma"),  # 275 genes, 21 known drugs
    ("MONDO_0002927", "spindle cell sarcoma"),  # 313 genes, 6 known drugs
    ("MONDO_0002928", "carcinosarcoma"),  # 6734 genes, 30 known drugs
    ("MONDO_0002959", "radiculopathy"),  # 95 genes, 10 known drugs
    ("MONDO_0002974", "cervical cancer"),  # 13512 genes, 236 known drugs
    ("MONDO_0002977", "autoimmune disorder of the nervous system"),  # 5771 genes, 7 known drugs
    ("MONDO_0003000", "central nervous system germ cell tumor"),  # 92 genes, 7 known drugs
    ("MONDO_0003001", "seminoma"),  # 1242 genes, 9 known drugs
    ("MONDO_0003004", "macular degeneration"),  # 5207 genes, 24 known drugs
    ("MONDO_0003005", "macular retinal edema"),  # 762 genes, 46 known drugs
    ("MONDO_0003014", "rhinitis"),  # 2060 genes, 20 known drugs
    ("MONDO_0003036", "mucoepidermoid carcinoma"),  # 696 genes, 1 known drugs
    ("MONDO_0003037", "hypotrichosis"),  # 968 genes, 3 known drugs
    ("MONDO_0003046", "anus neoplasm"),  # 555 genes, 3 known drugs
    ("MONDO_0003050", "lung large cell carcinoma"),  # 1195 genes, 2 known drugs
    ("MONDO_0003059", "bile duct cancer"),  # 8999 genes, 30 known drugs
]
