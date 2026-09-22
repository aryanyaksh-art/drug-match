"""Diseases selected programmatically by pipeline/select_diseases.py.

Rule: at least 50 associated genes and at least 1 known drug.
Every disease meeting it is included. Not hand-picked, not capped.
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
    ("MONDO_0003060", "biliary tract cancer"),  # 9042 genes, 151 known drugs
    ("MONDO_0003061", "benign muscle neoplasm"),  # 2270 genes, 2 known drugs
    ("MONDO_0003090", "extrahepatic bile duct carcinoma"),  # 8864 genes, 3 known drugs
    ("MONDO_0003158", "malignant myoepithelioma"),  # 137 genes, 3 known drugs
    ("MONDO_0003175", "salivary gland adenoid cystic carcinoma"),  # 456 genes, 2 known drugs
    ("MONDO_0003193", "bile duct adenocarcinoma"),  # 8896 genes, 4 known drugs
    ("MONDO_0003198", "small intestine adenocarcinoma"),  # 911 genes, 23 known drugs
    ("MONDO_0003199", "anal carcinoma"),  # 387 genes, 30 known drugs
    ("MONDO_0003210", "intrahepatic cholangiocarcinoma"),  # 2881 genes, 86 known drugs
    ("MONDO_0003219", "gastroesophageal junction adenocarcinoma"),  # 893 genes, 179 known drugs
    ("MONDO_0003220", "gallbladder carcinoma"),  # 1250 genes, 42 known drugs
    ("MONDO_0003233", "essential tremor"),  # 621 genes, 34 known drugs
    ("MONDO_0003265", "adjustment disorder"),  # 50 genes, 2 known drugs
    ("MONDO_0003268", "mixed glioma"),  # 385 genes, 6 known drugs
    ("MONDO_0003308", "pleural mesothelioma"),  # 1247 genes, 28 known drugs
    ("MONDO_0003334", "demyelinating polyneuropathy"),  # 602 genes, 1 known drugs
    ("MONDO_0003345", "hilar cholangiocarcinoma"),  # 311 genes, 14 known drugs
    ("MONDO_0003381", "pituitary gland disorder"),  # 4621 genes, 4 known drugs
    ("MONDO_0003406", "sleep-wake disorder"),  # 3891 genes, 10 known drugs
    ("MONDO_0003441", "dystonic disorder"),  # 3038 genes, 4 known drugs
    ("MONDO_0003473", "spinal cord ependymoma"),  # 54 genes, 1 known drugs
    ("MONDO_0003481", "dysgerminoma of ovary"),  # 52 genes, 1 known drugs
    ("MONDO_0003510", "malignant testicular germ cell tumor"),  # 509 genes, 7 known drugs
    ("MONDO_0003523", "gastrin-producing neuroendocrine tumor"),  # 148 genes, 1 known drugs
    ("MONDO_0003544", "spinal cord cancer"),  # 160 genes, 6 known drugs
    ("MONDO_0003572", "nasopharyngeal type undifferentiated carcinoma"),  # 117 genes, 5 known drugs
    ("MONDO_0003608", "optic atrophy"),  # 3035 genes, 3 known drugs
    ("MONDO_0003689", "familial hemolytic anemia"),  # 4136 genes, 1 known drugs
    ("MONDO_0003699", "phobic disorder"),  # 284 genes, 1 known drugs
    ("MONDO_0003709", "agoraphobia"),  # 72 genes, 2 known drugs
    ("MONDO_0003715", "bladder urachal carcinoma"),  # 99 genes, 7 known drugs
    ("MONDO_0003749", "esophageal disorder"),  # 13637 genes, 1 known drugs
    ("MONDO_0003757", "paraplegia"),  # 3357 genes, 1 known drugs
    ("MONDO_0003763", "acute stress disorder"),  # 64 genes, 5 known drugs
    ("MONDO_0003781", "bronchitis"),  # 612 genes, 35 known drugs
    ("MONDO_0003792", "ovarian carcinosarcoma"),  # 100 genes, 9 known drugs
    ("MONDO_0003795", "ovarian small cell carcinoma"),  # 101 genes, 2 known drugs
    ("MONDO_0003816", "articular cartilage disorder"),  # 721 genes, 3 known drugs
    ("MONDO_0003834", "gastric cardia carcinoma"),  # 430 genes, 3 known drugs
    ("MONDO_0003835", "gastric cardia adenocarcinoma"),  # 132 genes, 12 known drugs
    ("MONDO_0003847", "hereditary disease"),  # 20639 genes, 10 known drugs
    ("MONDO_0003865", "acral lentiginous melanoma"),  # 621 genes, 30 known drugs
    ("MONDO_0003869", "childhood brain stem glioma"),  # 472 genes, 2 known drugs
    ("MONDO_0003900", "connective tissue disorder"),  # 17273 genes, 2 known drugs
    ("MONDO_0003937", "spondylitis"),  # 1779 genes, 13 known drugs
    ("MONDO_0003960", "pulmonary large cell neuroendocrine carcinoma"),  # 539 genes, 9 known drugs
    ("MONDO_0004037", "retinal edema"),  # 792 genes, 2 known drugs
    ("MONDO_0004069", "inborn mitochondrial metabolism disorder"),  # 6818 genes, 1 known drugs
    ("MONDO_0004114", "urinary bladder small cell neuroendocrine carcinoma"),  # 481 genes, 9 known drugs
    ("MONDO_0004116", "esophageal small cell neuroendocrine carcinoma"),  # 54 genes, 8 known drugs
    ("MONDO_0004192", "urethra cancer"),  # 155 genes, 1 known drugs
    ("MONDO_0004235", "diverticulitis"),  # 211 genes, 4 known drugs
    ("MONDO_0004247", "peptic ulcer disease"),  # 1424 genes, 17 known drugs
    ("MONDO_0004251", "small intestine neoplasm"),  # 2606 genes, 4 known drugs
    ("MONDO_0004286", "pancreatic intraductal papillary-mucinous neoplasm"),  # 723 genes, 3 known drugs
    ("MONDO_0004298", "stomach disorder"),  # 14945 genes, 6 known drugs
    ("MONDO_0004323", "muscular atrophy"),  # 533 genes, 7 known drugs
    ("MONDO_0004335", "digestive system disorder"),  # 20900 genes, 4 known drugs
    ("MONDO_0004355", "childhood leukemia"),  # 269 genes, 40 known drugs
    ("MONDO_0004382", "laryngeal disorder"),  # 3275 genes, 1 known drugs
    ("MONDO_0004431", "hemarthrosis"),  # 58 genes, 5 known drugs
    ("MONDO_0004456", "cocaine abuse"),  # 190 genes, 28 known drugs
    ("MONDO_0004465", "periampullary adenocarcinoma"),  # 134 genes, 8 known drugs
    ("MONDO_0004471", "bacterial arthritis"),  # 336 genes, 9 known drugs
    ("MONDO_0004496", "myocarditis"),  # 1521 genes, 22 known drugs
    ("MONDO_0004508", "periapical periodontitis"),  # 535 genes, 36 known drugs
    ("MONDO_0004514", "chronic rhinitis"),  # 76 genes, 5 known drugs
    ("MONDO_0004522", "infectious peritonitis"),  # 156 genes, 4 known drugs
    ("MONDO_0004555", "kidney angiomyolipoma"),  # 138 genes, 4 known drugs
    ("MONDO_0004557", "congenital fibrosarcoma"),  # 95 genes, 4 known drugs
    ("MONDO_0004565", "intestinal obstruction"),  # 852 genes, 9 known drugs
    ("MONDO_0004567", "ileus"),  # 606 genes, 10 known drugs
    ("MONDO_0004580", "retinal degeneration"),  # 7925 genes, 1 known drugs
    ("MONDO_0004588", "night blindness"),  # 1383 genes, 2 known drugs
    ("MONDO_0004608", "oropharynx cancer"),  # 1019 genes, 28 known drugs
    ("MONDO_0004627", "duodenitis"),  # 291 genes, 1 known drugs
    ("MONDO_0004631", "tongue cancer"),  # 1397 genes, 7 known drugs
    ("MONDO_0004643", "myeloid leukemia"),  # 13779 genes, 48 known drugs
    ("MONDO_0004647", "in situ carcinoma"),  # 4178 genes, 17 known drugs
    ("MONDO_0004648", "vascular dementia"),  # 828 genes, 17 known drugs
    ("MONDO_0004652", "bacterial pneumonia"),  # 954 genes, 25 known drugs
    ("MONDO_0004653", "atypical chronic myeloid leukemia, BCR-ABL1 negative"),  # 57 genes, 5 known drugs
    ("MONDO_0004658", "breast carcinoma in situ"),  # 2981 genes, 3 known drugs
    ("MONDO_0004669", "salivary gland cancer"),  # 1157 genes, 40 known drugs
    ("MONDO_0004670", "lupus erythematosus"),  # 6099 genes, 15 known drugs
    ("MONDO_0004689", "inborn metal metabolism disorder"),  # 5697 genes, 2 known drugs
    ("MONDO_0004693", "squamous carcinoma in situ"),  # 249 genes, 3 known drugs
    ("MONDO_0004694", "hepatopulmonary syndrome"),  # 125 genes, 4 known drugs
    ("MONDO_0004703", "bladder carcinoma in situ"),  # 71 genes, 16 known drugs
    ("MONDO_0004728", "diabetic macular edema"),  # 293 genes, 89 known drugs
    ("MONDO_0004736", "inborn disorder of amino acid metabolism"),  # 7043 genes, 2 known drugs
    ("MONDO_0004739", "urea cycle disorder"),  # 2969 genes, 7 known drugs
    ("MONDO_0004741", "tyrosinemia"),  # 838 genes, 1 known drugs
    ("MONDO_0004743", "hyperhomocysteinemia"),  # 588 genes, 7 known drugs
    ("MONDO_0004784", "allergic asthma"),  # 1540 genes, 39 known drugs
    ("MONDO_0004789", "cholangitis"),  # 1960 genes, 4 known drugs
    ("MONDO_0004790", "fatty liver disease"),  # 6155 genes, 18 known drugs
    ("MONDO_0004796", "infectious meningitis"),  # 1580 genes, 9 known drugs
    ("MONDO_0004822", "bronchiectasis"),  # 1103 genes, 34 known drugs
    ("MONDO_0004842", "stomatitis"),  # 734 genes, 4 known drugs
    ("MONDO_0004844", "oral mucosa leukoplakia"),  # 167 genes, 4 known drugs
    ("MONDO_0004849", "pulmonary emphysema"),  # 1772 genes, 37 known drugs
    ("MONDO_0004855", "tenosynovitis"),  # 141 genes, 8 known drugs
    ("MONDO_0004857", "tendinitis"),  # 239 genes, 10 known drugs
    ("MONDO_0004868", "biliary tract disorder"),  # 11181 genes, 1 known drugs
    ("MONDO_0004880", "bowel dysfunction"),  # 385 genes, 6 known drugs
    ("MONDO_0004900", "peripheral vertigo"),  # 781 genes, 2 known drugs
    ("MONDO_0004933", "hypoplastic left heart syndrome"),  # 627 genes, 3 known drugs
    ("MONDO_0004938", "substance dependence"),  # 2715 genes, 4 known drugs
    ("MONDO_0004950", "gastric carcinoma"),  # 6700 genes, 46 known drugs
    ("MONDO_0004953", "invasive ductal breast carcinoma"),  # 4007 genes, 22 known drugs
    ("MONDO_0004956", "metastatic prostate carcinoma"),  # 1184 genes, 21 known drugs
    ("MONDO_0004957", "mucinous adenocarcinoma"),  # 1533 genes, 3 known drugs
    ("MONDO_0004958", "oral cavity squamous cell carcinoma"),  # 5047 genes, 69 known drugs
    ("MONDO_0004966", "gastritis"),  # 1839 genes, 14 known drugs
    ("MONDO_0004970", "adenocarcinoma"),  # 19385 genes, 92 known drugs
    ("MONDO_0004971", "adenoid cystic carcinoma"),  # 1050 genes, 61 known drugs
    ("MONDO_0004974", "adrenal gland pheochromocytoma"),  # 543 genes, 21 known drugs
    ("MONDO_0004982", "pancreatitis"),  # 3058 genes, 12 known drugs
    ("MONDO_0004983", "spermatogenic failure"),  # 1212 genes, 1 known drugs
    ("MONDO_0004986", "urinary bladder carcinoma"),  # 10776 genes, 160 known drugs
    ("MONDO_0004988", "breast adenocarcinoma"),  # 4380 genes, 29 known drugs
    ("MONDO_0004990", "breast tumor luminal A or B"),  # 473 genes, 6 known drugs
    ("MONDO_0004993", "carcinoma"),  # 21368 genes, 43 known drugs
    ("MONDO_0004994", "cardiomyopathy"),  # 10229 genes, 36 known drugs
    ("MONDO_0005001", "chronic gastritis"),  # 967 genes, 12 known drugs
    ("MONDO_0005003", "chronic pancreatitis"),  # 1554 genes, 34 known drugs
    ("MONDO_0005004", "clear cell adenocarcinoma"),  # 8721 genes, 13 known drugs
    ("MONDO_0005005", "clear cell renal carcinoma"),  # 9160 genes, 106 known drugs
    ("MONDO_0005006", "clear cell sarcoma of kidney"),  # 119 genes, 11 known drugs
    ("MONDO_0005008", "colorectal adenocarcinoma"),  # 10519 genes, 103 known drugs
    ("MONDO_0005012", "cutaneous melanoma"),  # 3614 genes, 81 known drugs
    ("MONDO_0005013", "dedifferentiated chondrosarcoma"),  # 60 genes, 10 known drugs
    ("MONDO_0005015", "diabetes mellitus"),  # 13837 genes, 266 known drugs
    ("MONDO_0005017", "diffuse gastric adenocarcinoma"),  # 731 genes, 5 known drugs
    ("MONDO_0005019", "diffuse scleroderma"),  # 100 genes, 6 known drugs
    ("MONDO_0005021", "dilated cardiomyopathy"),  # 6095 genes, 30 known drugs
    ("MONDO_0005023", "ductal breast carcinoma in situ"),  # 2781 genes, 40 known drugs
    ("MONDO_0005026", "endometrioid adenocarcinoma"),  # 1788 genes, 7 known drugs
    ("MONDO_0005028", "esophageal adenocarcinoma"),  # 3288 genes, 106 known drugs
    ("MONDO_0005029", "essential thrombocythemia"),  # 1215 genes, 33 known drugs
    ("MONDO_0005031", "fibromatosis"),  # 996 genes, 2 known drugs
    ("MONDO_0005034", "thyroid gland follicular carcinoma"),  # 1967 genes, 27 known drugs
    ("MONDO_0005035", "ganglioneuroblastoma"),  # 210 genes, 19 known drugs
    ("MONDO_0005036", "gastric adenocarcinoma"),  # 4794 genes, 237 known drugs
    ("MONDO_0005045", "hypertrophic cardiomyopathy"),  # 7200 genes, 29 known drugs
    ("MONDO_0005051", "invasive lobular breast carcinoma"),  # 436 genes, 9 known drugs
    ("MONDO_0005052", "irritable bowel syndrome"),  # 2050 genes, 114 known drugs
    ("MONDO_0005055", "Kaposi's sarcoma"),  # 1098 genes, 80 known drugs
    ("MONDO_0005057", "large cell neuroendocrine carcinoma"),  # 881 genes, 9 known drugs
    ("MONDO_0005058", "leiomyosarcoma"),  # 1118 genes, 82 known drugs
    ("MONDO_0005060", "liposarcoma"),  # 1479 genes, 45 known drugs
    ("MONDO_0005061", "lung adenocarcinoma"),  # 8760 genes, 97 known drugs
    ("MONDO_0005072", "neuroblastoma"),  # 6866 genes, 174 known drugs
    ("MONDO_0005075", "thyroid gland papillary carcinoma"),  # 12173 genes, 37 known drugs
    ("MONDO_0005076", "periodontitis"),  # 3187 genes, 86 known drugs
    ("MONDO_0005077", "pertussis"),  # 435 genes, 13 known drugs
    ("MONDO_0005080", "portal hypertension"),  # 1274 genes, 28 known drugs
    ("MONDO_0005081", "preeclampsia"),  # 4277 genes, 84 known drugs
    ("MONDO_0005082", "prostate adenocarcinoma"),  # 4483 genes, 91 known drugs
    ("MONDO_0005084", "mental disorder"),  # 16868 genes, 15 known drugs
    ("MONDO_0005085", "pterygium"),  # 1388 genes, 7 known drugs
    ("MONDO_0005086", "renal cell carcinoma"),  # 14421 genes, 346 known drugs
    ("MONDO_0005089", "sarcoma"),  # 14019 genes, 179 known drugs
    ("MONDO_0005091", "severe acute respiratory syndrome"),  # 1405 genes, 11 known drugs
    ("MONDO_0005095", "spondyloarthropathy"),  # 2096 genes, 7 known drugs
    ("MONDO_0005096", "squamous cell carcinoma"),  # 13090 genes, 100 known drugs
    ("MONDO_0005097", "squamous cell lung carcinoma"),  # 5572 genes, 81 known drugs
    ("MONDO_0005098", "stroke disorder"),  # 7684 genes, 93 known drugs
    ("MONDO_0005099", "subarachnoid hemorrhage"),  # 1176 genes, 57 known drugs
    ("MONDO_0005102", "undifferentiated (embryonal) sarcoma"),  # 177 genes, 20 known drugs
    ("MONDO_0005103", "well-differentiated liposarcoma"),  # 228 genes, 3 known drugs
    ("MONDO_0005106", "lipoma"),  # 712 genes, 6 known drugs
    ("MONDO_0005110", "idiopathic cardiomyopathy"),  # 768 genes, 1 known drugs
    ("MONDO_0005112", "malignant pleural mesothelioma"),  # 874 genes, 86 known drugs
    ("MONDO_0005129", "cataract"),  # 3540 genes, 50 known drugs
    ("MONDO_0005130", "celiac disease"),  # 1580 genes, 15 known drugs
    ("MONDO_0005131", "cervical carcinoma"),  # 8376 genes, 62 known drugs
    ("MONDO_0005138", "lung carcinoma"),  # 14357 genes, 4 known drugs
    ("MONDO_0005140", "ovarian carcinoma"),  # 15746 genes, 277 known drugs
    ("MONDO_0005146", "post-traumatic stress disorder"),  # 1945 genes, 106 known drugs
    ("MONDO_0005152", "hypopituitarism"),  # 2110 genes, 2 known drugs
    ("MONDO_0005153", "cervical adenocarcinoma"),  # 1360 genes, 11 known drugs
    ("MONDO_0005154", "liver disorder"),  # 17191 genes, 79 known drugs
    ("MONDO_0005155", "cirrhosis of liver"),  # 3436 genes, 100 known drugs
    ("MONDO_0005156", "encephalomyelitis"),  # 3807 genes, 5 known drugs
    ("MONDO_0005159", "prostate carcinoma"),  # 11298 genes, 46 known drugs
    ("MONDO_0005164", "fibrosarcoma"),  # 1837 genes, 14 known drugs
    ("MONDO_0005167", "fibroma"),  # 1390 genes, 2 known drugs
    ("MONDO_0005184", "pancreatic ductal adenocarcinoma"),  # 5062 genes, 241 known drugs
    ("MONDO_0005186", "cocaine dependence"),  # 564 genes, 105 known drugs
    ("MONDO_0005192", "exocrine pancreatic carcinoma"),  # 10899 genes, 254 known drugs
    ("MONDO_0005206", "renal carcinoma"),  # 14598 genes, 39 known drugs
    ("MONDO_0005210", "uterine corpus sarcoma"),  # 383 genes, 21 known drugs
    ("MONDO_0005211", "ovarian serous adenocarcinoma"),  # 13708 genes, 12 known drugs
    ("MONDO_0005212", "rhabdomyosarcoma"),  # 2166 genes, 95 known drugs
    ("MONDO_0005213", "uterine carcinoma"),  # 14194 genes, 3 known drugs
    ("MONDO_0005215", "vulvar carcinoma"),  # 405 genes, 4 known drugs
    ("MONDO_0005216", "hypopharyngeal carcinoma"),  # 504 genes, 9 known drugs
    ("MONDO_0005220", "collecting duct carcinoma"),  # 242 genes, 11 known drugs
    ("MONDO_0005221", "renal pelvis urothelial carcinoma"),  # 1237 genes, 3 known drugs
    ("MONDO_0005231", "hepatitis C virus infection"),  # 1664 genes, 185 known drugs
    ("MONDO_0005232", "large cell carcinoma"),  # 2263 genes, 1 known drugs
    ("MONDO_0005233", "non-small cell lung carcinoma"),  # 12475 genes, 1072 known drugs
    ("MONDO_0005235", "smoldering plasma cell myeloma"),  # 96 genes, 22 known drugs
    ("MONDO_0005238", "round cell liposarcoma"),  # 104 genes, 2 known drugs
    ("MONDO_0005244", "peripheral neuropathy"),  # 8096 genes, 86 known drugs
    ("MONDO_0005246", "osteomyelitis"),  # 1264 genes, 30 known drugs
    ("MONDO_0005249", "pneumonia"),  # 3689 genes, 198 known drugs
    ("MONDO_0005258", "autism spectrum disorder"),  # 5089 genes, 123 known drugs
    ("MONDO_0005260", "autism"),  # 4782 genes, 50 known drugs
    ("MONDO_0005264", "transient ischemic attack"),  # 854 genes, 26 known drugs
    ("MONDO_0005265", "inflammatory bowel disease"),  # 7629 genes, 103 known drugs
    ("MONDO_0005266", "diabetic retinopathy"),  # 2308 genes, 68 known drugs
    ("MONDO_0005275", "lung disorder"),  # 17194 genes, 25 known drugs
    ("MONDO_0005276", "dental caries"),  # 644 genes, 32 known drugs
    ("MONDO_0005278", "serous adenocarcinoma"),  # 13782 genes, 2 known drugs
    ("MONDO_0005282", "cutaneous lupus erythematosus"),  # 2125 genes, 31 known drugs
    ("MONDO_0005283", "retinal disorder"),  # 9613 genes, 6 known drugs
    ("MONDO_0005284", "chronic progressive multiple sclerosis"),  # 605 genes, 5 known drugs
    ("MONDO_0005288", "intestinal polyp"),  # 209 genes, 1 known drugs
    ("MONDO_0005291", "brain aneurysm"),  # 732 genes, 6 known drugs
    ("MONDO_0005292", "colitis"),  # 5376 genes, 16 known drugs
    ("MONDO_0005296", "sleep apnea syndrome"),  # 2624 genes, 21 known drugs
    ("MONDO_0005299", "brain ischemia"),  # 2962 genes, 10 known drugs
    ("MONDO_0005303", "drug dependence"),  # 2566 genes, 28 known drugs
    ("MONDO_0005304", "biliary tract neoplasm"),  # 9086 genes, 10 known drugs
    ("MONDO_0005312", "pouchitis"),  # 276 genes, 15 known drugs
    ("MONDO_0005313", "necrotizing enterocolitis"),  # 1233 genes, 23 known drugs
    ("MONDO_0005314", "relapsing-remitting multiple sclerosis"),  # 1261 genes, 24 known drugs
    ("MONDO_0005318", "canker sore"),  # 152 genes, 13 known drugs
    ("MONDO_0005319", "humerus fracture"),  # 84 genes, 2 known drugs
    ("MONDO_0005320", "tibia fracture"),  # 60 genes, 5 known drugs
    ("MONDO_0005321", "Fuchs' endothelial dystrophy"),  # 1158 genes, 1 known drugs
    ("MONDO_0005324", "seasonal allergic rhinitis"),  # 634 genes, 92 known drugs
    ("MONDO_0005327", "hip fracture"),  # 301 genes, 38 known drugs
    ("MONDO_0005335", "colorectal neoplasm"),  # 15718 genes, 26 known drugs
    ("MONDO_0005336", "myopathy"),  # 9950 genes, 10 known drugs
    ("MONDO_0005342", "IgA glomerulonephritis"),  # 2302 genes, 64 known drugs
    ("MONDO_0005344", "hepatitis B virus infection"),  # 2163 genes, 135 known drugs
    ("MONDO_0005345", "hypospadias"),  # 557 genes, 7 known drugs
    ("MONDO_0005346", "gallstones"),  # 688 genes, 2 known drugs
    ("MONDO_0005349", "otosclerosis"),  # 492 genes, 3 known drugs
    ("MONDO_0005351", "anorexia nervosa"),  # 818 genes, 39 known drugs
    ("MONDO_0005352", "conduct disorder"),  # 175 genes, 7 known drugs
    ("MONDO_0005354", "chronic hepatitis C virus infection"),  # 970 genes, 92 known drugs
    ("MONDO_0005357", "Creutzfeldt Jacob disease"),  # 1391 genes, 2 known drugs
    ("MONDO_0005359", "drug-induced liver injury"),  # 58 genes, 17 known drugs
    ("MONDO_0005361", "eosinophilic esophagitis"),  # 817 genes, 41 known drugs
    ("MONDO_0005365", "hearing loss disorder"),  # 4367 genes, 13 known drugs
    ("MONDO_0005366", "chronic hepatitis B virus infection"),  # 1136 genes, 82 known drugs
    ("MONDO_0005367", "heroin dependence"),  # 244 genes, 10 known drugs
    ("MONDO_0005371", "mood disorder"),  # 7613 genes, 52 known drugs
    ("MONDO_0005375", "nasopharyngeal neoplasm"),  # 5393 genes, 13 known drugs
    ("MONDO_0005379", "neurotic disorder"),  # 2109 genes, 1 known drugs
    ("MONDO_0005380", "osteonecrosis"),  # 2711 genes, 5 known drugs
    ("MONDO_0005381", "bone disorder"),  # 17384 genes, 18 known drugs
    ("MONDO_0005382", "bone Paget disease"),  # 1762 genes, 5 known drugs
    ("MONDO_0005383", "panic disorder"),  # 382 genes, 35 known drugs
    ("MONDO_0005384", "focal epilepsy"),  # 1766 genes, 19 known drugs
    ("MONDO_0005391", "restless legs syndrome"),  # 613 genes, 47 known drugs
    ("MONDO_0005392", "scoliosis"),  # 2063 genes, 9 known drugs
    ("MONDO_0005394", "brain infarction"),  # 1544 genes, 4 known drugs
    ("MONDO_0005395", "movement disorder"),  # 10018 genes, 15 known drugs
    ("MONDO_0005401", "colonic neoplasm"),  # 12174 genes, 3 known drugs
    ("MONDO_0005404", "myalgic encephalomeyelitis/chronic fatigue syndrome"),  # 1775 genes, 28 known drugs
    ("MONDO_0005406", "gestational diabetes"),  # 2937 genes, 29 known drugs
    ("MONDO_0005411", "gallbladder cancer"),  # 1862 genes, 66 known drugs
    ("MONDO_0005412", "duodenal ulcer"),  # 549 genes, 37 known drugs
    ("MONDO_0005416", "osteoarthritis, knee"),  # 1587 genes, 144 known drugs
    ("MONDO_0005417", "wet macular degeneration"),  # 573 genes, 56 known drugs
    ("MONDO_0005419", "methamphetamine dependence"),  # 144 genes, 30 known drugs
    ("MONDO_0005429", "prion disease"),  # 2436 genes, 1 known drugs
    ("MONDO_0005433", "alcohol withdrawal"),  # 183 genes, 22 known drugs
    ("MONDO_0005438", "metastatic malignant neoplasm in the lymph nodes"),  # 5567 genes, 7 known drugs
    ("MONDO_0005439", "familial hypercholesterolemia"),  # 3217 genes, 43 known drugs
    ("MONDO_0005440", "embryonal carcinoma"),  # 1378 genes, 4 known drugs
    ("MONDO_0005445", "visceral leishmaniasis"),  # 1329 genes, 12 known drugs
    ("MONDO_0005447", "testicular cancer"),  # 1339 genes, 27 known drugs
    ("MONDO_0005451", "eating disorder"),  # 1036 genes, 27 known drugs
    ("MONDO_0005452", "bulimia nervosa"),  # 187 genes, 17 known drugs
    ("MONDO_0005453", "congenital heart disease"),  # 4330 genes, 37 known drugs
    ("MONDO_0005454", "lung neuroendocrine neoplasm"),  # 4550 genes, 20 known drugs
    ("MONDO_0005460", "swine influenza"),  # 352 genes, 3 known drugs
    ("MONDO_0005461", "endometrium adenocarcinoma"),  # 1639 genes, 20 known drugs
    ("MONDO_0005462", "primitive neuroectodermal tumor"),  # 7690 genes, 35 known drugs
    ("MONDO_0005464", "rhegmatogenous retinal detachment"),  # 655 genes, 10 known drugs
    ("MONDO_0005466", "hypersomnia"),  # 165 genes, 8 known drugs
    ("MONDO_0005473", "temporomandibular joint disorder"),  # 336 genes, 17 known drugs
    ("MONDO_0005475", "migraine with aura"),  # 1181 genes, 11 known drugs
    ("MONDO_0005484", "colorectal adenoma"),  # 1859 genes, 1 known drugs
    ("MONDO_0005485", "psychotic disorder"),  # 7379 genes, 138 known drugs
    ("MONDO_0005487", "schizoaffective disorder"),  # 330 genes, 104 known drugs
    ("MONDO_0005491", "Chagas cardiomyopathy"),  # 107 genes, 4 known drugs
    ("MONDO_0005494", "triple-negative breast carcinoma"),  # 4741 genes, 322 known drugs
    ("MONDO_0005496", "bile duct carcinoma"),  # 8940 genes, 3 known drugs
    ("MONDO_0005512", "malignant peritoneal mesothelioma"),  # 161 genes, 16 known drugs
    ("MONDO_0005515", "oral cavity cancer"),  # 4366 genes, 21 known drugs
    ("MONDO_0005517", "pharynx cancer"),  # 5462 genes, 6 known drugs
    ("MONDO_0005520", "rickets"),  # 1828 genes, 8 known drugs
    ("MONDO_0005522", "small intestine carcinoma"),  # 1080 genes, 5 known drugs
    ("MONDO_0005526", "tetanus"),  # 493 genes, 8 known drugs
    ("MONDO_0005530", "opiate dependence"),  # 490 genes, 63 known drugs
    ("MONDO_0005532", "Crohn's colitis"),  # 139 genes, 14 known drugs
    ("MONDO_0005538", "proctitis"),  # 412 genes, 3 known drugs
    ("MONDO_0005546", "fibromyalgia"),  # 595 genes, 103 known drugs
    ("MONDO_0005549", "renal cell adenocarcinoma"),  # 11181 genes, 90 known drugs
    ("MONDO_0005554", "rheumatic disorder"),  # 12672 genes, 82 known drugs
    ("MONDO_0005559", "neurodegenerative disease"),  # 17338 genes, 15 known drugs
    ("MONDO_0005560", "brain disorder"),  # 18712 genes, 7 known drugs
    ("MONDO_0005563", "nut midline carcinoma"),  # 250 genes, 11 known drugs
    ("MONDO_0005566", "neonatal abstinence syndrome"),  # 308 genes, 9 known drugs
    ("MONDO_0005567", "substance withdrawal syndrome"),  # 521 genes, 3 known drugs
    ("MONDO_0005571", "polycythemia"),  # 2081 genes, 1 known drugs
    ("MONDO_0005574", "tauopathy"),  # 12733 genes, 1 known drugs
    ("MONDO_0005575", "colorectal cancer"),  # 16299 genes, 744 known drugs
    ("MONDO_0005578", "arthritic joint disease"),  # 10075 genes, 17 known drugs
    ("MONDO_0005579", "idiopathic generalized epilepsy"),  # 1401 genes, 3 known drugs
    ("MONDO_0005580", "esophageal squamous cell carcinoma"),  # 6474 genes, 144 known drugs
    ("MONDO_0005582", "binge eating disorder"),  # 120 genes, 21 known drugs
    ("MONDO_0005590", "breast ductal adenocarcinoma"),  # 3569 genes, 1 known drugs
    ("MONDO_0005593", "chronic periodontitis"),  # 1012 genes, 29 known drugs
    ("MONDO_0005595", "laryngeal squamous cell carcinoma"),  # 1421 genes, 26 known drugs
    ("MONDO_0005601", "ovarian mucinous adenocarcinoma"),  # 484 genes, 5 known drugs
    ("MONDO_0005607", "chronic bronchitis"),  # 438 genes, 45 known drugs
    ("MONDO_0005611", "bladder transitional cell carcinoma"),  # 4756 genes, 66 known drugs
    ("MONDO_0005617", "undifferentiated carcinoma"),  # 1678 genes, 3 known drugs
    ("MONDO_0005618", "anxiety disorder"),  # 3077 genes, 135 known drugs
    ("MONDO_0005620", "cerebral amyloid angiopathy"),  # 1211 genes, 3 known drugs
    ("MONDO_0005625", "cerebral malaria"),  # 589 genes, 6 known drugs
    ("MONDO_0005627", "head and neck cancer"),  # 12899 genes, 216 known drugs
    ("MONDO_0005628", "male breast carcinoma"),  # 127 genes, 1 known drugs
    ("MONDO_0005632", "acute chest syndrome"),  # 134 genes, 20 known drugs
    ("MONDO_0005636", "adenosarcoma"),  # 194 genes, 1 known drugs
    ("MONDO_0005649", "appendicitis"),  # 461 genes, 38 known drugs
    ("MONDO_0005665", "Bell's palsy"),  # 101 genes, 17 known drugs
    ("MONDO_0005674", "bone giant cell tumor"),  # 221 genes, 3 known drugs
    ("MONDO_0005689", "cannabis dependence"),  # 299 genes, 32 known drugs
    ("MONDO_0005696", "central nervous system tuberculosis"),  # 343 genes, 9 known drugs
    ("MONDO_0005709", "common cold"),  # 166 genes, 49 known drugs
    ("MONDO_0005711", "congenital diaphragmatic hernia"),  # 1235 genes, 2 known drugs
    ("MONDO_0005712", "congenital nystagmus"),  # 1441 genes, 1 known drugs
    ("MONDO_0005714", "congenital syphilis"),  # 522 genes, 5 known drugs
    ("MONDO_0005723", "Cryptococcal meningitis"),  # 144 genes, 15 known drugs
    ("MONDO_0005744", "yolk sac tumor"),  # 387 genes, 7 known drugs
    ("MONDO_0005749", "eosinophilic pneumonia"),  # 100 genes, 4 known drugs
    ("MONDO_0005766", "fungal lung infectious disease"),  # 984 genes, 5 known drugs
    ("MONDO_0005775", "G6PD deficiency"),  # 545 genes, 3 known drugs
    ("MONDO_0005789", "hepatitis D virus infection"),  # 175 genes, 21 known drugs
    ("MONDO_0005790", "hepatitis A virus infection"),  # 1915 genes, 3 known drugs
    ("MONDO_0005798", "HIV-associated nephropathy"),  # 157 genes, 2 known drugs
    ("MONDO_0005803", "hyperinsulinemic hypoglycemia"),  # 5107 genes, 9 known drugs
    ("MONDO_0005804", "hyperprolactinemia"),  # 545 genes, 14 known drugs
    ("MONDO_0005806", "hypopharynx cancer"),  # 683 genes, 15 known drugs
    ("MONDO_0005812", "influenza"),  # 2913 genes, 83 known drugs
    ("MONDO_0005814", "intestinal cancer"),  # 15619 genes, 2 known drugs
    ("MONDO_0005815", "pancreatic neuroendocrine neoplasm"),  # 2569 genes, 3 known drugs
    ("MONDO_0005824", "Legionnaires' disease"),  # 313 genes, 1 known drugs
    ("MONDO_0005854", "mixed connective tissue disease"),  # 813 genes, 3 known drugs
    ("MONDO_0005867", "Mycoplasma pneumoniae pneumonia"),  # 159 genes, 4 known drugs
    ("MONDO_0005872", "nervous system cancer"),  # 14149 genes, 1 known drugs
    ("MONDO_0005885", "optic neuritis"),  # 461 genes, 39 known drugs
    ("MONDO_0005886", "oral candidiasis"),  # 155 genes, 6 known drugs
    ("MONDO_0005893", "pancreatic endocrine carcinoma"),  # 163 genes, 5 known drugs
    ("MONDO_0005906", "peritonsillar abscess"),  # 62 genes, 15 known drugs
    ("MONDO_0005922", "pleural tuberculosis"),  # 162 genes, 1 known drugs
    ("MONDO_0005929", "postpartum depression"),  # 228 genes, 31 known drugs
    ("MONDO_0005937", "REM sleep behavior disorder"),  # 101 genes, 6 known drugs
    ("MONDO_0005960", "silicosis"),  # 672 genes, 3 known drugs
    ("MONDO_0005961", "sinusitis"),  # 1730 genes, 47 known drugs
    ("MONDO_0005965", "spinal stenosis"),  # 313 genes, 3 known drugs
    ("MONDO_0005972", "streptococcal pneumonia"),  # 145 genes, 2 known drugs
    ("MONDO_0006003", "uterine corpus cancer"),  # 11043 genes, 20 known drugs
    ("MONDO_0006012", "viral pneumonia"),  # 499 genes, 3 known drugs
    ("MONDO_0006031", "chronic rhinosinusitis"),  # 1938 genes, 60 known drugs
    ("MONDO_0006033", "diffuse intrinsic pontine glioma"),  # 470 genes, 80 known drugs
    ("MONDO_0006041", "lung carcinoid tumor"),  # 347 genes, 2 known drugs
    ("MONDO_0006042", "meningeal tuberculosis"),  # 676 genes, 22 known drugs
    ("MONDO_0006043", "metaplastic breast carcinoma"),  # 515 genes, 3 known drugs
    ("MONDO_0006047", "pancreatic adenocarcinoma"),  # 7332 genes, 266 known drugs
    ("MONDO_0006052", "pulmonary tuberculosis"),  # 922 genes, 78 known drugs
    ("MONDO_0006058", "Wilms tumor"),  # 1613 genes, 35 known drugs
    ("MONDO_0006074", "adenosquamous carcinoma"),  # 702 genes, 3 known drugs
    ("MONDO_0006082", "anal squamous cell carcinoma"),  # 238 genes, 31 known drugs
    ("MONDO_0006087", "appendix adenocarcinoma"),  # 173 genes, 9 known drugs
    ("MONDO_0006115", "blast phase chronic myelogenous leukemia, BCR-ABL1 positive"),  # 100 genes, 11 known drugs
    ("MONDO_0006130", "central nervous system neoplasm"),  # 13492 genes, 75 known drugs
    ("MONDO_0006134", "cervical adenosquamous carcinoma"),  # 66 genes, 5 known drugs
    ("MONDO_0006135", "cervical clear cell adenocarcinoma"),  # 50 genes, 1 known drugs
    ("MONDO_0006142", "cervical small cell carcinoma"),  # 211 genes, 3 known drugs
    ("MONDO_0006143", "cervical squamous cell carcinoma"),  # 3251 genes, 28 known drugs
    ("MONDO_0006173", "conjunctival squamous cell carcinoma"),  # 50 genes, 1 known drugs
    ("MONDO_0006181", "digestive system carcinoma"),  # 18497 genes, 17 known drugs
    ("MONDO_0006186", "duodenal adenocarcinoma"),  # 856 genes, 1 known drugs
    ("MONDO_0006189", "eccrine porocarcinoma"),  # 448 genes, 1 known drugs
    ("MONDO_0006191", "endometrial clear cell adenocarcinoma"),  # 164 genes, 5 known drugs
    ("MONDO_0006192", "endometrial endometrioid adenocarcinoma"),  # 970 genes, 5 known drugs
    ("MONDO_0006196", "endometrial serous adenocarcinoma"),  # 314 genes, 13 known drugs
    ("MONDO_0006206", "fallopian tube carcinoma"),  # 160 genes, 51 known drugs
    ("MONDO_0006210", "fibrolamellar hepatocellular carcinoma"),  # 243 genes, 22 known drugs
    ("MONDO_0006215", "gallbladder adenocarcinoma"),  # 810 genes, 6 known drugs
    ("MONDO_0006221", "gastric adenoma"),  # 580 genes, 1 known drugs
    ("MONDO_0006226", "gastric mucosa-associated lymphoid tissue lymphoma"),  # 123 genes, 14 known drugs
    ("MONDO_0006237", "granulocytic sarcoma"),  # 96 genes, 3 known drugs
    ("MONDO_0006244", "HER2 positive breast carcinoma"),  # 768 genes, 36 known drugs
    ("MONDO_0006248", "hydatidiform mole"),  # 516 genes, 3 known drugs
    ("MONDO_0006254", "intestinal type adenocarcinoma"),  # 821 genes, 7 known drugs
    ("MONDO_0006255", "intimal sarcoma"),  # 94 genes, 8 known drugs
    ("MONDO_0006256", "invasive breast carcinoma"),  # 4982 genes, 13 known drugs
    ("MONDO_0006260", "kidney medullary carcinoma"),  # 1596 genes, 15 known drugs
    ("MONDO_0006270", "lobular breast carcinoma in situ"),  # 149 genes, 1 known drugs
    ("MONDO_0006277", "lung lymphangioleiomyomatosis"),  # 297 genes, 1 known drugs
    ("MONDO_0006279", "lung sarcomatoid carcinoma"),  # 519 genes, 2 known drugs
    ("MONDO_0006282", "lymphangiosarcoma"),  # 65 genes, 1 known drugs
    ("MONDO_0006288", "malignant adrenal gland pheochromocytoma"),  # 117 genes, 1 known drugs
    ("MONDO_0006290", "malignant germ cell tumor"),  # 2656 genes, 19 known drugs
    ("MONDO_0006292", "malignant mesothelioma"),  # 1583 genes, 37 known drugs
    ("MONDO_0006294", "pleural cancer"),  # 886 genes, 2 known drugs
    ("MONDO_0006311", "myelodysplastic/myeloproliferative neoplasm"),  # 939 genes, 27 known drugs
    ("MONDO_0006314", "nasal cavity polyp"),  # 1181 genes, 17 known drugs
    ("MONDO_0006325", "ocular melanoma"),  # 6027 genes, 20 known drugs
    ("MONDO_0006329", "olfactory neuroblastoma"),  # 249 genes, 14 known drugs
    ("MONDO_0006335", "ovarian endometrioid adenocarcinoma"),  # 948 genes, 14 known drugs
    ("MONDO_0006345", "palmar fibromatosis"),  # 149 genes, 1 known drugs
    ("MONDO_0006346", "pancreatic acinar cell carcinoma"),  # 360 genes, 1 known drugs
    ("MONDO_0006360", "penile carcinoma"),  # 266 genes, 7 known drugs
    ("MONDO_0006373", "pituitary gland adenoma"),  # 2084 genes, 12 known drugs
    ("MONDO_0006382", "poorly differentiated thyroid gland carcinoma"),  # 308 genes, 38 known drugs
    ("MONDO_0006397", "renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions"),  # 234 genes, 3 known drugs
    ("MONDO_0006406", "sarcomatoid carcinoma"),  # 677 genes, 3 known drugs
    ("MONDO_0006407", "sarcomatoid mesothelioma"),  # 133 genes, 2 known drugs
    ("MONDO_0006411", "sinonasal undifferentiated carcinoma"),  # 114 genes, 6 known drugs
    ("MONDO_0006414", "skin sarcoma"),  # 157 genes, 1 known drugs
    ("MONDO_0006450", "therapy-related myeloid neoplasm"),  # 159 genes, 1 known drugs
    ("MONDO_0006451", "thymic carcinoma"),  # 620 genes, 49 known drugs
    ("MONDO_0006468", "thyroid gland undifferentiated (anaplastic) carcinoma"),  # 1288 genes, 69 known drugs
    ("MONDO_0006470", "tonsillar squamous cell carcinoma"),  # 124 genes, 1 known drugs
    ("MONDO_0006474", "transitional cell carcinoma"),  # 5225 genes, 47 known drugs
    ("MONDO_0006485", "uterine carcinosarcoma"),  # 6571 genes, 22 known drugs
    ("MONDO_0006486", "uveal melanoma"),  # 4944 genes, 84 known drugs
    ("MONDO_0006497", "cerebral palsy"),  # 888 genes, 58 known drugs
    ("MONDO_0006502", "acute respiratory distress syndrome"),  # 3744 genes, 184 known drugs
    ("MONDO_0006509", "papillary carcinoma"),  # 12085 genes, 3 known drugs
    ("MONDO_0006512", "estrogen-receptor positive breast cancer"),  # 293 genes, 35 known drugs
    ("MONDO_0006513", "estrogen-receptor negative breast cancer"),  # 4781 genes, 10 known drugs
    ("MONDO_0006515", "acute pancreatitis"),  # 1472 genes, 45 known drugs
    ("MONDO_0006517", "childhood malignant neoplasm"),  # 1242 genes, 21 known drugs
    ("MONDO_0006519", "rectal cancer"),  # 3901 genes, 141 known drugs
    ("MONDO_0006543", "epidermolysis bullosa dystrophica"),  # 1066 genes, 4 known drugs
    ("MONDO_0006574", "lipomatosis"),  # 1425 genes, 2 known drugs
    ("MONDO_0006591", "panniculitis"),  # 219 genes, 1 known drugs
    ("MONDO_0006611", "skin sarcoidosis"),  # 72 genes, 7 known drugs
    ("MONDO_0006625", "altitude sickness"),  # 65 genes, 1 known drugs
    ("MONDO_0006626", "diabetic neuropathy"),  # 1238 genes, 65 known drugs
    ("MONDO_0006629", "osteoarthritis, hip"),  # 887 genes, 10 known drugs
    ("MONDO_0006632", "osteoarthritis, hand"),  # 238 genes, 12 known drugs
    ("MONDO_0006639", "adrenal cortex carcinoma"),  # 5422 genes, 47 known drugs
    ("MONDO_0006644", "alcoholic liver cirrhosis"),  # 491 genes, 7 known drugs
    ("MONDO_0006649", "anterior ischemic optic neuropathy"),  # 113 genes, 6 known drugs
    ("MONDO_0006662", "aseptic meningitis"),  # 276 genes, 7 known drugs
    ("MONDO_0006663", "perinatal asphyxia"),  # 578 genes, 30 known drugs
    ("MONDO_0006664", "atrial septal defect"),  # 1683 genes, 1 known drugs
    ("MONDO_0006665", "chronic atrophic gastritis"),  # 661 genes, 2 known drugs
    ("MONDO_0006670", "bacterial meningitis"),  # 981 genes, 11 known drugs
    ("MONDO_0006684", "brain edema"),  # 460 genes, 8 known drugs
    ("MONDO_0006687", "burning mouth syndrome"),  # 210 genes, 31 known drugs
    ("MONDO_0006702", "chronic inflammatory demyelinating polyradiculoneuropathy"),  # 519 genes, 19 known drugs
    ("MONDO_0006709", "common bile duct neoplasm"),  # 600 genes, 1 known drugs
    ("MONDO_0006722", "dental fluorosis"),  # 216 genes, 2 known drugs
    ("MONDO_0006744", "endolymphatic hydrops"),  # 770 genes, 2 known drugs
    ("MONDO_0006745", "endometrioid stromal sarcoma"),  # 331 genes, 3 known drugs
    ("MONDO_0006763", "frozen shoulder"),  # 798 genes, 38 known drugs
    ("MONDO_0006769", "gastroparesis"),  # 236 genes, 44 known drugs
    ("MONDO_0006799", "hypothalamic neoplasm"),  # 2783 genes, 2 known drugs
    ("MONDO_0006802", "inappropriate ADH syndrome"),  # 91 genes, 2 known drugs
    ("MONDO_0006804", "inflammatory breast carcinoma"),  # 1017 genes, 45 known drugs
    ("MONDO_0006810", "intracranial hypertension"),  # 538 genes, 6 known drugs
    ("MONDO_0006816", "arthropathy"),  # 11323 genes, 8 known drugs
    ("MONDO_0006823", "Klinefelter syndrome"),  # 553 genes, 8 known drugs
    ("MONDO_0006837", "low tension glaucoma"),  # 181 genes, 6 known drugs
    ("MONDO_0006843", "macular holes"),  # 215 genes, 3 known drugs
    ("MONDO_0006851", "meconium aspiration syndrome"),  # 313 genes, 3 known drugs
    ("MONDO_0006853", "mesenchymal chondrosarcoma"),  # 120 genes, 1 known drugs
    ("MONDO_0006861", "myeloid sarcoma"),  # 4792 genes, 12 known drugs
    ("MONDO_0006862", "myofascial pain syndrome"),  # 76 genes, 13 known drugs
    ("MONDO_0006874", "obstructive jaundice"),  # 262 genes, 13 known drugs
    ("MONDO_0006879", "optic papillitis"),  # 102 genes, 1 known drugs
    ("MONDO_0006896", "peptic esophagitis"),  # 56 genes, 15 known drugs
    ("MONDO_0006913", "pneumococcal meningitis"),  # 244 genes, 2 known drugs
    ("MONDO_0006915", "polyradiculoneuropathy"),  # 527 genes, 1 known drugs
    ("MONDO_0006932", "pulmonary edema"),  # 771 genes, 8 known drugs
    ("MONDO_0006937", "pulpitis"),  # 544 genes, 13 known drugs
    ("MONDO_0006946", "renal osteodystrophy"),  # 199 genes, 4 known drugs
    ("MONDO_0006950", "retinal vasculitis"),  # 85 genes, 2 known drugs
    ("MONDO_0006951", "retinal vein occlusion"),  # 224 genes, 28 known drugs
    ("MONDO_0006952", "retinopathy of prematurity"),  # 2489 genes, 22 known drugs
    ("MONDO_0006966", "secondary Parkinson disease"),  # 489 genes, 2 known drugs
    ("MONDO_0006973", "skin appendage carcinoma"),  # 660 genes, 3 known drugs
    ("MONDO_0006975", "smooth muscle tumor"),  # 2723 genes, 2 known drugs
    ("MONDO_0007005", "ulcerative proctosigmoiditis"),  # 118 genes, 4 known drugs
    ("MONDO_0007027", "metabolic dysfunction-associated steatohepatitis"),  # 3741 genes, 138 known drugs
    ("MONDO_0007028", "rotator cuff syndrome"),  # 339 genes, 36 known drugs
    ("MONDO_0007039", "NF2-related schwannomatosis"),  # 1409 genes, 9 known drugs
    ("MONDO_0007068", "adenylosuccinate lyase deficiency"),  # 500 genes, 1 known drugs
    ("MONDO_0007070", "adiposis dolorosa"),  # 152 genes, 2 known drugs
    ("MONDO_0007078", "pseudohypoparathyroidism type 1A"),  # 666 genes, 2 known drugs
    ("MONDO_0007079", "alcohol dependence"),  # 1711 genes, 125 known drugs
    ("MONDO_0007100", "familial amyloid neuropathy"),  # 1057 genes, 15 known drugs
    ("MONDO_0007125", "ankyloglossia"),  # 135 genes, 3 known drugs
    ("MONDO_0007147", "obstructive sleep apnea syndrome"),  # 2268 genes, 114 known drugs
    ("MONDO_0007154", "arteriovenous malformations of the brain"),  # 295 genes, 3 known drugs
    ("MONDO_0007163", "episodic ataxia type 2"),  # 530 genes, 1 known drugs
    ("MONDO_0007182", "Machado-Joseph disease"),  # 876 genes, 1 known drugs
    ("MONDO_0007186", "gastroesophageal reflux disease"),  # 1453 genes, 95 known drugs
    ("MONDO_0007187", "nevoid basal cell carcinoma syndrome"),  # 1062 genes, 7 known drugs
    ("MONDO_0007203", "blue rubber bleb nevus"),  # 152 genes, 1 known drugs
    ("MONDO_0007239", "epidermolytic ichthyosis"),  # 433 genes, 2 known drugs
    ("MONDO_0007243", "Burkitt lymphoma"),  # 2155 genes, 58 known drugs
    ("MONDO_0007254", "breast cancer"),  # 17064 genes, 1036 known drugs
    ("MONDO_0007256", "hepatocellular carcinoma"),  # 15470 genes, 479 known drugs
    ("MONDO_0007275", "carpal tunnel syndrome"),  # 568 genes, 41 known drugs
    ("MONDO_0007293", "leukocyte adhesion deficiency 1"),  # 82 genes, 2 known drugs
    ("MONDO_0007309", "Charcot-Marie-Tooth disease type 1A"),  # 520 genes, 6 known drugs
    ("MONDO_0007318", "Alagille syndrome"),  # 1046 genes, 3 known drugs
    ("MONDO_0007342", "clubfoot"),  # 598 genes, 3 known drugs
    ("MONDO_0007345", "aorta coarctation"),  # 761 genes, 4 known drugs
    ("MONDO_0007414", "Gorham-Stout disease"),  # 683 genes, 1 known drugs
    ("MONDO_0007417", "Darier disease"),  # 394 genes, 3 known drugs
    ("MONDO_0007450", "neurohypophyseal diabetes insipidus"),  # 198 genes, 1 known drugs
    ("MONDO_0007488", "Lewy body dementia"),  # 1306 genes, 21 known drugs
    ("MONDO_0007523", "Ehlers-Danlos syndrome, hypermobility type"),  # 413 genes, 3 known drugs
    ("MONDO_0007540", "multiple endocrine neoplasia type 1"),  # 417 genes, 2 known drugs
    ("MONDO_0007571", "primary erythermalgia"),  # 144 genes, 2 known drugs
    ("MONDO_0007576", "esophageal cancer"),  # 12610 genes, 157 known drugs
    ("MONDO_0007608", "desmoid tumor"),  # 389 genes, 32 known drugs
    ("MONDO_0007650", "MALT lymphoma"),  # 1061 genes, 26 known drugs
    ("MONDO_0007652", "gastric mucosal hypertrophy"),  # 210 genes, 1 known drugs
    ("MONDO_0007661", "Tourette syndrome"),  # 561 genes, 40 known drugs
    ("MONDO_0007691", "Guillain-Barre syndrome, familial"),  # 178 genes, 6 known drugs
    ("MONDO_0007727", "TNF receptor 1-associated periodic fever syndrome"),  # 329 genes, 1 known drugs
    ("MONDO_0007743", "attention deficit-hyperactivity disorder"),  # 3337 genes, 135 known drugs
    ("MONDO_0007793", "hypochondroplasia"),  # 893 genes, 3 known drugs
    ("MONDO_0007803", "multiple system atrophy"),  # 1869 genes, 26 known drugs
    ("MONDO_0007827", "inclusion body myositis"),  # 1146 genes, 21 known drugs
    ("MONDO_0007864", "angioosteohypertrophic syndrome"),  # 368 genes, 1 known drugs
    ("MONDO_0007885", "Legg-Calve-Perthes disease"),  # 298 genes, 1 known drugs
    ("MONDO_0007886", "uterine corpus leiomyoma"),  # 1273 genes, 37 known drugs
    ("MONDO_0007888", "hereditary leiomyomatosis and renal cell cancer"),  # 566 genes, 6 known drugs
    ("MONDO_0007896", "acute monocytic leukemia"),  # 622 genes, 24 known drugs
    ("MONDO_0007899", "lichen sclerosus et atrophicus"),  # 176 genes, 22 known drugs
    ("MONDO_0007908", "multiple symmetric lipomatosis"),  # 481 genes, 1 known drugs
    ("MONDO_0007916", "primary intestinal lymphangiectasia"),  # 304 genes, 1 known drugs
    ("MONDO_0007925", "myelodysplastic syndrome associated with isolated del(5q)"),  # 274 genes, 1 known drugs
    ("MONDO_0007935", "cystoid macular edema"),  # 533 genes, 16 known drugs
    ("MONDO_0007959", "medulloblastoma"),  # 3856 genes, 98 known drugs
    ("MONDO_0007972", "Meniere disease"),  # 724 genes, 23 known drugs
    ("MONDO_0008039", "tropical spastic paraparesis"),  # 653 genes, 10 known drugs
    ("MONDO_0008040", "transient myeloproliferative syndrome"),  # 91 genes, 6 known drugs
    ("MONDO_0008054", "juvenile dermatomyositis"),  # 1762 genes, 19 known drugs
    ("MONDO_0008056", "myotonic dystrophy type 1"),  # 1069 genes, 12 known drugs
    ("MONDO_0008073", "familial juvenile hyperuricemic nephropathy type 1"),  # 755 genes, 1 known drugs
    ("MONDO_0008075", "schwannomatosis"),  # 674 genes, 2 known drugs
    ("MONDO_0008093", "nevus, epidermal"),  # 501 genes, 1 known drugs
    ("MONDO_0008094", "familial multiple nevi flammei"),  # 138 genes, 7 known drugs
    ("MONDO_0008114", "obsessive-compulsive disorder"),  # 663 genes, 72 known drugs
    ("MONDO_0008116", "oculopharyngeal muscular dystrophy"),  # 701 genes, 1 known drugs
    ("MONDO_0008119", "spinocerebellar ataxia type 1"),  # 892 genes, 3 known drugs
    ("MONDO_0008159", "postmenopausal osteoporosis"),  # 604 genes, 25 known drugs
    ("MONDO_0008170", "ovarian cancer"),  # 15776 genes, 568 known drugs
    ("MONDO_0008177", "extramammary Paget disease"),  # 528 genes, 4 known drugs
    ("MONDO_0008195", "paramyotonia congenita of Von Eulenburg"),  # 323 genes, 3 known drugs
    ("MONDO_0008207", "chondromalacia patellae"),  # 130 genes, 1 known drugs
    ("MONDO_0008218", "Hailey-Hailey disease"),  # 290 genes, 5 known drugs
    ("MONDO_0008222", "Andersen-Tawil syndrome"),  # 897 genes, 2 known drugs
    ("MONDO_0008223", "hypokalemic periodic paralysis"),  # 366 genes, 2 known drugs
    ("MONDO_0008224", "hyperkalemic periodic paralysis"),  # 414 genes, 1 known drugs
    ("MONDO_0008228", "pernicious anemia"),  # 343 genes, 1 known drugs
    ("MONDO_0008231", "Peyronie disease"),  # 287 genes, 8 known drugs
    ("MONDO_0008259", "familial spontaneous pneumothorax"),  # 143 genes, 2 known drugs
    ("MONDO_0008274", "polyostotic fibrous dysplasia"),  # 312 genes, 3 known drugs
    ("MONDO_0008280", "Peutz-Jeghers syndrome"),  # 541 genes, 1 known drugs
    ("MONDO_0008294", "acute intermittent porphyria"),  # 265 genes, 3 known drugs
    ("MONDO_0008297", "variegate porphyria"),  # 453 genes, 1 known drugs
    ("MONDO_0008303", "familial male-limited precocious puberty"),  # 608 genes, 2 known drugs
    ("MONDO_0008310", "Hutchinson-Gilford progeria syndrome"),  # 916 genes, 6 known drugs
    ("MONDO_0008315", "prostate cancer"),  # 10886 genes, 762 known drugs
    ("MONDO_0008318", "Proteus syndrome"),  # 698 genes, 1 known drugs
    ("MONDO_0008327", "exfoliation syndrome"),  # 1838 genes, 8 known drugs
    ("MONDO_0008364", "Raynaud disease"),  # 137 genes, 9 known drugs
    ("MONDO_0008375", "retinal detachment"),  # 1038 genes, 4 known drugs
    ("MONDO_0008380", "retinoblastoma"),  # 2706 genes, 23 known drugs
    ("MONDO_0008394", "Silver-Russell syndrome"),  # 700 genes, 1 known drugs
    ("MONDO_0008420", "seborrheic keratosis"),  # 294 genes, 2 known drugs
    ("MONDO_0008433", "small cell lung carcinoma"),  # 5083 genes, 368 known drugs
    ("MONDO_0008434", "Smith-Magenis syndrome"),  # 678 genes, 1 known drugs
    ("MONDO_0008457", "spinocerebellar ataxia type 6"),  # 702 genes, 1 known drugs
    ("MONDO_0008458", "spinocerebellar ataxia type 2"),  # 873 genes, 3 known drugs
    ("MONDO_0008475", "spondylolisthesis"),  # 602 genes, 1 known drugs
    ("MONDO_0008487", "polycystic ovary syndrome"),  # 3839 genes, 112 known drugs
    ("MONDO_0008491", "stiff-person syndrome"),  # 440 genes, 11 known drugs
    ("MONDO_0008501", "Sturge-Weber syndrome"),  # 945 genes, 3 known drugs
    ("MONDO_0008523", "Blau syndrome"),  # 1071 genes, 1 known drugs
    ("MONDO_0008538", "temporal arteritis"),  # 1269 genes, 29 known drugs
    ("MONDO_0008575", "nicotine dependence"),  # 848 genes, 78 known drugs
    ("MONDO_0008585", "HELLP syndrome"),  # 447 genes, 3 known drugs
    ("MONDO_0008599", "trigeminal neuralgia"),  # 490 genes, 27 known drugs
    ("MONDO_0008608", "Down syndrome"),  # 4332 genes, 20 known drugs
    ("MONDO_0008627", "ureter cancer"),  # 134 genes, 1 known drugs
    ("MONDO_0008633", "Muckle-Wells syndrome"),  # 466 genes, 3 known drugs
    ("MONDO_0008641", "retinal vasculopathy with cerebral leukoencephalopathy and systemic manifestations"),  # 468 genes, 1 known drugs
    ("MONDO_0008667", "von Hippel-Lindau disease"),  # 767 genes, 11 known drugs
    ("MONDO_0008678", "Williams syndrome"),  # 774 genes, 3 known drugs
    ("MONDO_0008685", "Wolff-Parkinson-White syndrome"),  # 274 genes, 2 known drugs
    ("MONDO_0008692", "abetalipoproteinemia"),  # 473 genes, 2 known drugs
    ("MONDO_0008721", "medium chain acyl-CoA dehydrogenase deficiency"),  # 470 genes, 3 known drugs
    ("MONDO_0008723", "very long chain acyl-CoA dehydrogenase deficiency"),  # 594 genes, 4 known drugs
    ("MONDO_0008728", "classic congenital adrenal hyperplasia due to 21-hydroxylase deficiency"),  # 354 genes, 7 known drugs
    ("MONDO_0008733", "familial glucocorticoid deficiency"),  # 634 genes, 1 known drugs
    ("MONDO_0008752", "Alexander disease"),  # 1097 genes, 2 known drugs
    ("MONDO_0008763", "Alstrom syndrome"),  # 856 genes, 1 known drugs
    ("MONDO_0008769", "neuronal ceroid lipofuscinosis 2"),  # 537 genes, 1 known drugs
    ("MONDO_0008783", "Tangier disease"),  # 971 genes, 3 known drugs
    ("MONDO_0008815", "argininosuccinic aciduria"),  # 428 genes, 2 known drugs
    ("MONDO_0008840", "ataxia telangiectasia"),  # 3491 genes, 5 known drugs
    ("MONDO_0008863", "sitosterolemia"),  # 1247 genes, 3 known drugs
    ("MONDO_0008867", "biliary atresia"),  # 814 genes, 19 known drugs
    ("MONDO_0008890", "progressive bulbar palsy"),  # 179 genes, 4 known drugs
    ("MONDO_0008892", "progressive familial intrahepatic cholestasis type 1"),  # 290 genes, 2 known drugs
    ("MONDO_0008903", "lung cancer"),  # 16017 genes, 263 known drugs
    ("MONDO_0008907", "PMM2-congenital disorder of glycosylation"),  # 449 genes, 1 known drugs
    ("MONDO_0008918", "carnitine-acylcarnitine translocase deficiency"),  # 616 genes, 1 known drugs
    ("MONDO_0008919", "systemic primary carnitine deficiency disease"),  # 381 genes, 1 known drugs
    ("MONDO_0008947", "bilateral striopallidodentate calcinosis"),  # 1266 genes, 1 known drugs
    ("MONDO_0008948", "cerebrotendinous xanthomatosis"),  # 1015 genes, 2 known drugs
    ("MONDO_0008963", "Chediak-Higashi syndrome"),  # 541 genes, 9 known drugs
    ("MONDO_0008977", "chondrosarcoma"),  # 1308 genes, 41 known drugs
    ("MONDO_0008978", "chordoma"),  # 954 genes, 28 known drugs
    ("MONDO_0008982", "central areolar choroidal dystrophy"),  # 1614 genes, 1 known drugs
    ("MONDO_0008988", "citrullinemia type I"),  # 701 genes, 1 known drugs
    ("MONDO_0009009", "hypoplasminogenemia"),  # 319 genes, 1 known drugs
    ("MONDO_0009044", "Crigler-Najjar syndrome"),  # 947 genes, 4 known drugs
    ("MONDO_0009047", "cryptorchidism"),  # 668 genes, 2 known drugs
    ("MONDO_0009067", "cystinuria"),  # 413 genes, 5 known drugs
    ("MONDO_0009123", "orthostatic hypotension 1"),  # 299 genes, 1 known drugs
    ("MONDO_0009172", "enterocolitis"),  # 1321 genes, 2 known drugs
    ("MONDO_0009179", "recessive dystrophic epidermolysis bullosa"),  # 758 genes, 16 known drugs
    ("MONDO_0009194", "immunodeficiency 32B"),  # 622 genes, 6 known drugs
    ("MONDO_0009211", "congenital factor VII deficiency"),  # 143 genes, 1 known drugs
    ("MONDO_0009212", "congenital factor X deficiency"),  # 102 genes, 1 known drugs
    ("MONDO_0009242", "brittle cornea syndrome"),  # 1552 genes, 1 known drugs
    ("MONDO_0009249", "hereditary fructose intolerance"),  # 369 genes, 1 known drugs
    ("MONDO_0009258", "classic galactosemia"),  # 782 genes, 2 known drugs
    ("MONDO_0009264", "gastroschisis"),  # 94 genes, 1 known drugs
    ("MONDO_0009267", "Gaucher disease type III"),  # 491 genes, 2 known drugs
    ("MONDO_0009287", "glycogen storage disease due to glucose-6-phosphatase deficiency type IA"),  # 551 genes, 9 known drugs
    ("MONDO_0009288", "glycogen storage disease Ib"),  # 710 genes, 1 known drugs
    ("MONDO_0009293", "glycogen storage disease V"),  # 455 genes, 3 known drugs
    ("MONDO_0009294", "glycogen storage disease VI"),  # 3348 genes, 3 known drugs
    ("MONDO_0009295", "glycogen storage disease VII"),  # 339 genes, 1 known drugs
    ("MONDO_0009319", "pantothenate kinase-associated neurodegeneration"),  # 956 genes, 2 known drugs
    ("MONDO_0009348", "classic Hodgkin lymphoma"),  # 1029 genes, 90 known drugs
    ("MONDO_0009352", "classic homocystinuria"),  # 507 genes, 2 known drugs
    ("MONDO_0009366", "normal pressure hydrocephalus"),  # 376 genes, 1 known drugs
    ("MONDO_0009376", "carbamoyl phosphate synthetase I deficiency disease"),  # 581 genes, 2 known drugs
    ("MONDO_0009377", "hyperammonemia due to N-acetylglutamate synthase deficiency"),  # 553 genes, 1 known drugs
    ("MONDO_0009387", "familial lipoprotein lipase deficiency"),  # 722 genes, 4 known drugs
    ("MONDO_0009411", "autoimmune polyendocrine syndrome type 1"),  # 485 genes, 1 known drugs
    ("MONDO_0009431", "hereditary hypophosphatemic rickets with hypercalciuria"),  # 677 genes, 1 known drugs
    ("MONDO_0009468", "pseudotumor cerebri"),  # 435 genes, 13 known drugs
    ("MONDO_0009478", "combined immunodeficiency due to DOCK8 deficiency"),  # 339 genes, 1 known drugs
    ("MONDO_0009499", "Krabbe disease"),  # 1321 genes, 5 known drugs
    ("MONDO_0009509", "Landau-Kleffner syndrome"),  # 425 genes, 2 known drugs
    ("MONDO_0009528", "chylomicron retention disease"),  # 543 genes, 2 known drugs
    ("MONDO_0009549", "severe early-childhood-onset retinal dystrophy"),  # 2162 genes, 1 known drugs
    ("MONDO_0009561", "alpha-mannosidosis"),  # 1232 genes, 1 known drugs
    ("MONDO_0009607", "methionine adenosyltransferase deficiency"),  # 151 genes, 1 known drugs
    ("MONDO_0009623", "Nijmegen breakage syndrome"),  # 839 genes, 1 known drugs
    ("MONDO_0009635", "microvillus inclusion disease"),  # 221 genes, 1 known drugs
    ("MONDO_0009643", "sulfite oxidase deficiency due to molybdenum cofactor deficiency type A"),  # 141 genes, 2 known drugs
    ("MONDO_0009650", "mucolipidosis type II"),  # 635 genes, 8 known drugs
    ("MONDO_0009655", "mucopolysaccharidosis type 3A"),  # 497 genes, 8 known drugs
    ("MONDO_0009659", "mucopolysaccharidosis type 4A"),  # 892 genes, 2 known drugs
    ("MONDO_0009661", "mucopolysaccharidosis type 6"),  # 1012 genes, 8 known drugs
    ("MONDO_0009662", "mucopolysaccharidosis type 7"),  # 740 genes, 1 known drugs
    ("MONDO_0009665", "biotinidase deficiency"),  # 308 genes, 1 known drugs
    ("MONDO_0009669", "spinal muscular atrophy, type 1"),  # 351 genes, 3 known drugs
    ("MONDO_0009676", "autosomal recessive limb-girdle muscular dystrophy type 2B"),  # 771 genes, 1 known drugs
    ("MONDO_0009691", "mycosis fungoides"),  # 1310 genes, 75 known drugs
    ("MONDO_0009692", "primary myelofibrosis"),  # 831 genes, 63 known drugs
    ("MONDO_0009693", "plasma cell myeloma"),  # 5305 genes, 554 known drugs
    ("MONDO_0009696", "juvenile myoclonic epilepsy"),  # 952 genes, 2 known drugs
    ("MONDO_0009697", "Lafora disease"),  # 857 genes, 1 known drugs
    ("MONDO_0009705", "carnitine palmitoyl transferase 1A deficiency"),  # 527 genes, 1 known drugs
    ("MONDO_0009710", "Thomsen and Becker disease"),  # 286 genes, 2 known drugs
    ("MONDO_0009726", "proteosome-associated autoinflammatory syndrome"),  # 1081 genes, 1 known drugs
    ("MONDO_0009735", "Netherton syndrome"),  # 863 genes, 7 known drugs
    ("MONDO_0009746", "hereditary sensory and autonomic neuropathy type 4"),  # 373 genes, 2 known drugs
    ("MONDO_0009757", "Niemann-Pick disease, type C1"),  # 385 genes, 4 known drugs
    ("MONDO_0009763", "obesity-hypoventilation syndrome"),  # 159 genes, 2 known drugs
    ("MONDO_0009807", "osteosarcoma"),  # 6856 genes, 142 known drugs
    ("MONDO_0009813", "chronic recurrent multifocal osteomyelitis"),  # 868 genes, 10 known drugs
    ("MONDO_0009820", "osteoporosis-pseudoglioma syndrome"),  # 918 genes, 2 known drugs
    ("MONDO_0009823", "primary hyperoxaluria type 1"),  # 474 genes, 5 known drugs
    ("MONDO_0009824", "primary hyperoxaluria type 2"),  # 372 genes, 1 known drugs
    ("MONDO_0009831", "malignant pancreatic neoplasm"),  # 10528 genes, 463 known drugs
    ("MONDO_0009833", "Shwachman-Diamond syndrome"),  # 779 genes, 1 known drugs
    ("MONDO_0009849", "hyperimmunoglobulinemia D with periodic fever"),  # 253 genes, 1 known drugs
    ("MONDO_0009877", "Laron syndrome"),  # 424 genes, 1 known drugs
    ("MONDO_0009889", "autosomal recessive polycystic kidney disease"),  # 1372 genes, 2 known drugs
    ("MONDO_0009891", "acquired polycythemia vera"),  # 1751 genes, 53 known drugs
    ("MONDO_0009897", "adult polyglucosan body disease"),  # 350 genes, 1 known drugs
    ("MONDO_0009902", "cutaneous porphyria"),  # 522 genes, 3 known drugs
    ("MONDO_0009904", "Gitelman syndrome"),  # 328 genes, 3 known drugs
    ("MONDO_0009925", "autosomal recessive inherited pseudoxanthoma elasticum"),  # 595 genes, 2 known drugs
    ("MONDO_0009945", "pyridoxine-dependent epilepsy"),  # 345 genes, 1 known drugs
    ("MONDO_0009949", "pyruvate carboxylase deficiency disease"),  # 615 genes, 1 known drugs
    ("MONDO_0009950", "pyruvate kinase deficiency of red cells"),  # 403 genes, 1 known drugs
    ("MONDO_0009953", "leukocyte adhesion deficiency type II"),  # 468 genes, 1 known drugs
    ("MONDO_0009971", "respiratory distress syndrome in premature infants"),  # 458 genes, 21 known drugs
    ("MONDO_0009974", "familial hemophagocytic lymphohistiocytosis type 1"),  # 359 genes, 8 known drugs
    ("MONDO_0009975", "reticulum cell sarcoma"),  # 249 genes, 14 known drugs
    ("MONDO_0009993", "embryonal rhabdomyosarcoma"),  # 645 genes, 11 known drugs
    ("MONDO_0009994", "alveolar rhabdomyosarcoma"),  # 798 genes, 22 known drugs
    ("MONDO_0010006", "Sandhoff disease"),  # 1117 genes, 12 known drugs
    ("MONDO_0010031", "Sjogren-Larsson syndrome"),  # 991 genes, 2 known drugs
    ("MONDO_0010035", "Smith-Lemli-Opitz syndrome"),  # 734 genes, 3 known drugs
    ("MONDO_0010079", "Canavan disease"),  # 677 genes, 1 known drugs
    ("MONDO_0010083", "succinic semialdehyde dehydrogenase deficiency"),  # 872 genes, 1 known drugs
    ("MONDO_0010122", "congenital thrombotic thrombocytopenic purpura"),  # 286 genes, 3 known drugs
    ("MONDO_0010150", "head and neck squamous cell carcinoma"),  # 8836 genes, 426 known drugs
    ("MONDO_0010159", "mismatch repair cancer syndrome 1"),  # 348 genes, 4 known drugs
    ("MONDO_0010161", "tyrosinemia type I"),  # 435 genes, 1 known drugs
    ("MONDO_0010184", "methylmalonic aciduria and homocystinuria type cblC"),  # 167 genes, 1 known drugs
    ("MONDO_0010196", "Werner syndrome"),  # 1315 genes, 2 known drugs
    ("MONDO_0010198", "Wernicke-Korsakoff syndrome"),  # 471 genes, 1 known drugs
    ("MONDO_0010247", "X-linked cerebral adrenoleukodystrophy"),  # 836 genes, 1 known drugs
    ("MONDO_0010269", "Coats disease"),  # 1738 genes, 3 known drugs
    ("MONDO_0010298", "Lesch-Nyhan syndrome"),  # 618 genes, 2 known drugs
    ("MONDO_0010311", "Becker muscular dystrophy"),  # 804 genes, 15 known drugs
    ("MONDO_0010315", "T-B+ severe combined immunodeficiency due to gamma chain deficiency"),  # 404 genes, 3 known drugs
    ("MONDO_0010354", "Allan-Herndon-Dudley syndrome"),  # 475 genes, 2 known drugs
    ("MONDO_0010382", "fragile X-associated tremor/ataxia syndrome"),  # 989 genes, 3 known drugs
    ("MONDO_0010434", "synovial sarcoma"),  # 2541 genes, 48 known drugs
    ("MONDO_0010518", "Wiskott-Aldrich syndrome"),  # 981 genes, 16 known drugs
    ("MONDO_0010543", "Barth syndrome"),  # 432 genes, 2 known drugs
    ("MONDO_0010557", "choroideremia"),  # 2080 genes, 4 known drugs
    ("MONDO_0010572", "occipital horn syndrome"),  # 668 genes, 2 known drugs
    ("MONDO_0010580", "immune dysregulation-polyendocrinopathy-enteropathy-X-linked syndrome"),  # 650 genes, 3 known drugs
    ("MONDO_0010585", "X-linked hypohidrotic ectodermal dysplasia"),  # 480 genes, 1 known drugs
    ("MONDO_0010604", "hemophilia B"),  # 260 genes, 25 known drugs
    ("MONDO_0010619", "X-linked dominant hypophosphatemic rickets"),  # 728 genes, 1 known drugs
    ("MONDO_0010622", "recessive X-linked ichthyosis"),  # 343 genes, 1 known drugs
    ("MONDO_0010626", "hyper-IgM syndrome type 1"),  # 528 genes, 3 known drugs
    ("MONDO_0010627", "X-linked lymphoproliferative syndrome"),  # 77 genes, 8 known drugs
    ("MONDO_0010645", "oculocerebrorenal syndrome"),  # 706 genes, 1 known drugs
    ("MONDO_0010651", "Menkes disease"),  # 2247 genes, 7 known drugs
    ("MONDO_0010683", "X-linked myotubular myopathy"),  # 272 genes, 1 known drugs
    ("MONDO_0010725", "X-linked retinoschisis"),  # 1414 genes, 3 known drugs
    ("MONDO_0010735", "Kennedy disease"),  # 502 genes, 5 known drugs
    ("MONDO_0010743", "thrombocytopenia 1"),  # 202 genes, 1 known drugs
    ("MONDO_0010785", "maternally-inherited diabetes and deafness"),  # 645 genes, 1 known drugs
    ("MONDO_0010787", "Kearns-Sayre syndrome"),  # 688 genes, 1 known drugs
    ("MONDO_0010788", "Leber hereditary optic neuropathy"),  # 1436 genes, 8 known drugs
    ("MONDO_0010790", "MERRF syndrome"),  # 393 genes, 1 known drugs
    ("MONDO_0010797", "Pearson syndrome"),  # 480 genes, 1 known drugs
    ("MONDO_0010826", "childhood absence epilepsy"),  # 403 genes, 6 known drugs
    ("MONDO_0010857", "semantic dementia"),  # 179 genes, 2 known drugs
    ("MONDO_0010911", "prolactin-producing pituitary gland adenoma"),  # 401 genes, 9 known drugs
    ("MONDO_0011012", "African iron overload"),  # 611 genes, 5 known drugs
    ("MONDO_0011013", "autosomal dominant hypocalcemia 1"),  # 207 genes, 1 known drugs
    ("MONDO_0011014", "pleuropulmonary blastoma"),  # 139 genes, 8 known drugs
    ("MONDO_0011057", "cerebrovascular disorder"),  # 9731 genes, 12 known drugs
    ("MONDO_0011156", "progressive familial intrahepatic cholestasis type 2"),  # 441 genes, 1 known drugs
    ("MONDO_0011184", "childhood apraxia of speech"),  # 270 genes, 3 known drugs
    ("MONDO_0011200", "torsion dystonia 7"),  # 193 genes, 1 known drugs
    ("MONDO_0011240", "megalencephaly-capillary malformation-polymicrogyria syndrome"),  # 653 genes, 1 known drugs
    ("MONDO_0011257", "MPI-congenital disorder of glycosylation"),  # 311 genes, 1 known drugs
    ("MONDO_0011266", "myotonic dystrophy type 2"),  # 742 genes, 1 known drugs
    ("MONDO_0011330", "spinocerebellar ataxia type 10"),  # 809 genes, 1 known drugs
    ("MONDO_0011377", "long QT syndrome 3"),  # 198 genes, 1 known drugs
    ("MONDO_0011385", "intervertebral disk degenerative disorder"),  # 1897 genes, 6 known drugs
    ("MONDO_0011393", "hypoalphalipoproteinemia, primary, 1"),  # 757 genes, 3 known drugs
    ("MONDO_0011399", "alpha thalassemia spectrum"),  # 851 genes, 1 known drugs
    ("MONDO_0011426", "aceruloplasminemia"),  # 1055 genes, 1 known drugs
    ("MONDO_0011429", "juvenile idiopathic arthritis"),  # 3274 genes, 52 known drugs
    ("MONDO_0011438", "acne"),  # 1593 genes, 135 known drugs
    ("MONDO_0011441", "complex regional pain syndrome type 1"),  # 61 genes, 2 known drugs
    ("MONDO_0011464", "spinocerebellar ataxia type 11"),  # 605 genes, 1 known drugs
    ("MONDO_0011479", "postural orthostatic tachycardia syndrome"),  # 231 genes, 38 known drugs
    ("MONDO_0011484", "catecholaminergic polymorphic ventricular tachycardia 1"),  # 288 genes, 1 known drugs
    ("MONDO_0011502", "Wolfram syndrome 2"),  # 182 genes, 4 known drugs
    ("MONDO_0011565", "metabolic syndrome X"),  # 181 genes, 2 known drugs
    ("MONDO_0011603", "GNE myopathy"),  # 466 genes, 3 known drugs
    ("MONDO_0011604", "spondylo-ocular syndrome"),  # 1059 genes, 1 known drugs
    ("MONDO_0011628", "propionic acidemia"),  # 451 genes, 4 known drugs
    ("MONDO_0011652", "Phelan-McDermid syndrome"),  # 579 genes, 6 known drugs
    ("MONDO_0011655", "alveolar soft part sarcoma"),  # 329 genes, 32 known drugs
    ("MONDO_0011669", "hypotonia-cystinuria syndrome"),  # 274 genes, 1 known drugs
    ("MONDO_0011717", "hyperinsulinism-hyperammonemia syndrome"),  # 605 genes, 1 known drugs
    ("MONDO_0011719", "gastrointestinal stromal tumor"),  # 2013 genes, 88 known drugs
    ("MONDO_0011724", "encephalopathy due to GLUT1 deficiency"),  # 826 genes, 1 known drugs
    ("MONDO_0011728", "benign essential blepharospasm"),  # 80 genes, 7 known drugs
    ("MONDO_0011758", "Hurler syndrome"),  # 765 genes, 7 known drugs
    ("MONDO_0011759", "Hurler-Scheie syndrome"),  # 728 genes, 2 known drugs
    ("MONDO_0011760", "Scheie syndrome"),  # 809 genes, 6 known drugs
    ("MONDO_0011776", "CINCA syndrome"),  # 373 genes, 3 known drugs
    ("MONDO_0011786", "allergic rhinitis"),  # 1922 genes, 127 known drugs
    ("MONDO_0011787", "autosomal recessive limb-girdle muscular dystrophy type 2I"),  # 583 genes, 1 known drugs
    ("MONDO_0011818", "isolated focal cortical dysplasia type II"),  # 484 genes, 2 known drugs
    ("MONDO_0011849", "psoriatic arthritis"),  # 1820 genes, 77 known drugs
    ("MONDO_0011871", "Niemann-Pick disease type B"),  # 729 genes, 2 known drugs
    ("MONDO_0011895", "idiopathic hypereosinophilic syndrome"),  # 680 genes, 4 known drugs
    ("MONDO_0011908", "juvenile myelomonocytic leukemia"),  # 405 genes, 46 known drugs
    ("MONDO_0011934", "dermatofibrosarcoma protuberans"),  # 310 genes, 3 known drugs
    ("MONDO_0011962", "endometrial cancer"),  # 12697 genes, 243 known drugs
    ("MONDO_0011972", "ovarian hyperstimulation syndrome"),  # 281 genes, 16 known drugs
    ("MONDO_0011996", "chronic myelogenous leukemia, BCR-ABL1 positive"),  # 4479 genes, 189 known drugs
    ("MONDO_0012000", "specific phobia"),  # 76 genes, 5 known drugs
    ("MONDO_0012004", "parathyroid gland carcinoma"),  # 640 genes, 4 known drugs
    ("MONDO_0012081", "15q11q13 microduplication syndrome"),  # 905 genes, 1 known drugs
    ("MONDO_0012084", "aromatic L-amino acid decarboxylase deficiency"),  # 430 genes, 1 known drugs
    ("MONDO_0012089", "ichthyosis prematurity syndrome"),  # 291 genes, 1 known drugs
    ("MONDO_0012110", "growth delay due to insulin-like growth factor type 1 deficiency"),  # 547 genes, 2 known drugs
    ("MONDO_0012126", "familial avascular necrosis of femoral head"),  # 643 genes, 2 known drugs
    ("MONDO_0012172", "mitochondrial trifunctional protein deficiency"),  # 519 genes, 3 known drugs
    ("MONDO_0012173", "long chain 3-hydroxyacyl-CoA dehydrogenase deficiency"),  # 689 genes, 2 known drugs
    ("MONDO_0012268", "AIDS"),  # 1570 genes, 109 known drugs
    ("MONDO_0012301", "mitochondrial DNA depletion syndrome, myopathic form"),  # 449 genes, 2 known drugs
    ("MONDO_0012335", "obesity due to pro-opiomelanocortin deficiency"),  # 527 genes, 1 known drugs
    ("MONDO_0012407", "pyridoxal phosphate-responsive seizures"),  # 199 genes, 1 known drugs
    ("MONDO_0012511", "preterm premature rupture of the membranes"),  # 389 genes, 24 known drugs
    ("MONDO_0012521", "herpes simplex encephalitis"),  # 341 genes, 2 known drugs
    ("MONDO_0012579", "autoimmune pulmonary alveolar proteinosis"),  # 662 genes, 4 known drugs
    ("MONDO_0012589", "Pitt-Hopkins syndrome"),  # 599 genes, 3 known drugs
    ("MONDO_0012672", "cholelithiasis"),  # 1513 genes, 9 known drugs
    ("MONDO_0012723", "Leber congenital amaurosis 10"),  # 51 genes, 2 known drugs
    ("MONDO_0012817", "Ewing sarcoma"),  # 1942 genes, 129 known drugs
    ("MONDO_0012819", "diabetic ketoacidosis"),  # 873 genes, 12 known drugs
    ("MONDO_0012825", "extraskeletal myxoid chondrosarcoma"),  # 293 genes, 11 known drugs
    ("MONDO_0012833", "Crouzon syndrome-acanthosis nigricans syndrome"),  # 1083 genes, 8 known drugs
    ("MONDO_0012858", "primary CD59 deficiency"),  # 70 genes, 1 known drugs
    ("MONDO_0012883", "acute promyelocytic leukemia"),  # 2080 genes, 35 known drugs
    ("MONDO_0013021", "sterile multifocal osteomyelitis with periostitis and pustulosis"),  # 459 genes, 1 known drugs
    ("MONDO_0013098", "noise induced hearing loss"),  # 294 genes, 1 known drugs
    ("MONDO_0013144", "hereditary antithrombin deficiency"),  # 85 genes, 1 known drugs
    ("MONDO_0013189", "trichotillomania"),  # 144 genes, 10 known drugs
    ("MONDO_0013209", "metabolic dysfunction-associated steatotic liver disease"),  # 5677 genes, 156 known drugs
    ("MONDO_0013227", "congenital plasminogen activator inhibitor type 1 deficiency"),  # 128 genes, 1 known drugs
    ("MONDO_0013280", "myxoid liposarcoma"),  # 291 genes, 24 known drugs
    ("MONDO_0013327", "primary hyperoxaluria type 3"),  # 355 genes, 1 known drugs
    ("MONDO_0013452", "multisystemic smooth muscle dysfunction syndrome"),  # 620 genes, 1 known drugs
    ("MONDO_0013600", "insomnia"),  # 2536 genes, 121 known drugs
    ("MONDO_0013662", "Barrett esophagus"),  # 2491 genes, 20 known drugs
    ("MONDO_0013792", "intracerebral hemorrhage"),  # 1093 genes, 67 known drugs
    ("MONDO_0013892", "C3 glomerulonephritis"),  # 427 genes, 2 known drugs
    ("MONDO_0013991", "obesity due to congenital leptin deficiency"),  # 523 genes, 1 known drugs
    ("MONDO_0013999", "retinal dystrophy, optic nerve edema, splenomegaly, anhidrosis, and migraine headache syndrome"),  # 262 genes, 1 known drugs
    ("MONDO_0014005", "immunoglobulin-mediated membranoproliferative glomerulonephritis"),  # 556 genes, 2 known drugs
    ("MONDO_0014072", "D,L-2-hydroxyglutaric aciduria"),  # 181 genes, 1 known drugs
    ("MONDO_0014226", "idiopathic CD4 lymphocytopenia"),  # 338 genes, 2 known drugs
    ("MONDO_0014379", "ADNP-related multiple congenital anomalies - intellectual disability - autism spectrum disorder"),  # 466 genes, 1 known drugs
    ("MONDO_0014405", "STING-associated vasculopathy with onset in infancy"),  # 293 genes, 1 known drugs
    ("MONDO_0014633", "epilepsy with myoclonic atonic seizures"),  # 903 genes, 1 known drugs
    ("MONDO_0014960", "encephalopathy, progressive, early-onset, with brain edema and/or leukoencephalopathy"),  # 1253 genes, 6 known drugs
    ("MONDO_0015075", "thyroid gland carcinoma"),  # 12651 genes, 63 known drugs
    ("MONDO_0015104", "porphyria cutanea tarda"),  # 827 genes, 4 known drugs
    ("MONDO_0015131", "combined immunodeficiency"),  # 3775 genes, 3 known drugs
    ("MONDO_0015175", "autoimmune pancreatitis"),  # 748 genes, 8 known drugs
    ("MONDO_0015183", "short bowel syndrome"),  # 125 genes, 22 known drugs
    ("MONDO_0015229", "Bardet-Biedl syndrome"),  # 2786 genes, 2 known drugs
    ("MONDO_0015231", "Bartter syndrome"),  # 666 genes, 1 known drugs
    ("MONDO_0015243", "allergic bronchopulmonary aspergillosis"),  # 481 genes, 13 known drugs
    ("MONDO_0015247", "opsoclonus-myoclonus syndrome"),  # 495 genes, 5 known drugs
    ("MONDO_0015253", "Diamond-Blackfan anemia"),  # 1138 genes, 23 known drugs
    ("MONDO_0015263", "Brugada syndrome"),  # 564 genes, 3 known drugs
    ("MONDO_0015264", "cryptogenic organizing pneumonia"),  # 365 genes, 1 known drugs
    ("MONDO_0015265", "bronchiolitis obliterans syndrome"),  # 1055 genes, 31 known drugs
    ("MONDO_0015274", "chronic beryllium disease"),  # 377 genes, 3 known drugs
    ("MONDO_0015277", "medullary thyroid gland carcinoma"),  # 1420 genes, 52 known drugs
    ("MONDO_0015286", "congenital disorder of glycosylation"),  # 5132 genes, 2 known drugs
    ("MONDO_0015339", "adrenomyeloneuropathy"),  # 359 genes, 9 known drugs
    ("MONDO_0015447", "differentiated thyroid carcinoma"),  # 11588 genes, 72 known drugs
    ("MONDO_0015459", "nasopharyngeal carcinoma"),  # 4940 genes, 145 known drugs
    ("MONDO_0015469", "craniosynostosis"),  # 3985 genes, 4 known drugs
    ("MONDO_0015474", "cryptosporidiosis"),  # 190 genes, 8 known drugs
    ("MONDO_0015484", "cysticercosis"),  # 775 genes, 3 known drugs
    ("MONDO_0015486", "keratoconus"),  # 2700 genes, 16 known drugs
    ("MONDO_0015515", "carnitine palmitoyltransferase II deficiency"),  # 1051 genes, 4 known drugs
    ("MONDO_0015517", "common variable immunodeficiency"),  # 1805 genes, 11 known drugs
    ("MONDO_0015523", "epithelioid hemangioendothelioma"),  # 159 genes, 5 known drugs
    ("MONDO_0015564", "Castleman disease"),  # 554 genes, 11 known drugs
    ("MONDO_0015574", "chronic cutaneous lupus erythematosus"),  # 554 genes, 2 known drugs
    ("MONDO_0015597", "palmoplantar pustulosis"),  # 182 genes, 17 known drugs
    ("MONDO_0015612", "Dent disease"),  # 1111 genes, 2 known drugs
    ("MONDO_0015643", "photosensitive epilepsy"),  # 112 genes, 10 known drugs
    ("MONDO_0015650", "epilepsy syndrome"),  # 5417 genes, 4 known drugs
    ("MONDO_0015667", "acute myeloid leukemia by FAB classification"),  # 5564 genes, 169 known drugs
    ("MONDO_0015686", "primary peritoneal carcinoma"),  # 512 genes, 252 known drugs
    ("MONDO_0015691", "hypereosinophilic syndrome"),  # 1155 genes, 11 known drugs
    ("MONDO_0015742", "periventricular leukomalacia"),  # 425 genes, 3 known drugs
    ("MONDO_0015758", "primary cutaneous T-cell lymphoma"),  # 1669 genes, 1 known drugs
    ("MONDO_0015762", "progressive familial intrahepatic cholestasis"),  # 1843 genes, 3 known drugs
    ("MONDO_0015780", "dyskeratosis congenita"),  # 1760 genes, 10 known drugs
    ("MONDO_0015796", "acute lung injury"),  # 1130 genes, 63 known drugs
    ("MONDO_0015867", "vaginal carcinoma"),  # 62 genes, 6 known drugs
    ("MONDO_0015914", "primary orthostatic hypotension"),  # 508 genes, 8 known drugs
    ("MONDO_0015925", "interstitial lung disease"),  # 6821 genes, 49 known drugs
    ("MONDO_0015926", "pneumoconiosis"),  # 1396 genes, 1 known drugs
    ("MONDO_0015947", "inherited ichthyosis"),  # 3342 genes, 2 known drugs
    ("MONDO_0015967", "monogenic diabetes"),  # 2485 genes, 3 known drugs
    ("MONDO_0015974", "severe combined immunodeficiency"),  # 2470 genes, 21 known drugs
    ("MONDO_0015977", "agammaglobulinemia"),  # 2444 genes, 5 known drugs
    ("MONDO_0015991", "citrullinemia"),  # 2291 genes, 1 known drugs
    ("MONDO_0015993", "cone-rod dystrophy"),  # 2515 genes, 1 known drugs
    ("MONDO_0016002", "Ehlers-Danlos syndrome, kyphoscoliotic type 1"),  # 487 genes, 1 known drugs
    ("MONDO_0016009", "fetal trimethadione syndrome"),  # 585 genes, 1 known drugs
    ("MONDO_0016028", "erythromelalgia"),  # 170 genes, 4 known drugs
    ("MONDO_0016033", "Cornelia de Lange syndrome"),  # 1278 genes, 1 known drugs
    ("MONDO_0016063", "Cowden disease"),  # 3293 genes, 1 known drugs
    ("MONDO_0016064", "cleft palate"),  # 1667 genes, 6 known drugs
    ("MONDO_0016107", "myotonic dystrophy"),  # 1788 genes, 2 known drugs
    ("MONDO_0016112", "hereditary inclusion-body myopathy"),  # 1125 genes, 2 known drugs
    ("MONDO_0016113", "bulbospinal muscular atrophy"),  # 1020 genes, 2 known drugs
    ("MONDO_0016129", "eosinophilic gastroenteritis"),  # 172 genes, 6 known drugs
    ("MONDO_0016145", "neuromuscular disease caused by qualitative or quantitative defects of dysferlin"),  # 787 genes, 1 known drugs
    ("MONDO_0016147", "neuromuscular disease caused by qualitative or quantitative defects of dystrophin"),  # 616 genes, 2 known drugs
    ("MONDO_0016158", "narcolepsy-cataplexy syndrome"),  # 545 genes, 16 known drugs
    ("MONDO_0016163", "spinocerebellar ataxia 7"),  # 826 genes, 1 known drugs
    ("MONDO_0016167", "optic pathway glioma"),  # 305 genes, 12 known drugs
    ("MONDO_0016168", "cryopyrin-associated periodic syndrome"),  # 939 genes, 8 known drugs
    ("MONDO_0016218", "Guillain-Barre syndrome"),  # 817 genes, 7 known drugs
    ("MONDO_0016238", "solitary fibrous tumor"),  # 380 genes, 12 known drugs
    ("MONDO_0016241", "alternating hemiplegia of childhood"),  # 1194 genes, 3 known drugs
    ("MONDO_0016244", "atypical hemolytic-uremic syndrome"),  # 922 genes, 8 known drugs
    ("MONDO_0016262", "leiomyosarcoma of the corpus uteri"),  # 1014 genes, 21 known drugs
    ("MONDO_0016264", "autoimmune hepatitis"),  # 1505 genes, 32 known drugs
    ("MONDO_0016295", "neuronal ceroid lipofuscinosis"),  # 1960 genes, 1 known drugs
    ("MONDO_0016318", "progressive multifocal leukoencephalopathy"),  # 762 genes, 19 known drugs
    ("MONDO_0016349", "congenital hydrocephalus"),  # 1185 genes, 1 known drugs
    ("MONDO_0016358", "limited cutaneous systemic sclerosis"),  # 147 genes, 2 known drugs
    ("MONDO_0016367", "dermatomyositis"),  # 2130 genes, 48 known drugs
    ("MONDO_0016383", "nephrogenic diabetes insipidus"),  # 294 genes, 4 known drugs
    ("MONDO_0016391", "neonatal diabetes mellitus"),  # 1838 genes, 1 known drugs
    ("MONDO_0016466", "asbestosis"),  # 705 genes, 2 known drugs
    ("MONDO_0016471", "pachyonychia congenita"),  # 4851 genes, 5 known drugs
    ("MONDO_0016486", "beta-thalassemia major"),  # 398 genes, 27 known drugs
    ("MONDO_0016487", "beta-thalassemia intermedia"),  # 471 genes, 11 known drugs
    ("MONDO_0016512", "Kabuki syndrome"),  # 855 genes, 1 known drugs
    ("MONDO_0016537", "lymphoproliferative syndrome"),  # 1765 genes, 22 known drugs
    ("MONDO_0016575", "primary ciliary dyskinesia"),  # 2690 genes, 3 known drugs
    ("MONDO_0016587", "arrhythmogenic right ventricular cardiomyopathy"),  # 1510 genes, 1 known drugs
    ("MONDO_0016642", "meningioma"),  # 2598 genes, 45 known drugs
    ("MONDO_0016680", "high grade astrocytic tumor"),  # 10315 genes, 7 known drugs
    ("MONDO_0016681", "gliosarcoma"),  # 402 genes, 65 known drugs
    ("MONDO_0016683", "gliomatosis cerebri"),  # 225 genes, 2 known drugs
    ("MONDO_0016684", "anaplastic astrocytoma"),  # 1093 genes, 63 known drugs
    ("MONDO_0016685", "low-grade astrocytoma"),  # 1066 genes, 6 known drugs
    ("MONDO_0016686", "diffuse astrocytoma"),  # 339 genes, 4 known drugs
    ("MONDO_0016690", "pleomorphic xanthoastrocytoma"),  # 150 genes, 6 known drugs
    ("MONDO_0016691", "pilocytic astrocytoma"),  # 646 genes, 2 known drugs
    ("MONDO_0016692", "pilomyxoid astrocytoma"),  # 92 genes, 6 known drugs
    ("MONDO_0016693", "subependymal giant cell astrocytoma"),  # 102 genes, 1 known drugs
    ("MONDO_0016695", "oligodendroglioma"),  # 2621 genes, 29 known drugs
    ("MONDO_0016696", "anaplastic oligodendroglioma"),  # 518 genes, 30 known drugs
    ("MONDO_0016698", "ependymoma"),  # 2626 genes, 72 known drugs
    ("MONDO_0016700", "anaplastic ependymoma"),  # 212 genes, 2 known drugs
    ("MONDO_0016702", "oligoastrocytoma"),  # 376 genes, 16 known drugs
    ("MONDO_0016703", "anaplastic oligoastrocytoma"),  # 130 genes, 11 known drugs
    ("MONDO_0016717", "choroid plexus neoplasm"),  # 487 genes, 10 known drugs
    ("MONDO_0016718", "choroid plexus carcinoma"),  # 411 genes, 13 known drugs
    ("MONDO_0016722", "pineoblastoma"),  # 257 genes, 8 known drugs
    ("MONDO_0016729", "mixed neuronal-glial tumor"),  # 1944 genes, 1 known drugs
    ("MONDO_0016743", "tumor of meninges"),  # 2861 genes, 3 known drugs
    ("MONDO_0016748", "hemangioblastoma"),  # 785 genes, 5 known drugs
    ("MONDO_0016755", "neurofibroma"),  # 794 genes, 2 known drugs
    ("MONDO_0016820", "Moyamoya disease"),  # 1025 genes, 9 known drugs
    ("MONDO_0016971", "limb-girdle muscular dystrophy"),  # 2038 genes, 4 known drugs
    ("MONDO_0016982", "angiosarcoma"),  # 2291 genes, 38 known drugs
    ("MONDO_0017014", "interstitial lung disease specific to childhood"),  # 2345 genes, 1 known drugs
    ("MONDO_0017015", "primary interstitial lung disease specific to childhood"),  # 1377 genes, 1 known drugs
    ("MONDO_0017148", "heritable pulmonary arterial hypertension"),  # 1314 genes, 1 known drugs
    ("MONDO_0017160", "behavioral variant of frontotemporal dementia"),  # 772 genes, 2 known drugs
    ("MONDO_0017182", "familial hyperinsulinism"),  # 5010 genes, 5 known drugs
    ("MONDO_0017198", "osteopetrosis"),  # 3106 genes, 9 known drugs
    ("MONDO_0017265", "autosomal recessive congenital ichthyosis"),  # 1235 genes, 3 known drugs
    ("MONDO_0017276", "frontotemporal dementia"),  # 3113 genes, 20 known drugs
    ("MONDO_0017290", "familial intrahepatic cholestasis"),  # 1892 genes, 1 known drugs
    ("MONDO_0017314", "Ehlers-Danlos syndrome, vascular type"),  # 754 genes, 1 known drugs
    ("MONDO_0017364", "POEMS syndrome"),  # 424 genes, 13 known drugs
    ("MONDO_0017366", "hereditary pheochromocytoma-paraganglioma"),  # 2151 genes, 2 known drugs
    ("MONDO_0017373", "poliomyelitis"),  # 431 genes, 6 known drugs
    ("MONDO_0017376", "reactive arthritis"),  # 431 genes, 8 known drugs
    ("MONDO_0017386", "pleomorphic rhabdomyosarcoma"),  # 76 genes, 2 known drugs
    ("MONDO_0017387", "epithelioid sarcoma"),  # 274 genes, 10 known drugs
    ("MONDO_0017416", "postpoliomyelitis syndrome"),  # 208 genes, 6 known drugs
    ("MONDO_0017570", "leukocyte adhesion deficiency"),  # 1224 genes, 4 known drugs
    ("MONDO_0017572", "tick-borne encephalitis"),  # 700 genes, 4 known drugs
    ("MONDO_0017575", "mitochondrial neurogastrointestinal encephalomyopathy"),  # 942 genes, 2 known drugs
    ("MONDO_0017582", "pituitary adenocarcinoma"),  # 704 genes, 1 known drugs
    ("MONDO_0017590", "carcinoma of the ampulla of vater"),  # 588 genes, 12 known drugs
    ("MONDO_0017596", "diffuse large B-cell lymphoma of the central nervous system"),  # 135 genes, 12 known drugs
    ("MONDO_0017610", "epidermolysis bullosa simplex"),  # 1699 genes, 9 known drugs
    ("MONDO_0017611", "pituitary tumor"),  # 2779 genes, 9 known drugs
    ("MONDO_0017612", "junctional epidermolysis bullosa"),  # 1190 genes, 4 known drugs
    ("MONDO_0017623", "PTEN hamartoma tumor syndrome"),  # 1264 genes, 2 known drugs
    ("MONDO_0017708", "mevalonate kinase deficiency"),  # 914 genes, 1 known drugs
    ("MONDO_0017720", "GM2 gangliosidosis"),  # 1386 genes, 4 known drugs
    ("MONDO_0017767", "rheumatic fever"),  # 444 genes, 6 known drugs
    ("MONDO_0017778", "lamellar ichthyosis"),  # 701 genes, 5 known drugs
    ("MONDO_0017795", "ameloblastoma"),  # 562 genes, 3 known drugs
    ("MONDO_0017816", "primary systemic amyloidosis"),  # 183 genes, 21 known drugs
    ("MONDO_0017827", "malignant peripheral nerve sheath tumor"),  # 945 genes, 39 known drugs
    ("MONDO_0017844", "Sezary syndrome"),  # 854 genes, 50 known drugs
    ("MONDO_0017853", "hypersensitivity pneumonitis"),  # 617 genes, 3 known drugs
    ("MONDO_0017884", "papillary renal cell carcinoma"),  # 5262 genes, 26 known drugs
    ("MONDO_0017885", "chromophobe renal cell carcinoma"),  # 2431 genes, 5 known drugs
    ("MONDO_0017886", "MIT family translocation renal cell carcinoma"),  # 58 genes, 2 known drugs
    ("MONDO_0017979", "autoimmune lymphoproliferative syndrome"),  # 1330 genes, 5 known drugs
    ("MONDO_0017987", "syringomyelia"),  # 85 genes, 2 known drugs
    ("MONDO_0017990", "catecholaminergic polymorphic ventricular tachycardia"),  # 784 genes, 6 known drugs
    ("MONDO_0017991", "Takayasu arteritis"),  # 740 genes, 19 known drugs
    ("MONDO_0018010", "juvenile idiopathic inflammatory myopathy"),  # 492 genes, 3 known drugs
    ("MONDO_0018037", "hyper-IgE syndrome"),  # 1528 genes, 1 known drugs
    ("MONDO_0018059", "meningococcal meningitis"),  # 361 genes, 1 known drugs
    ("MONDO_0018075", "neural tube defect"),  # 1909 genes, 1 known drugs
    ("MONDO_0018078", "soft tissue sarcoma"),  # 6159 genes, 234 known drugs
    ("MONDO_0018088", "familial Mediterranean fever"),  # 768 genes, 7 known drugs
    ("MONDO_0018097", "infantile spasms"),  # 1155 genes, 18 known drugs
    ("MONDO_0018105", "Wolfram syndrome"),  # 706 genes, 5 known drugs
    ("MONDO_0018149", "GM1 gangliosidosis"),  # 1067 genes, 15 known drugs
    ("MONDO_0018155", "lateral sclerosis"),  # 268 genes, 6 known drugs
    ("MONDO_0018158", "mitochondrial DNA depletion syndrome"),  # 3278 genes, 1 known drugs
    ("MONDO_0018166", "oral submucous fibrosis"),  # 578 genes, 6 known drugs
    ("MONDO_0018171", "malignant germ cell tumor of ovary"),  # 157 genes, 2 known drugs
    ("MONDO_0018172", "malignant sex cord stromal tumor of ovary"),  # 116 genes, 5 known drugs
    ("MONDO_0018177", "glioblastoma"),  # 11192 genes, 456 known drugs
    ("MONDO_0018199", "new-onset refractory status epilepticus"),  # 396 genes, 1 known drugs
    ("MONDO_0018213", "hereditary sensory and autonomic neuropathy type 1"),  # 1003 genes, 1 known drugs
    ("MONDO_0018215", "paraneoplastic neurologic syndrome"),  # 1522 genes, 2 known drugs
    ("MONDO_0018271", "peripheral primitive neuroectodermal tumor"),  # 185 genes, 13 known drugs
    ("MONDO_0018301", "interstitial cystitis"),  # 514 genes, 49 known drugs
    ("MONDO_0018304", "Schnitzler syndrome"),  # 225 genes, 5 known drugs
    ("MONDO_0018305", "chronic granulomatous disease"),  # 1129 genes, 26 known drugs
    ("MONDO_0018307", "neurodegeneration with brain iron accumulation"),  # 2198 genes, 1 known drugs
    ("MONDO_0018309", "Hirschsprung disease"),  # 1117 genes, 2 known drugs
    ("MONDO_0018328", "homozygous familial hypercholesterolemia"),  # 1612 genes, 10 known drugs
    ("MONDO_0018352", "squamous cell carcinoma of penis"),  # 223 genes, 25 known drugs
    ("MONDO_0018353", "refractory celiac disease"),  # 217 genes, 1 known drugs
    ("MONDO_0018364", "malignant epithelial tumor of ovary"),  # 15612 genes, 232 known drugs
    ("MONDO_0018373", "avascular necrosis"),  # 2039 genes, 2 known drugs
    ("MONDO_0018456", "polyarticular juvenile idiopathic arthritis"),  # 828 genes, 7 known drugs
    ("MONDO_0018469", "pulmonary non-tuberculous mycobacterial infection"),  # 146 genes, 6 known drugs
    ("MONDO_0018473", "hyperlipoproteinemia type 3"),  # 582 genes, 4 known drugs
    ("MONDO_0018479", "congenital adrenal hyperplasia"),  # 1329 genes, 16 known drugs
    ("MONDO_0018510", "small intestine neuroendocrine neoplasm"),  # 410 genes, 2 known drugs
    ("MONDO_0018515", "squamous cell carcinoma of rectum"),  # 244 genes, 10 known drugs
    ("MONDO_0018531", "carcinoma of liver and intrahepatic biliary tract"),  # 16240 genes, 3 known drugs
    ("MONDO_0018540", "PFAPA syndrome"),  # 147 genes, 2 known drugs
    ("MONDO_0018542", "severe congenital neutropenia"),  # 2274 genes, 2 known drugs
    ("MONDO_0018543", "autosomal dominant hypocalcemia"),  # 577 genes, 4 known drugs
    ("MONDO_0018555", "hypogonadotropic hypogonadism"),  # 4699 genes, 23 known drugs
    ("MONDO_0018570", "hypophosphatasia"),  # 1184 genes, 11 known drugs
    ("MONDO_0018637", "familial chylomicronemia syndrome"),  # 1462 genes, 5 known drugs
    ("MONDO_0018646", "sclerosing cholangitis"),  # 2008 genes, 48 known drugs
    ("MONDO_0018648", "Keratocystic odontogenic tumor"),  # 235 genes, 1 known drugs
    ("MONDO_0018666", "hepatoblastoma"),  # 1280 genes, 34 known drugs
    ("MONDO_0018667", "pleural empyema"),  # 157 genes, 3 known drugs
    ("MONDO_0018696", "corticobasal syndrome"),  # 429 genes, 3 known drugs
    ("MONDO_0018744", "oligodendroglial tumor"),  # 1623 genes, 2 known drugs
    ("MONDO_0018752", "exercise-induced malignant hyperthermia"),  # 118 genes, 1 known drugs
    ("MONDO_0018768", "familial cold autoinflammatory syndrome"),  # 237 genes, 3 known drugs
    ("MONDO_0018800", "Kallmann syndrome"),  # 1880 genes, 2 known drugs
    ("MONDO_0018815", "aneurysmal bone cyst"),  # 887 genes, 1 known drugs
    ("MONDO_0018852", "achromatopsia"),  # 2263 genes, 3 known drugs
    ("MONDO_0018866", "Aicardi-Goutieres syndrome"),  # 1260 genes, 8 known drugs
    ("MONDO_0018871", "acute myelomonocytic leukemia M4"),  # 370 genes, 1 known drugs
    ("MONDO_0018872", "acute megakaryoblastic leukemia"),  # 383 genes, 1 known drugs
    ("MONDO_0018874", "acute myeloid leukemia"),  # 13654 genes, 592 known drugs
    ("MONDO_0018902", "hepatocellular adenoma"),  # 530 genes, 1 known drugs
    ("MONDO_0018907", "craniopharyngioma"),  # 742 genes, 7 known drugs
    ("MONDO_0018910", "oculocutaneous albinism"),  # 2503 genes, 3 known drugs
    ("MONDO_0018911", "maturity-onset diabetes of the young"),  # 1422 genes, 1 known drugs
    ("MONDO_0018919", "McCune-Albright syndrome"),  # 568 genes, 3 known drugs
    ("MONDO_0018920", "peripartum cardiomyopathy"),  # 533 genes, 13 known drugs
    ("MONDO_0018923", "22q11.2 deletion syndrome"),  # 1605 genes, 6 known drugs
    ("MONDO_0018937", "mucopolysaccharidosis type 3"),  # 1015 genes, 11 known drugs
    ("MONDO_0018938", "mucopolysaccharidosis type 4"),  # 1184 genes, 1 known drugs
    ("MONDO_0018940", "congenital myasthenic syndrome"),  # 1234 genes, 5 known drugs
    ("MONDO_0018947", "centronuclear myopathy"),  # 931 genes, 2 known drugs
    ("MONDO_0018994", "Charcot-Marie-Tooth disease type X"),  # 911 genes, 1 known drugs
    ("MONDO_0019004", "kidney Wilms tumor"),  # 297 genes, 3 known drugs
    ("MONDO_0019010", "congenital isolated hyperinsulinism"),  # 4977 genes, 7 known drugs
    ("MONDO_0019011", "Charcot-Marie-Tooth disease type 1"),  # 1127 genes, 1 known drugs
    ("MONDO_0019018", "Tako-tsubo cardiomyopathy"),  # 907 genes, 7 known drugs
    ("MONDO_0019024", "mast cell sarcoma"),  # 253 genes, 1 known drugs
    ("MONDO_0019037", "progressive supranuclear palsy"),  # 2083 genes, 22 known drugs
    ("MONDO_0019052", "inborn errors of metabolism"),  # 13339 genes, 22 known drugs
    ("MONDO_0019053", "peroxisomal disease"),  # 3891 genes, 4 known drugs
    ("MONDO_0019056", "neuromuscular disease"),  # 12363 genes, 3 known drugs
    ("MONDO_0019060", "bone neoplasm"),  # 14856 genes, 10 known drugs
    ("MONDO_0019064", "hereditary spastic paraplegia"),  # 3330 genes, 2 known drugs
    ("MONDO_0019072", "intrahepatic cholestasis"),  # 2274 genes, 12 known drugs
    ("MONDO_0019079", "proximal spinal muscular atrophy"),  # 1971 genes, 13 known drugs
    ("MONDO_0019086", "carcinoma of esophagus"),  # 6967 genes, 40 known drugs
    ("MONDO_0019087", "cholangiocarcinoma"),  # 8782 genes, 145 known drugs
    ("MONDO_0019091", "bronchopulmonary dysplasia"),  # 1923 genes, 49 known drugs
    ("MONDO_0019100", "neuromyelitis optica"),  # 783 genes, 50 known drugs
    ("MONDO_0019111", "familial thrombocytosis"),  # 534 genes, 4 known drugs
    ("MONDO_0019121", "pneumocystosis"),  # 892 genes, 33 known drugs
    ("MONDO_0019125", "relapsing polychondritis"),  # 387 genes, 8 known drugs
    ("MONDO_0019127", "polymyositis"),  # 1736 genes, 28 known drugs
    ("MONDO_0019149", "cholesteryl ester storage disease"),  # 919 genes, 1 known drugs
    ("MONDO_0019165", "central precocious puberty"),  # 441 genes, 6 known drugs
    ("MONDO_0019168", "pyomyositis"),  # 116 genes, 2 known drugs
    ("MONDO_0019169", "pyruvate dehydrogenase deficiency"),  # 1518 genes, 4 known drugs
    ("MONDO_0019171", "familial long QT syndrome"),  # 2490 genes, 10 known drugs
    ("MONDO_0019180", "hereditary hemorrhagic telangiectasia"),  # 836 genes, 22 known drugs
    ("MONDO_0019182", "inherited obesity"),  # 8734 genes, 1 known drugs
    ("MONDO_0019188", "Rubinstein-Taybi syndrome"),  # 919 genes, 1 known drugs
    ("MONDO_0019202", "myxofibrosarcoma"),  # 309 genes, 9 known drugs
    ("MONDO_0019209", "Japanese encephalitis"),  # 583 genes, 2 known drugs
    ("MONDO_0019212", "disseminated superficial actinic porokeratosis"),  # 166 genes, 1 known drugs
    ("MONDO_0019218", "inborn disorder of bile acid synthesis"),  # 1925 genes, 2 known drugs
    ("MONDO_0019234", "peroxisome biogenesis disorder"),  # 2349 genes, 2 known drugs
    ("MONDO_0019249", "mucopolysaccharidosis"),  # 2606 genes, 9 known drugs
    ("MONDO_0019255", "sphingolipidosis"),  # 4270 genes, 1 known drugs
    ("MONDO_0019262", "juvenile neuronal ceroid lipofuscinosis"),  # 1454 genes, 1 known drugs
    ("MONDO_0019266", "SAPHO syndrome"),  # 198 genes, 1 known drugs
    ("MONDO_0019276", "inherited epidermolysis bullosa"),  # 3822 genes, 1 known drugs
    ("MONDO_0019306", "congenital non-bullous ichthyosiform erythroderma"),  # 771 genes, 3 known drugs
    ("MONDO_0019312", "Hermansky-Pudlak syndrome"),  # 2355 genes, 10 known drugs
    ("MONDO_0019313", "lymphatic malformation"),  # 3464 genes, 7 known drugs
    ("MONDO_0019338", "sarcoidosis"),  # 3073 genes, 45 known drugs
    ("MONDO_0019340", "scleroderma"),  # 3296 genes, 23 known drugs
    ("MONDO_0019345", "shigellosis"),  # 470 genes, 7 known drugs
    ("MONDO_0019346", "sialidosis type 1"),  # 647 genes, 1 known drugs
    ("MONDO_0019350", "hereditary spherocytosis"),  # 664 genes, 1 known drugs
    ("MONDO_0019355", "adult-onset Still disease"),  # 542 genes, 14 known drugs
    ("MONDO_0019369", "complex regional pain syndrome"),  # 647 genes, 30 known drugs
    ("MONDO_0019373", "desmoplastic small round cell tumor"),  # 278 genes, 41 known drugs
    ("MONDO_0019391", "Fanconi anemia"),  # 2688 genes, 28 known drugs
    ("MONDO_0019403", "congenital dyserythropoietic anemia"),  # 1533 genes, 1 known drugs
    ("MONDO_0019409", "idiopathic juvenile osteoporosis"),  # 458 genes, 4 known drugs
    ("MONDO_0019434", "systemic-onset juvenile idiopathic arthritis"),  # 1801 genes, 11 known drugs
    ("MONDO_0019436", "psoriasis-related juvenile idiopathic arthritis"),  # 379 genes, 12 known drugs
    ("MONDO_0019437", "enthesitis-related juvenile idiopathic arthritis"),  # 941 genes, 6 known drugs
    ("MONDO_0019438", "AL amyloidosis"),  # 3562 genes, 27 known drugs
    ("MONDO_0019439", "AA amyloidosis"),  # 316 genes, 1 known drugs
    ("MONDO_0019451", "chronic neutrophilic leukemia"),  # 154 genes, 5 known drugs
    ("MONDO_0019452", "myeloproliferative neoplasm, unclassifiable"),  # 72 genes, 1 known drugs
    ("MONDO_0019457", "therapy related acute myeloid leukemia and myelodysplastic syndrome"),  # 75 genes, 13 known drugs
    ("MONDO_0019460", "acute leukemia of ambiguous lineage"),  # 309 genes, 31 known drugs
    ("MONDO_0019467", "CD4+/CD56+ hematodermic neoplasm"),  # 234 genes, 18 known drugs
    ("MONDO_0019499", "Turner syndrome"),  # 828 genes, 13 known drugs
    ("MONDO_0019514", "hepatic veno-occlusive disease"),  # 735 genes, 9 known drugs
    ("MONDO_0019542", "acute liver failure"),  # 1018 genes, 9 known drugs
    ("MONDO_0019558", "discoid lupus erythematosus"),  # 471 genes, 20 known drugs
    ("MONDO_0019562", "localized scleroderma"),  # 413 genes, 6 known drugs
    ("MONDO_0019600", "xeroderma pigmentosum"),  # 1642 genes, 1 known drugs
    ("MONDO_0019609", "Zellweger spectrum disorders"),  # 2131 genes, 1 known drugs
    ("MONDO_0019610", "Zollinger-Ellison syndrome"),  # 227 genes, 15 known drugs
    ("MONDO_0019612", "functioning gonadotropic adenoma"),  # 465 genes, 1 known drugs
    ("MONDO_0019613", "non-functioning pituitary adenoma"),  # 449 genes, 3 known drugs
    ("MONDO_0019640", "posterior urethral valve"),  # 720 genes, 2 known drugs
    ("MONDO_0019735", "polymyalgia rheumatica"),  # 220 genes, 22 known drugs
    ("MONDO_0019751", "autoinflammatory syndrome"),  # 5461 genes, 1 known drugs
    ("MONDO_0019771", "oromandibular dystonia"),  # 162 genes, 2 known drugs
    ("MONDO_0019773", "myelomeningocele"),  # 144 genes, 2 known drugs
    ("MONDO_0019781", "astrocytoma (excluding glioblastoma)"),  # 5506 genes, 48 known drugs
    ("MONDO_0019787", "autoimmune enteropathy"),  # 706 genes, 2 known drugs
    ("MONDO_0019806", "primary progressive aphasia"),  # 647 genes, 4 known drugs
    ("MONDO_0019933", "acromegaly"),  # 755 genes, 25 known drugs
    ("MONDO_0019938", "anorectal malformation"),  # 92 genes, 1 known drugs
    ("MONDO_0019952", "congenital myopathy"),  # 4344 genes, 1 known drugs
    ("MONDO_0019954", "pancreatic neuroendocrine tumor"),  # 2516 genes, 53 known drugs
    ("MONDO_0019963", "bronchial endocrine tumor"),  # 290 genes, 4 known drugs
    ("MONDO_0019992", "pseudohypoparathyroidism"),  # 1283 genes, 1 known drugs
    ("MONDO_0020072", "childhood-onset epilepsy syndrome"),  # 2253 genes, 1 known drugs
    ("MONDO_0020076", "myeloproliferative neoplasm"),  # 13997 genes, 63 known drugs
    ("MONDO_0020088", "familial partial lipodystrophy"),  # 1899 genes, 6 known drugs
    ("MONDO_0020121", "muscular dystrophy"),  # 8781 genes, 22 known drugs
    ("MONDO_0020122", "acquired idiopathic inflammatory myopathy"),  # 1813 genes, 3 known drugs
    ("MONDO_0020124", "neuromuscular junction disease"),  # 1234 genes, 1 known drugs
    ("MONDO_0020128", "motor neuron disorder"),  # 7201 genes, 17 known drugs
    ("MONDO_0020250", "autosomal dominant optic atrophy"),  # 1672 genes, 1 known drugs
    ("MONDO_0020311", "chronic myelomonocytic leukemia"),  # 911 genes, 118 known drugs
    ("MONDO_0020480", "sulfite oxidase deficiency due to molybdenum cofactor deficiency"),  # 325 genes, 1 known drugs
    ("MONDO_0020492", "hemimegalencephaly"),  # 629 genes, 1 known drugs
    ("MONDO_0020531", "long chain acyl-CoA dehydrogenase deficiency"),  # 599 genes, 4 known drugs
    ("MONDO_0020560", "atypical teratoid rhabdoid tumor"),  # 1819 genes, 37 known drugs
    ("MONDO_0020561", "myxoid/round cell liposarcoma"),  # 383 genes, 7 known drugs
    ("MONDO_0020562", "pleomorphic liposarcoma"),  # 141 genes, 2 known drugs
    ("MONDO_0020563", "dedifferentiated liposarcoma"),  # 269 genes, 37 known drugs
    ("MONDO_0020598", "malabsorption syndrome"),  # 2464 genes, 1 known drugs
    ("MONDO_0020634", "grade III meningioma"),  # 100 genes, 1 known drugs
    ("MONDO_0020635", "anaplastic meningioma"),  # 100 genes, 1 known drugs
    ("MONDO_0020640", "autoimmune encephalitis"),  # 402 genes, 21 known drugs
    ("MONDO_0020642", "polycystic kidney disease"),  # 2793 genes, 7 known drugs
    ("MONDO_0020654", "renal pelvis/ureter urothelial carcinoma"),  # 700 genes, 23 known drugs
    ("MONDO_0020669", "paranasal sinus cancer"),  # 87 genes, 4 known drugs
    ("MONDO_0020678", "sensorineural hearing loss disorder"),  # 1289 genes, 17 known drugs
    ("MONDO_0020680", "acute bronchiolitis"),  # 69 genes, 8 known drugs
    ("MONDO_0020686", "acute tonsillitis"),  # 360 genes, 3 known drugs
    ("MONDO_0020689", "AIDS dementia complex"),  # 1428 genes, 8 known drugs
    ("MONDO_0020720", "X-linked hypophosphatemic rickets"),  # 871 genes, 3 known drugs
    ("MONDO_0020743", "mixed phenotype acute leukemia"),  # 245 genes, 48 known drugs
    ("MONDO_0020760", "skin squamous cell carcinoma in situ"),  # 224 genes, 2 known drugs
    ("MONDO_0020761", "Bowen disease of the skin"),  # 222 genes, 3 known drugs
    ("MONDO_0020804", "basal cell carcinoma"),  # 2888 genes, 57 known drugs
    ("MONDO_0021009", "salivary gland mucoepidermoid carcinoma"),  # 180 genes, 1 known drugs
    ("MONDO_0021023", "complete androgen insensitivity syndrome"),  # 258 genes, 3 known drugs
    ("MONDO_0021040", "pancreatic neoplasm"),  # 10964 genes, 30 known drugs
    ("MONDO_0021042", "glioma"),  # 12664 genes, 188 known drugs
    ("MONDO_0021054", "bone sarcoma"),  # 1574 genes, 51 known drugs
    ("MONDO_0021055", "classic familial adenomatous polyposis"),  # 437 genes, 2 known drugs
    ("MONDO_0021056", "familial adenomatous polyposis 1"),  # 185 genes, 1 known drugs
    ("MONDO_0021061", "neurofibromatosis"),  # 2523 genes, 1 known drugs
    ("MONDO_0021063", "malignant colon neoplasm"),  # 11868 genes, 146 known drugs
    ("MONDO_0021069", "malignant endocrine neoplasm"),  # 17783 genes, 6 known drugs
    ("MONDO_0021071", "laryngeal neoplasm"),  # 2396 genes, 2 known drugs
    ("MONDO_0021081", "anti-NMDA receptor encephalitis"),  # 330 genes, 1 known drugs
    ("MONDO_0021085", "gastric neoplasm"),  # 14564 genes, 47 known drugs
    ("MONDO_0021094", "immunodeficiency disease"),  # 6622 genes, 16 known drugs
    ("MONDO_0021095", "parkinsonian disorder"),  # 8765 genes, 1 known drugs
    ("MONDO_0021104", "alcoholic fatty liver disease"),  # 493 genes, 5 known drugs
    ("MONDO_0021108", "meningitis"),  # 1633 genes, 15 known drugs
    ("MONDO_0021113", "respiratory failure"),  # 4229 genes, 50 known drugs
    ("MONDO_0021117", "lung neoplasm"),  # 16038 genes, 6 known drugs
    ("MONDO_0021138", "bone marrow cancer"),  # 13997 genes, 1 known drugs
    ("MONDO_0021146", "headache disorder"),  # 3108 genes, 8 known drugs
    ("MONDO_0021165", "Paget disease"),  # 670 genes, 8 known drugs
    ("MONDO_0021167", "myositis disease"),  # 2647 genes, 2 known drugs
    ("MONDO_0021211", "brain neoplasm"),  # 6876 genes, 94 known drugs
    ("MONDO_0021228", "brainstem neoplasm"),  # 742 genes, 9 known drugs
    ("MONDO_0021231", "retina neoplasm"),  # 3337 genes, 1 known drugs
    ("MONDO_0021232", "pineal body neoplasm"),  # 723 genes, 3 known drugs
    ("MONDO_0021234", "spinal cord neoplasm"),  # 221 genes, 4 known drugs
    ("MONDO_0021245", "oral cavity neoplasm"),  # 4480 genes, 4 known drugs
    ("MONDO_0021248", "nervous system neoplasm"),  # 15468 genes, 1 known drugs
    ("MONDO_0021310", "malignant tumor of neck"),  # 5482 genes, 2 known drugs
    ("MONDO_0021315", "malignant tumor of nasopharynx"),  # 4942 genes, 3 known drugs
    ("MONDO_0021322", "malignant tumor of meninges"),  # 150 genes, 1 known drugs
    ("MONDO_0021327", "carcinoma of urethra"),  # 154 genes, 1 known drugs
    ("MONDO_0021337", "tonsil carcinoma"),  # 199 genes, 4 known drugs
    ("MONDO_0021355", "neoplasm of esophagus"),  # 12622 genes, 3 known drugs
    ("MONDO_0021357", "tumor of salivary gland"),  # 1450 genes, 8 known drugs
    ("MONDO_0021375", "tumor of duodenum"),  # 1048 genes, 1 known drugs
    ("MONDO_0021392", "polyp of large intestine"),  # 878 genes, 6 known drugs
    ("MONDO_0021400", "polyp of colon"),  # 657 genes, 1 known drugs
    ("MONDO_0021416", "polyp of gallbladder"),  # 213 genes, 2 known drugs
    ("MONDO_0021533", "intestinal neuroendocrine tumor G1"),  # 239 genes, 2 known drugs
    ("MONDO_0021541", "hemangioma of retina"),  # 62 genes, 2 known drugs
    ("MONDO_0021553", "transverse myelitis"),  # 125 genes, 21 known drugs
    ("MONDO_0021581", "connective tissue neoplasm"),  # 15254 genes, 2 known drugs
    ("MONDO_0021632", "primary brain neoplasm"),  # 551 genes, 12 known drugs
    ("MONDO_0021636", "astrocytic tumor"),  # 10568 genes, 3 known drugs
    ("MONDO_0021637", "low grade glioma"),  # 3621 genes, 50 known drugs
    ("MONDO_0021640", "grade III glioma"),  # 754 genes, 36 known drugs
    ("MONDO_0021662", "bile duct neoplasm"),  # 9043 genes, 5 known drugs
    ("MONDO_0021667", "neuralgia"),  # 780 genes, 10 known drugs
    ("MONDO_0021698", "alcohol-related disorders"),  # 2825 genes, 1 known drugs
    ("MONDO_0021765", "radiculitis"),  # 77 genes, 4 known drugs
    ("MONDO_0021925", "tracheobronchitis"),  # 638 genes, 3 known drugs
    ("MONDO_0022113", "central centrifugal cicatricial alopecia"),  # 133 genes, 5 known drugs
    ("MONDO_0022205", "pustular psoriasis"),  # 637 genes, 8 known drugs
    ("MONDO_0022308", "corticobasal degeneration disorder"),  # 130 genes, 2 known drugs
    ("MONDO_0022430", "persistent fetal circulation syndrome"),  # 345 genes, 12 known drugs
    ("MONDO_0022687", "cerebellar degeneration"),  # 7119 genes, 1 known drugs
    ("MONDO_0023644", "lip and oral cavity carcinoma"),  # 4773 genes, 20 known drugs
    ("MONDO_0023880", "WHIM syndrome"),  # 604 genes, 2 known drugs
    ("MONDO_0024270", "parasitic intestinal disorder"),  # 1262 genes, 3 known drugs
    ("MONDO_0024275", "amebic dysentery"),  # 226 genes, 3 known drugs
    ("MONDO_0024282", "mucinous ovarian cancer"),  # 579 genes, 5 known drugs
    ("MONDO_0024300", "hypophosphatemic rickets"),  # 1487 genes, 6 known drugs
    ("MONDO_0024331", "colorectal carcinoma"),  # 13882 genes, 125 known drugs
    ("MONDO_0024332", "perennial allergic rhinitis"),  # 56 genes, 44 known drugs
    ("MONDO_0024355", "respiratory tract infectious disorder"),  # 7644 genes, 10 known drugs
    ("MONDO_0024361", "circadian rhythm sleep disorder"),  # 124 genes, 5 known drugs
    ("MONDO_0024419", "enthesitis"),  # 156 genes, 4 known drugs
    ("MONDO_0024457", "neurodegeneration with brain iron accumulation 2A"),  # 888 genes, 1 known drugs
    ("MONDO_0024477", "liver and intrahepatic bile duct neoplasm"),  # 16130 genes, 4 known drugs
    ("MONDO_0024503", "digestive system neuroendocrine neoplasm"),  # 2943 genes, 5 known drugs
    ("MONDO_0024609", "vulvar squamous cell carcinoma"),  # 311 genes, 11 known drugs
    ("MONDO_0024619", "central nervous system infectious disorder"),  # 5311 genes, 2 known drugs
    ("MONDO_0024677", "pancreatic insulinoma"),  # 1688 genes, 1 known drugs
    ("MONDO_0024686", "tenosynovial giant cell tumor, diffuse type"),  # 397 genes, 7 known drugs
    ("MONDO_0024879", "metastatic carcinoma"),  # 620 genes, 5 known drugs
    ("MONDO_0024880", "metastatic malignant neoplasm"),  # 2116 genes, 74 known drugs
    ("MONDO_0026777", "VEXAS syndrome"),  # 195 genes, 7 known drugs
    ("MONDO_0030055", "neuronopathy, distal hereditary motor, autosomal recessive 8"),  # 162 genes, 1 known drugs
    ("MONDO_0032766", "hypoalphalipoproteinemia, primary, 2"),  # 1333 genes, 3 known drugs
    ("MONDO_0032920", "juvenile arthritis due to defect in LACC1"),  # 71 genes, 6 known drugs
    ("MONDO_0035838", "idiopathic multicentric Castleman disease"),  # 417 genes, 6 known drugs
    ("MONDO_0040679", "urothelial carcinoma"),  # 5314 genes, 186 known drugs
    ("MONDO_0041052", "postherpetic neuralgia"),  # 137 genes, 53 known drugs
    ("MONDO_0042487", "uterine cervix carcinoma in situ"),  # 266 genes, 1 known drugs
    ("MONDO_0042982", "GATA2 deficiency with susceptibility to MDS/AML"),  # 599 genes, 7 known drugs
    ("MONDO_0043209", "albinism"),  # 1615 genes, 6 known drugs
    ("MONDO_0043373", "sudden sensorineural hearing loss"),  # 159 genes, 20 known drugs
    ("MONDO_0043510", "brain injury"),  # 1681 genes, 74 known drugs
    ("MONDO_0043579", "enteritis"),  # 1275 genes, 2 known drugs
    ("MONDO_0043693", "alcoholic liver diseases"),  # 1471 genes, 7 known drugs
    ("MONDO_0043735", "osteoradionecrosis"),  # 60 genes, 5 known drugs
    ("MONDO_0043797", "spinal cord injury"),  # 1280 genes, 60 known drugs
    ("MONDO_0043836", "tuberculosis, spinal"),  # 82 genes, 1 known drugs
    ("MONDO_0043905", "pneumonitis"),  # 4096 genes, 14 known drugs
    ("MONDO_0043919", "radiation pneumonitis"),  # 242 genes, 12 known drugs
    ("MONDO_0044339", "lumbar disk degenerative disorder"),  # 161 genes, 3 known drugs
    ("MONDO_0044638", "hypopharynx squamous cell carcinoma"),  # 332 genes, 24 known drugs
    ("MONDO_0044704", "oropharynx squamous cell carcinoma"),  # 603 genes, 53 known drugs
    ("MONDO_0044751", "chronic diarrheal disease"),  # 184 genes, 1 known drugs
    ("MONDO_0044753", "lumbar spinal stenosis"),  # 54 genes, 18 known drugs
    ("MONDO_0044782", "esophageal ulcer"),  # 375 genes, 2 known drugs
    ("MONDO_0044785", "desmoplastic melanoma"),  # 510 genes, 1 known drugs
    ("MONDO_0044791", "combined hepatocellular carcinoma and cholangiocarcinoma"),  # 192 genes, 2 known drugs
    ("MONDO_0044792", "large congenital melanocytic nevus"),  # 493 genes, 1 known drugs
    ("MONDO_0044872", "dysautonomia"),  # 196 genes, 6 known drugs
    ("MONDO_0044877", "paraneoplastic cerebellar degeneration"),  # 280 genes, 1 known drugs
    ("MONDO_0044887", "central nervous system non-hodgkin lymphoma"),  # 149 genes, 8 known drugs
    ("MONDO_0044903", "myelofibrosis"),  # 1051 genes, 125 known drugs
    ("MONDO_0044915", "salivary duct carcinoma"),  # 345 genes, 20 known drugs
    ("MONDO_0044919", "malignant renal pelvis neoplasm"),  # 442 genes, 1 known drugs
    ("MONDO_0044925", "oral cavity carcinoma"),  # 3935 genes, 1 known drugs
    ("MONDO_0044926", "oropharyngeal carcinoma"),  # 720 genes, 8 known drugs
    ("MONDO_0044937", "rectal carcinoma"),  # 2562 genes, 12 known drugs
    ("MONDO_0044970", "mitochondrial disease"),  # 7003 genes, 12 known drugs
    ("MONDO_0045057", "delirium"),  # 709 genes, 45 known drugs
    ("MONDO_0056806", "non-small cell squamous lung carcinoma"),  # 452 genes, 81 known drugs
    ("MONDO_0056819", "nasal cavity and paranasal sinus carcinoma"),  # 247 genes, 6 known drugs
    ("MONDO_0100010", "disease of the tendon"),  # 1009 genes, 20 known drugs
    ("MONDO_0100014", "autoimmune retinopathy"),  # 60 genes, 1 known drugs
    ("MONDO_0100039", "CDKL5 disorder"),  # 373 genes, 2 known drugs
    ("MONDO_0100081", "sleep disorder"),  # 5174 genes, 32 known drugs
    ("MONDO_0100083", "hereditary thrombocytopenia and hematological cancer predisposition syndrome associated with RUNX1"),  # 298 genes, 1 known drugs
    ("MONDO_0100114", "dry age related macular degeneration"),  # 499 genes, 7 known drugs
    ("MONDO_0100116", "Middle East respiratory syndrome"),  # 130 genes, 3 known drugs
    ("MONDO_0100130", "adult acute respiratory distress syndrome"),  # 317 genes, 5 known drugs
    ("MONDO_0100137", "telomere syndrome"),  # 3425 genes, 6 known drugs
    ("MONDO_0100150", "RYR1-related myopathy"),  # 999 genes, 2 known drugs
    ("MONDO_0100151", "nephropathic cystinosis"),  # 1088 genes, 3 known drugs
    ("MONDO_0100192", "liver failure"),  # 1933 genes, 15 known drugs
    ("MONDO_0100193", "chronic liver failure"),  # 330 genes, 1 known drugs
    ("MONDO_0100234", "paroxysmal familial ventricular fibrillation"),  # 150 genes, 2 known drugs
    ("MONDO_0100241", "inherited thrombocytopenia"),  # 2980 genes, 1 known drugs
    ("MONDO_0100280", "Waldenstrom macroglobulinemia"),  # 564 genes, 89 known drugs
    ("MONDO_0100286", "respiratory syncytial virus bronchiolitis"),  # 169 genes, 1 known drugs
    ("MONDO_0100288", "enhanced S-cone syndrome"),  # 1898 genes, 1 known drugs
    ("MONDO_0100308", "atactic disorder"),  # 7467 genes, 1 known drugs
    ("MONDO_0100326", "Glanzmann thrombasthenia"),  # 293 genes, 2 known drugs
    ("MONDO_0100342", "malignant glioma"),  # 10566 genes, 208 known drugs
    ("MONDO_0100345", "lactose intolerance"),  # 149 genes, 3 known drugs
    ("MONDO_0100347", "carcinoid syndrome"),  # 195 genes, 12 known drugs
    ("MONDO_0100431", "migraine without aura"),  # 118 genes, 15 known drugs
    ("MONDO_0100464", "acid sphingomyelinase deficiency"),  # 844 genes, 1 known drugs
    ("MONDO_0100491", "generalized pustular psoriasis"),  # 458 genes, 11 known drugs
    ("MONDO_0100574", "generalized epilepsy"),  # 1652 genes, 3 known drugs
    ("MONDO_0100610", "autism spectrum disorder 1"),  # 109 genes, 4 known drugs
    ("MONDO_0100620", "developmental and epileptic encephalopathy"),  # 4516 genes, 4 known drugs
    ("MONDO_0600023", "idiopathic inflammatory myopathy"),  # 1879 genes, 19 known drugs
    ("MONDO_0700081", "newborn respiratory distress syndrome"),  # 824 genes, 24 known drugs
    ("MONDO_0700092", "neurodevelopmental disorder"),  # 10339 genes, 5 known drugs
    ("MONDO_0700115", "proliferative vitreoretinopathy"),  # 1262 genes, 12 known drugs
    ("MONDO_0700418", "idiopathic hypercalciuria"),  # 484 genes, 1 known drugs
    ("MONDO_0800026", "central hypoventilation syndrome, congenital, 1, with or without Hirschsprung disease"),  # 56 genes, 1 known drugs
    ("MONDO_0800027", "leukoencephalopathy, diffuse hereditary, with spheroids 1"),  # 368 genes, 1 known drugs
    ("MONDO_0800031", "central hypoventilation syndrome, congenital"),  # 197 genes, 1 known drugs
    ("MONDO_0800096", "abnormal mineralization disorder"),  # 1738 genes, 3 known drugs
    ("MONDO_0800207", "neuropathy, small fiber"),  # 130 genes, 5 known drugs
    ("MONDO_0800305", "myelofibrosis with myeloid metaplasia"),  # 92 genes, 3 known drugs
    ("MONDO_0800448", "leukoencephalopathy with vanishing white matter"),  # 1318 genes, 1 known drugs
    ("MONDO_0800449", "lysosomal acid lipase deficiency"),  # 1054 genes, 1 known drugs
    ("MONDO_0800453", "juvenile absence epilepsy"),  # 403 genes, 2 known drugs
    ("MONDO_0800491", "early-infantile DEE"),  # 1158 genes, 2 known drugs
    ("MONDO_0800501", "developmental and/or epileptic encephalopathy with spike-wave activation in sleep"),  # 465 genes, 16 known drugs
    ("MONDO_0850302", "intracranial meningioma"),  # 138 genes, 1 known drugs
    ("MONDO_0850340", "supratentorial ependymoma"),  # 71 genes, 1 known drugs
    ("MONDO_0957318", "nephrolithiasis, calcium oxalate"),  # 368 genes, 2 known drugs
    ("MONDO_0980757", "periodontitis, aggressive"),  # 314 genes, 3 known drugs
    ("MONDO_1010128", "peritonitis"),  # 1116 genes, 24 known drugs
    ("MONDO_1040002", "PIK3CA-related overgrowth spectrum"),  # 1395 genes, 5 known drugs
    ("MONDO_1060198", "ischemic stroke"),  # 4120 genes, 214 known drugs
    ("MONDO_8000006", "WHIM syndrome 1"),  # 501 genes, 1 known drugs
    ("Orphanet_100", "Ataxia-telangiectasia"),  # 851 genes, 5 known drugs
    ("Orphanet_124", "Blackfan-Diamond anemia"),  # 1603 genes, 19 known drugs
    ("Orphanet_136", "CADASIL"),  # 542 genes, 4 known drugs
    ("Orphanet_163690", "Hypotonia - cystinuria syndrome"),  # 274 genes, 1 known drugs
    ("Orphanet_167", "Chédiak-Higashi syndrome"),  # 542 genes, 9 known drugs
    ("Orphanet_1764", "Familial dysautonomia"),  # 439 genes, 4 known drugs
    ("Orphanet_182050", "MYH9-related disease"),  # 548 genes, 1 known drugs
    ("Orphanet_183469", "Genetic hypopigmentation of the skin"),  # 1503 genes, 1 known drugs
    ("Orphanet_183654", "Rare genetic coagulation disorder"),  # 2790 genes, 1 known drugs
    ("Orphanet_1872", "Cone rod dystrophy"),  # 2499 genes, 1 known drugs
    ("Orphanet_206966", "Mitochondrial myopathy"),  # 2715 genes, 9 known drugs
    ("Orphanet_228346", "CLN3 disease"),  # 723 genes, 1 known drugs
    ("Orphanet_228349", "CLN2 disease"),  # 537 genes, 1 known drugs
    ("Orphanet_2314", "Autosomal dominant hyper-IgE syndrome"),  # 655 genes, 2 known drugs
    ("Orphanet_2380", "Legg-Calvé-Perthes disease"),  # 204 genes, 1 known drugs
    ("Orphanet_238583", "Hyperphenylalaninemia"),  # 896 genes, 4 known drugs
    ("Orphanet_240085", "Progressive supranuclear palsy - parkinsonism"),  # 347 genes, 1 known drugs
    ("Orphanet_2442", "X-linked lymphoproliferative disease"),  # 873 genes, 4 known drugs
    ("Orphanet_247", "Arrhythmogenic right ventricular dysplasia"),  # 1082 genes, 2 known drugs
    ("Orphanet_247691", "Retinal vasculopathy and cerebral leukodystrophy"),  # 460 genes, 1 known drugs
    ("Orphanet_26106", "Familial gastric cancer"),  # 325 genes, 8 known drugs
    ("Orphanet_269", "Facioscapulohumeral dystrophy"),  # 814 genes, 6 known drugs
    ("Orphanet_271861", "Familial transthyretin-related amyloidosis"),  # 718 genes, 4 known drugs
    ("Orphanet_273", "Steinert myotonic dystrophy"),  # 367 genes, 2 known drugs
    ("Orphanet_276255", "Xeroderma pigmentosum complementation group C"),  # 267 genes, 1 known drugs
    ("Orphanet_277", "Severe combined immunodeficiency due to adenosine deaminase deficiency"),  # 588 genes, 2 known drugs
    ("Orphanet_30", "Hereditary orotic aciduria"),  # 364 genes, 1 known drugs
    ("Orphanet_303", "Dystrophic epidermolysis bullosa"),  # 328 genes, 9 known drugs
    ("Orphanet_308", "Unverricht-Lundborg disease"),  # 840 genes, 2 known drugs
    ("Orphanet_309005", "Disorder of lipid metabolism"),  # 4772 genes, 33 known drugs
    ("Orphanet_313808", "Hereditary diffuse leukoencephalopathy with axonal spheroids and pigmented glia"),  # 396 genes, 1 known drugs
    ("Orphanet_322126", "Genetic tumor of hematopoietic and lymphoid tissues"),  # 1724 genes, 2 known drugs
    ("Orphanet_3421", "Cerebroretinal vasculopathy"),  # 458 genes, 1 known drugs
    ("Orphanet_35689", "Primary lateral sclerosis"),  # 243 genes, 7 known drugs
    ("Orphanet_364", "Glycogen storage disease due to glucose-6-phosphatase deficiency"),  # 961 genes, 3 known drugs
    ("Orphanet_365", "Glycogen storage disease due to acid maltase deficiency"),  # 642 genes, 16 known drugs
    ("Orphanet_37553", "Cardiodysrhythmic potassium-sensitive periodic paralysis"),  # 721 genes, 2 known drugs
    ("Orphanet_394", "Classical homocystinuria"),  # 507 genes, 2 known drugs
    ("Orphanet_411", "Hyperlipoproteinemia type 1"),  # 1446 genes, 2 known drugs
    ("Orphanet_413", "Hyperlipoproteinemia type 4"),  # 650 genes, 1 known drugs
    ("Orphanet_43", "X-linked adrenoleukodystrophy"),  # 1047 genes, 9 known drugs
    ("Orphanet_46724", "Cerebral arteriovenous malformation"),  # 169 genes, 2 known drugs
    ("Orphanet_47045", "Familial cold urticaria"),  # 145 genes, 2 known drugs
    ("Orphanet_51", "Aicardi-Goutières syndrome"),  # 1013 genes, 8 known drugs
    ("Orphanet_53", "Albers-Schönberg osteopetrosis"),  # 967 genes, 1 known drugs
    ("Orphanet_550", "MELAS"),  # 958 genes, 6 known drugs
    ("Orphanet_551", "MERRF"),  # 664 genes, 1 known drugs
    ("Orphanet_552", "MODY"),  # 1196 genes, 2 known drugs
    ("Orphanet_590", "Congenital myasthenic syndromes"),  # 1491 genes, 4 known drugs
    ("Orphanet_597", "Central core disease"),  # 413 genes, 1 known drugs
    ("Orphanet_60", "Alpha-1-antitrypsin deficiency"),  # 833 genes, 7 known drugs
    ("Orphanet_602", "Distal myopathy, Nonaka type"),  # 490 genes, 1 known drugs
    ("Orphanet_63261", "HERNS syndrome"),  # 449 genes, 1 known drugs
    ("Orphanet_654", "Nephroblastoma"),  # 1416 genes, 12 known drugs
    ("Orphanet_68335", "Chromosomal anomaly"),  # 2746 genes, 1 known drugs
    ("Orphanet_701", "Alopecia universalis"),  # 337 genes, 17 known drugs
    ("Orphanet_71291", "Hereditary vascular retinopathy"),  # 449 genes, 1 known drugs
    ("Orphanet_733", "Familial adenomatous polyposis"),  # 849 genes, 12 known drugs
    ("Orphanet_758", "Pseudoxanthoma elasticum"),  # 1075 genes, 2 known drugs
    ("Orphanet_77259", "Gaucher disease type 1"),  # 845 genes, 8 known drugs
    ("Orphanet_77261", "Gaucher disease type 3"),  # 831 genes, 3 known drugs
    ("Orphanet_79161", "Disorder of carbohydrate metabolism"),  # 2946 genes, 1 known drugs
    ("Orphanet_79167", "Disorder of urea cycle metabolism and ammonia detoxification"),  # 1016 genes, 2 known drugs
    ("Orphanet_79168", "Disorder of bile acid synthesis"),  # 523 genes, 1 known drugs
    ("Orphanet_79211", "Combined hyperlipidemia"),  # 978 genes, 25 known drugs
    ("Orphanet_79259", "Glycogen storage disease due to glucose-6-phosphatase deficiency type b"),  # 801 genes, 1 known drugs
    ("Orphanet_79277", "Congenital erythropoietic porphyria"),  # 562 genes, 1 known drugs
    ("Orphanet_79282", "Methylmalonic acidemia with homocystinuria, type cblC"),  # 276 genes, 1 known drugs
    ("Orphanet_79293", "Familial LCAT deficiency"),  # 863 genes, 1 known drugs
    ("Orphanet_816", "Sjögren-Larsson syndrome"),  # 950 genes, 2 known drugs
    ("Orphanet_846", "Alpha-thalassemia"),  # 604 genes, 1 known drugs
    ("Orphanet_848", "Beta-thalassemia"),  # 717 genes, 42 known drugs
    ("Orphanet_891", "Familial exudative vitreoretinopathy"),  # 2465 genes, 1 known drugs
    ("Orphanet_89936", "X-linked hypophosphatemia"),  # 845 genes, 4 known drugs
    ("Orphanet_90", "Argininemia"),  # 419 genes, 1 known drugs
    ("Orphanet_903", "Von Willebrand disease"),  # 553 genes, 16 known drugs
    ("Orphanet_90342", "Xeroderma pigmentosum variant"),  # 274 genes, 1 known drugs
    ("Orphanet_90642", "Syndromic genetic deafness"),  # 4580 genes, 1 known drugs
    ("Orphanet_91088", "Other metabolic disease"),  # 5162 genes, 7 known drugs
    ("Orphanet_927", "Hyperammonemia due to N-acetylglutamate synthetase deficiency"),  # 549 genes, 1 known drugs
    ("Orphanet_95157", "Acute hepatic porphyria"),  # 293 genes, 2 known drugs
    ("Orphanet_98671", "Optic neuropathy"),  # 2275 genes, 13 known drugs
    ("Orphanet_98757", "Spinocerebellar ataxia type 3"),  # 857 genes, 4 known drugs
    ("Orphanet_98873", "Congenital dyserythropoietic anemia type II"),  # 386 genes, 1 known drugs
    ("Orphanet_98974", "Fuchs endothelial corneal dystrophy"),  # 1562 genes, 5 known drugs
]
