#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates src/data/cropsDatabase.ts containing over 220+ verified crops
across Maharashtra and India with rich botanical, phenological, and pathology data.
"""

import json
import os

PULSES = [
    {
        "id": "pigeon-pea-tur",
        "name": "Pigeon Pea (Tur / Arhar)",
        "localName": "तूर / अरहर (Tur / Arhar)",
        "scientificName": "Cajanus cajan",
        "category": "Pulses & Legumes",
        "avatarEmoji": "🫘",
        "season": "Kharif",
        "maharashtraRegion": "Marathwada (Latur is Asia's largest Tur dal trading hub), Vidarbha (Akola, Amravati), Khandesh",
        "description": "The foundation of Indian dal. Deep-rooted legume fixing nitrogen and enriching black soils; grown predominantly as intercrop with Soybean or Cotton.",
        "optimalTemp": "25°C - 35°C",
        "waterRequirement": "600 - 800 mm; drought-hardy due to deep taproot.",
        "soilPreference": "Deep, well-drained black cotton soil or loam, pH 6.5 - 7.5; zero water stagnation.",
        "growthStages": [
            {"stage": "Seedling & Branching", "days": "Days 1-45", "description": "Slow early growth while deep taproot establishes."},
            {"stage": "Canopy & Flowering", "days": "Days 46-100", "description": "Profuse yellow blooms attract pollinators."},
            {"stage": "Pod Formation & Filling", "days": "Days 101-140", "description": "Green pods develop; pod borer vulnerable stage."},
            {"stage": "Maturity & Harvest", "days": "Days 141-180", "description": "Pods turn dry brown; harvested with threshers."}
        ],
        "commonDiseases": [
            {"name": "Fusarium Wilt (Fusarium udum)", "symptoms": "Gradual wilting, purple bands on stems, vascular browning when stem is split.", "riskPeriod": "Flowering stage during soil moisture fluctuations."},
            {"name": "Sterility Mosaic Disease (SMD)", "symptoms": "Excessive bushiness, pale green mosaic leaves, complete lack of flowers; transmitted by eriophyid mites.", "riskPeriod": "Dense canopies with high mite vector populations."}
        ],
        "commonPests": ["Gram Pod Borer (Helicoverpa armigera)", "Plume Moth", "Pod Fly (Melanagromyza obtusa)", "Maruca Pod Borer"],
        "generalPrevention": [
            "Use wilt and SMD-resistant varieties like BSMR-736, BDN-711, or Maruti (ICP-8863).",
            "Seed treatment with Trichoderma viride @ 4g/kg + Rhizobium culture.",
            "Install bird perches @ 20/ha and pheromone traps @ 10/ha for Helicoverpa control."
        ]
    },
    {
        "id": "chickpea-chana",
        "name": "Chickpea (Bengal Gram / Chana)",
        "localName": "हरभरा / चणा (Harbhara / Chana)",
        "scientificName": "Cicer arietinum",
        "category": "Pulses & Legumes",
        "avatarEmoji": "🫘",
        "season": "Rabi (Winter)",
        "maharashtraRegion": "Marathwada (Latur, Osmanabad), Western Maharashtra (Ahmednagar, Solapur), Vidarbha",
        "description": "Premier winter pulse crop of Maharashtra. Consumed as fresh green pods (Hurda/Harbhara ghaati), roasted gram, besan flour, and dry dal.",
        "optimalTemp": "15°C - 25°C (cool nights, dry sunny days)",
        "waterRequirement": "250 - 350 mm; requires 1-2 protective irrigations at branching and pod filling.",
        "soilPreference": "Deep, moisture-retentive black cotton soil with pH 6.0 - 8.0.",
        "growthStages": [
            {"stage": "Emergence & Nipping", "days": "Days 1-25", "description": "Terminal bud nipping done at 25-30 days to stimulate heavy lateral branching."},
            {"stage": "Flowering", "days": "Days 26-55", "description": "Delicate pinkish or white flowers appear in leaf axils."},
            {"stage": "Pod Development", "days": "Days 56-85", "description": "Pods swell containing 1-2 plump seeds."},
            {"stage": "Maturity", "days": "Days 86-110", "description": "Foliage turns golden brown; grains harden."}
        ],
        "commonDiseases": [
            {"name": "Fusarium Wilt (Fusarium oxysporum f. sp. ciceris)", "symptoms": "Leaves drop, roots exhibit internal dark brown vascular discoloration.", "riskPeriod": "Warm early winter soils or mid-season moisture stress."},
            {"name": "Ascochyta Blight", "symptoms": "Circular lesions with concentric rings of pycnidia on leaves, stems, and pods.", "riskPeriod": "Cool, wet, cloudy winter spells."}
        ],
        "commonPests": ["Gram Pod Borer (Helicoverpa armigera)", "Cutworms", "Aphids"],
        "generalPrevention": [
            "Plant wilt-resistant varieties like Digvijay, Vijay, Phule Vikram, or Jaki-9218.",
            "Treat seed with Trichoderma viride @ 5g/kg + Carbendazim @ 2g/kg.",
            "Perform terminal nipping at 30 days to double pod-bearing branches."
        ]
    },
    {
        "id": "green-gram-moong",
        "name": "Green Gram (Moong)",
        "localName": "मूग (Moong)",
        "scientificName": "Vigna radiata",
        "category": "Pulses & Legumes",
        "avatarEmoji": "🌱",
        "season": "Kharif & Summer",
        "maharashtraRegion": "Marathwada, Vidarbha, Jalgaon, Dhule, Ahmednagar",
        "description": "Quick-maturing (60-70 days) protein-rich pulse crop ideal for crop rotations and soil health regeneration.",
        "optimalTemp": "25°C - 35°C",
        "waterRequirement": "300 - 400 mm.",
        "soilPreference": "Well-drained loam to clay loam.",
        "growthStages": [
            {"stage": "Vegetative", "days": "Days 1-25", "description": "Rapid leaf canopy and root nodulation."},
            {"stage": "Flowering", "days": "Days 26-45", "description": "Yellow blossoms in clusters."},
            {"stage": "Pod Maturity", "days": "Days 46-65", "description": "Black cylindrical pods ready for picking."}
        ],
        "commonDiseases": [
            {"name": "Yellow Mosaic Virus (MYMV)", "symptoms": "Irregular yellow and green patches on leaves; transmitted by whiteflies.", "riskPeriod": "Hot dry weather with high whitefly activity."},
            {"name": "Powdery Mildew", "symptoms": "White powdery coating on foliage.", "riskPeriod": "Humid mornings."}
        ],
        "commonPests": ["Whitefly", "Thrips", "Pod Borer", "Aphids"],
        "generalPrevention": ["Grow MYMV-resistant varieties (BM-2002-1, BM-2003-2, Vaibhav).", "Seed treatment with Imidacloprid @ 5g/kg."]
    },
    {
        "id": "black-gram-urad",
        "name": "Black Gram (Urad)",
        "localName": "उडीद (Udid / Urad)",
        "scientificName": "Vigna mungo",
        "category": "Pulses & Legumes",
        "avatarEmoji": "🫘",
        "season": "Kharif & Summer",
        "maharashtraRegion": "Vidarbha (Nagpur, Wardha), Marathwada (Nanded, Latur), Khandesh",
        "description": "Indispensable pulse in Indian culinary traditions for papad, idli, vada, and dal makhani.",
        "optimalTemp": "25°C - 35°C",
        "waterRequirement": "350 - 450 mm.",
        "soilPreference": "Medium to heavy black cotton soils with good drainage.",
        "growthStages": [
            {"stage": "Vegetative", "days": "Days 1-25", "description": "Dense hairy stems and trifoliate leaves."},
            {"stage": "Flowering", "days": "Days 26-45", "description": "Bright yellow flowers."},
            {"stage": "Pod Ripening", "days": "Days 46-70", "description": "Hairy pods turn black when ripe."}
        ],
        "commonDiseases": [
            {"name": "Yellow Mosaic Virus", "symptoms": "Bright golden yellow mottling.", "riskPeriod": "Whitefly outbreaks."},
            {"name": "Cercospora Leaf Spot", "symptoms": "Brown spots with reddish margins.", "riskPeriod": "Warm rainy periods."}
        ],
        "commonPests": ["Whitefly", "Pod Borer", "Stem Fly", "Aphids"],
        "generalPrevention": ["Use resistant varieties like TAU-1, TPU-4, AKU-15.", "Seed treatment with Trichoderma."]
    },
    {
        "id": "soybean",
        "name": "Soybean",
        "localName": "सोयाबीन (Soybean)",
        "scientificName": "Glycine max",
        "category": "Pulses & Legumes",
        "avatarEmoji": "🌱",
        "season": "Kharif",
        "maharashtraRegion": "Marathwada (Latur, Nanded), Vidarbha (Amravati, Akola, Yavatmal, Nagpur), Western Maharashtra (Kolhapur, Sangli)",
        "description": "The golden bean that revolutionized Maharashtra agriculture. Miracle crop delivering 40% protein and 20% edible oil, supporting millions of rural livelihoods.",
        "optimalTemp": "24°C - 30°C",
        "waterRequirement": "450 - 650 mm; highly sensitive to dry spells at pod-filling.",
        "soilPreference": "Deep, fertile well-drained black cotton soil, pH 6.5 - 7.5.",
        "growthStages": [
            {"stage": "Germination & Vegetative (V1-V4)", "days": "Days 1-30", "description": "Emergence, unifoliate and trifoliate leaf expansion, root nodulation with Bradyrhizobium."},
            {"stage": "Flowering (R1-R2)", "days": "Days 31-50", "description": "Tiny purple or white flowers open in leaf axils."},
            {"stage": "Pod Development (R3-R4)", "days": "Days 51-70", "description": "Pods elongate; critical moisture-sensitive phase."},
            {"stage": "Seed Filling & Senescence (R5-R8)", "days": "Days 71-100", "description": "Leaves yellow and drop; pods turn golden brown containing 2-3 round seeds."}
        ],
        "commonDiseases": [
            {"name": "Soybean Rust (Phakopsora pachyrhizi)", "symptoms": "Tiny brown to reddish-brown lesions with erupting volcanic pustules on leaf undersides.", "riskPeriod": "Extended cloudiness, high relative humidity (>85%), temp 18-26°C."},
            {"name": "Charcoal Rot (Macrophomina phaseolina)", "symptoms": "Sub-epidermal black specks (microsclerotia) causing premature plant death and stem splitting.", "riskPeriod": "Post-flowering drought accompanied by high soil temp (>33°C)."},
            {"name": "Collar Rot / Root Rot (Sclerotium rolfsii)", "symptoms": "White fan-shaped fungal mycelium with brown mustard-like seeds at soil line.", "riskPeriod": "Waterlogged soil conditions during seedling stage."}
        ],
        "commonPests": ["Girdle Beetle (Obereopsis brevis)", "Spodoptera litura (Tobacco Caterpillar)", "Semilooper", "Gram Pod Borer", "Stem Fly"],
        "generalPrevention": [
            "Use high-yielding university varieties: JS-335, JS-9305, Phule Sangam (KDS-726), Phule Kimaya (KDS-753).",
            "Inoculate seed with Bradyrhizobium japonicum + PSB culture @ 250g per 10kg seed.",
            "Treat seed with Carboxin + Thiram @ 2g/kg or Trichoderma @ 4g/kg.",
            "Apply light hoeing to eradicate Girdle beetle egg rings on petiole."
        ]
    },
    {
        "id": "moth-bean-matki",
        "name": "Moth Bean (Matki)",
        "localName": "मटकी (Matki / Moth)",
        "scientificName": "Vigna aconitifolia",
        "category": "Pulses & Legumes",
        "avatarEmoji": "🫘",
        "season": "Kharif",
        "maharashtraRegion": "Ahmednagar, Solapur, Beed, Dhule, Jalgaon dry zones",
        "description": "Super-drought hardy pulse; soul of Maharashtra's beloved breakfast dish 'Misal Pav' when sprouted.",
        "optimalTemp": "25°C - 38°C",
        "waterRequirement": "200 - 300 mm; survives severe dry spells.",
        "soilPreference": "Light, sandy, gravelly marginal soils.",
        "growthStages": [
            {"stage": "Vegetative", "days": "Days 1-30", "description": "Prostrate spreading ground cover."},
            {"stage": "Flowering", "days": "Days 31-50", "description": "Yellow blossoms."},
            {"stage": "Pod Ripening", "days": "Days 51-75", "description": "Slender pods turn brown."}
        ],
        "commonDiseases": [{"name": "Yellow Mosaic Virus", "symptoms": "Yellowing of leaves.", "riskPeriod": "Hot dry weather."}],
        "commonPests": ["Jassids", "Whitefly", "Pod Borer"],
        "generalPrevention": ["Use improved varieties like Phule Matki-15, RMO-40.", "Excellent soil-protecting cover crop against erosion."]
    },
    {
        "id": "cowpea-chawli",
        "name": "Cowpea (Chawli / Lobia)",
        "localName": "चवळी (Chawli / Lobia)",
        "scientificName": "Vigna unguiculata",
        "category": "Pulses & Legumes",
        "avatarEmoji": "🫘",
        "season": "Kharif & Summer",
        "maharashtraRegion": "Konkan, Western Maharashtra, Marathwada, Vidarbha",
        "description": "Versatile dual-purpose crop grown for tender green vegetable pods, nutritious dry pulse, and green manure.",
        "optimalTemp": "24°C - 34°C",
        "waterRequirement": "350 - 450 mm.",
        "soilPreference": "Adaptable to poor acid or alkaline soils.",
        "growthStages": [
            {"stage": "Vegetative", "days": "Days 1-30", "description": "Vigorous twining or bush growth."},
            {"stage": "Pod Setting", "days": "Days 31-55", "description": "Long green hanging pods."},
            {"stage": "Maturity", "days": "Days 56-85", "description": "Dry grain pods harvested."}
        ],
        "commonDiseases": [{"name": "Anthracnose", "symptoms": "Sunken brown lesions on pods.", "riskPeriod": "Continuous rain."}],
        "commonPests": ["Aphids (Aphis craccivora)", "Pod Borer"],
        "generalPrevention": ["Use Phule CP-05040, Konkan Safed varieties.", "Spray NSKE 5% for aphid control."]
    },
    {
        "id": "lentil-masoor",
        "name": "Lentil (Masoor)",
        "localName": "मसूर (Masoor)",
        "scientificName": "Lens culinaris",
        "category": "Pulses & Legumes",
        "avatarEmoji": "🫘",
        "season": "Rabi (Winter)",
        "maharashtraRegion": "Vidarbha (Nagpur, Bhandara), Marathwada, Central India",
        "description": "Ancient quick-cooking protein-rich pulse cultivated in residual soil moisture after paddy.",
        "optimalTemp": "15°C - 24°C",
        "waterRequirement": "200 - 300 mm.",
        "soilPreference": "Well-drained clay loam or alluvial soils.",
        "growthStages": [
            {"stage": "Seedling", "days": "Days 1-25", "description": "Delicate pinnate leaves."},
            {"stage": "Flowering", "days": "Days 26-55", "description": "Small bluish-white blossoms."},
            {"stage": "Pod Filling & Harvest", "days": "Days 56-90", "description": "Flat pods holding 1-2 lens-shaped seeds."}
        ],
        "commonDiseases": [{"name": "Rust", "symptoms": "Uredial pustules on leaves.", "riskPeriod": "Cool humid conditions."}],
        "commonPests": ["Pod Borer", "Aphids"],
        "generalPrevention": ["Seed treatment with Trichoderma.", "Use KLS-218, JL-3 varieties."]
    },
    {
        "id": "field-pea-vatana",
        "name": "Field Pea (Dry Vatana / Green Peas)",
        "localName": "वाटाणा (Vatana / Matar)",
        "scientificName": "Pisum sativum",
        "category": "Pulses & Legumes",
        "avatarEmoji": "🫛",
        "season": "Rabi",
        "maharashtraRegion": "Nashik, Pune, Satara, Ahmednagar cool winter pockets",
        "description": "Grown for sweet tender fresh green peas and sun-dried white/green vatana for famous street foods and curries.",
        "optimalTemp": "13°C - 20°C",
        "waterRequirement": "300 - 400 mm.",
        "soilPreference": "Well-drained fertile loamy soil, pH 6.0 - 7.5.",
        "growthStages": [
            {"stage": "Vegetative", "days": "Days 1-30", "description": "Tendril-bearing climbing foliage."},
            {"stage": "Blossom & Podding", "days": "Days 31-60", "description": "White butterfly-like flowers; sweet pods swell."},
            {"stage": "Harvest", "days": "Days 61-90", "description": "Green pods handpicked or left to dry."}
        ],
        "commonDiseases": [
            {"name": "Powdery Mildew (Erysiphe pisi)", "symptoms": "White powdery coating covering leaves, stems, and pods.", "riskPeriod": "Dry warm days and cool humid nights."}
        ],
        "commonPests": ["Pea Pod Borer", "Pea Aphid", "Leaf Miner"],
        "generalPrevention": ["Grow powdery mildew resistant varieties (Arkel, Azad P-1, Phule Priya).", "Spray Wettable Sulfur @ 3g/L."]
    },
    {
        "id": "horse-gram-kulthi",
        "name": "Horse Gram (Kulthi / Kulith)",
        "localName": "कुळीथ / हुलगा (Kulith / Hulga)",
        "scientificName": "Macrotyloma uniflorum",
        "category": "Pulses & Legumes",
        "avatarEmoji": "🫘",
        "season": "Kharif & Late Kharif",
        "maharashtraRegion": "Konkan (Ratnagiri, Sindhudurg), Western Ghats, Solapur, Ahmednagar",
        "description": "Nutritional powerhouse known for dissolving kidney stones and making soul-warming Konkani Pithla and soup.",
        "optimalTemp": "20°C - 32°C",
        "waterRequirement": "200 - 300 mm; extreme drought resistance.",
        "soilPreference": "Gravelly lateritic, red or impoverished hill soils.",
        "growthStages": [
            {"stage": "Vegetative", "days": "Days 1-35", "description": "Dense low-creeping vine."},
            {"stage": "Flowering", "days": "Days 36-65", "description": "Small yellow blossoms."},
            {"stage": "Maturity", "days": "Days 66-95", "description": "Curved dry pods with flat hard seeds."}
        ],
        "commonDiseases": [{"name": "Dry Root Rot", "symptoms": "Bark shredded at collar.", "riskPeriod": "Extreme heat."}],
        "commonPests": ["Pod Borer", "Hairy Caterpillar"],
        "generalPrevention": ["Use Dapoli-1, Sina varieties.", "Valuable green cover crop to stop hill soil runoff."]
    },
    {
        "id": "rajma-kidney-beans",
        "name": "Kidney Bean (Rajma)",
        "localName": "राजमा (Rajma)",
        "scientificName": "Phaseolus vulgaris",
        "category": "Pulses & Legumes",
        "avatarEmoji": "🫘",
        "season": "Rabi in Maharashtra / Kharif in Hills",
        "maharashtraRegion": "Western Maharashtra (Pune, Satara, Ahmednagar irrigated winter tracts), Jammu & Kashmir, Himachal",
        "description": "High-value protein pulse yielding plump red kidney beans with rich savory flavor.",
        "optimalTemp": "15°C - 25°C",
        "waterRequirement": "400 - 500 mm.",
        "soilPreference": "Rich, fertile loamy soil with excellent drainage.",
        "growthStages": [
            {"stage": "Vegetative", "days": "Days 1-30", "description": "Bush or pole type upright stems."},
            {"stage": "Flowering", "days": "Days 31-55", "description": "White or purple blooms."},
            {"stage": "Pod Maturity", "days": "Days 56-95", "description": "Large kidney-shaped seeds fill."}
        ],
        "commonDiseases": [{"name": "Bean Anthracnose", "symptoms": "Sunken dark cankers on pods.", "riskPeriod": "Wet humid spells."}],
        "commonPests": ["Aphid", "Pod Borer", "Whitefly"],
        "generalPrevention": ["Apply 100-120 kg N/ha since Rajma lacks active root nodulation.", "Use Varun, HUR-15 varieties."]
    },
    {
        "id": "cluster-bean-guar",
        "name": "Cluster Bean (Guar)",
        "localName": "गवार (Gawar / Guar)",
        "scientificName": "Cyamopsis tetragonoloba",
        "category": "Pulses & Legumes",
        "avatarEmoji": "🫛",
        "season": "Kharif & Summer",
        "maharashtraRegion": "Nashik, Pune, Ahmednagar, Marathwada, Rajasthan border tracts",
        "description": "Drought-hardy legume grown for delicious green vegetable clusters and industrial guar gum (galactomannan).",
        "optimalTemp": "26°C - 35°C",
        "waterRequirement": "250 - 350 mm.",
        "soilPreference": "Sandy to loamy well-drained soils.",
        "growthStages": [
            {"stage": "Vegetative", "days": "Days 1-30", "description": "Stiff upright branching."},
            {"stage": "Clustering", "days": "Days 31-55", "description": "Pods form in tight clusters at leaf nodes."},
            {"stage": "Maturity", "days": "Days 56-90", "description": "Tender vegetable pickings or seed drying."}
        ],
        "commonDiseases": [{"name": "Bacterial Blight", "symptoms": "V-shaped brown lesions on leaf margins.", "riskPeriod": "Monsoon humidity."}],
        "commonPests": ["Jassids", "Aphids", "Whitefly"],
        "generalPrevention": ["Grow Pusa Navbahar, Phule Gaurav.", "Seed treatment with Streptocycline @ 100 ppm."]
    },
    {
        "id": "broad-bean-fava",
        "name": "Broad Bean (Fava Bean)",
        "localName": "घेवडा / बाकला (Bakla / Broad Bean)",
        "scientificName": "Vicia faba",
        "category": "Pulses & Legumes",
        "avatarEmoji": "🫘",
        "season": "Rabi",
        "maharashtraRegion": "Mahabaleshwar, Pune, Western Ghat plateaus, North India",
        "description": "Cool-season ancient legume producing large succulent nutrient-rich beans in thick leathery pods.",
        "optimalTemp": "12°C - 20°C",
        "waterRequirement": "350 - 450 mm.",
        "soilPreference": "Heavy fertile clay loams.",
        "growthStages": [
            {"stage": "Vegetative", "days": "Days 1-35", "description": "Square hollow stems and glaucous leaves."},
            {"stage": "Flowering", "days": "Days 36-65", "description": "White flowers with dark blotches."},
            {"stage": "Pod Harvest", "days": "Days 66-105", "description": "Large thick pods."}
        ],
        "commonDiseases": [{"name": "Chocolate Spot (Botrytis fabae)", "symptoms": "Reddish-brown spots across leaves.", "riskPeriod": "Cool overcast weather."}],
        "commonPests": ["Black Bean Aphid"],
        "generalPrevention": ["Ensure wide row spacing (45 cm) for cross-ventilation."]
    },
    {
        "id": "hyacinth-bean-wal",
        "name": "Hyacinth Bean (Wal / Pavta)",
        "localName": "वाल / पावटा (Wal / Kadve Wal / Surti Wal)",
        "scientificName": "Lablab purpureus",
        "category": "Pulses & Legumes",
        "avatarEmoji": "🫘",
        "season": "Late Kharif & Rabi",
        "maharashtraRegion": "Konkan (Alibag Wal has GI status!), Pune, Satara, Western Maharashtra",
        "description": "Iconic pulse of Maharashtra coastal cuisine (Alibag Walachi Usal / Birde). Famous for distinct aromatic taste and high medicinal value.",
        "optimalTemp": "18°C - 28°C",
        "waterRequirement": "350 - 450 mm; grown on residual moisture in rice fallows.",
        "soilPreference": "Medium black to coastal alluvium.",
        "growthStages": [
            {"stage": "Vegetative & Trailing", "days": "Days 1-45", "description": "Vigorous climbing vine trained on bunds or rice stubble."},
            {"stage": "Blossoming", "days": "Days 46-75", "description": "White or purple fragrant flower racemes."},
            {"stage": "Pod Picking", "days": "Days 76-120", "description": "Broad flat pods harvested for fresh beans or dried."}
        ],
        "commonDiseases": [{"name": "Yellow Mosaic", "symptoms": "Golden leaf discoloration.", "riskPeriod": "Whitefly season."}],
        "commonPests": ["Aphids", "Pod Borer"],
        "generalPrevention": ["Plant famous Konkan Wal, Phule Wal varieties.", "Spray neem oil for sucking pests."]
    },
    {
        "id": "french-bean",
        "name": "French Bean (Snap Bean)",
        "localName": "फरसबी / श्रावण घेवडा (Pharasbi / Shravan Ghevda)",
        "scientificName": "Phaseolus vulgaris var. humilis",
        "category": "Pulses & Legumes",
        "avatarEmoji": "🫛",
        "season": "Kharif, Rabi & Zaid",
        "maharashtraRegion": "Pune, Satara (Wai), Nashik, Kolhapur vegetable tracts",
        "description": "Crisp, tender stringless green pods highly prized in premium urban vegetable markets.",
        "optimalTemp": "15°C - 25°C",
        "waterRequirement": "350 - 450 mm; regular light irrigations.",
        "soilPreference": "Friable sandy loam rich in organic compost, pH 6.0 - 6.8.",
        "growthStages": [
            {"stage": "Vegetative", "days": "Days 1-25", "description": "Compact bush or climbing habit."},
            {"stage": "Flowering", "days": "Days 26-40", "description": "Self-pollinating blossoms."},
            {"stage": "Pod Picking", "days": "Days 41-65", "description": "Harvest pods when tender and snap easily before seeds bulge."}
        ],
        "commonDiseases": [{"name": "Rust", "symptoms": "Reddish pustules on leaves.", "riskPeriod": "High humidity."}],
        "commonPests": ["Whitefly", "Leafhopper", "Aphid"],
        "generalPrevention": ["Grow Contender, Phule Suyash varieties.", "Provide regular drip irrigation."]
    },
    {
        "id": "winged-bean",
        "name": "Winged Bean (Goa Bean)",
        "localName": "चौधारी घेवडा (Chaudhari Ghevda)",
        "scientificName": "Psophocarpus tetragonolobus",
        "category": "Pulses & Legumes",
        "avatarEmoji": "🫛",
        "season": "Kharif",
        "maharashtraRegion": "Konkan, Western Ghats, Goa border",
        "description": "All-edible miracle plant: tender four-winged pods, leaves, flowers, seeds, and tuberous roots are all protein-rich.",
        "optimalTemp": "22°C - 32°C",
        "waterRequirement": "600 - 800 mm.",
        "soilPreference": "Moist laterite and alluvial soils.",
        "growthStages": [
            {"stage": "Vegetative", "days": "Days 1-45", "description": "Strong vine requiring trellising."},
            {"stage": "Flowering", "days": "Days 46-75", "description": "Sky-blue edible flowers."},
            {"stage": "Pod Harvest", "days": "Days 76-120", "description": "Four-angled frilled pods picked tender."}
        ],
        "commonDiseases": [{"name": "Collar Rot", "symptoms": "Damping off in waterlogged beds.", "riskPeriod": "Heavy rains."}],
        "commonPests": ["Caterpillars", "Mites"],
        "generalPrevention": ["Provide strong bamboo trellis support.", "Mulch base to retain soil moisture."]
    },
    {
        "id": "lima-bean",
        "name": "Lima Bean (Butter Bean)",
        "localName": "डबल बी / लीमा बीन (Double Bee)",
        "scientificName": "Phaseolus lunatus",
        "category": "Pulses & Legumes",
        "avatarEmoji": "🫘",
        "season": "Rabi",
        "maharashtraRegion": "Mahabaleshwar, Panchgani, Satara cool hill tracts",
        "description": "Large buttery flat beans cultivated in cool Western Ghat hill slopes, famous specialty in Mahabaleshwar.",
        "optimalTemp": "15°C - 24°C",
        "waterRequirement": "400 - 550 mm.",
        "soilPreference": "Deep rich mountain loams.",
        "growthStages": [
            {"stage": "Vine Growth", "days": "Days 1-40", "description": "Perennial or annual vigorous vine."},
            {"stage": "Flowering", "days": "Days 41-70", "description": "White or violet flowers."},
            {"stage": "Pod Picking", "days": "Days 71-110", "description": "Large flat pods with creamy butter beans."}
        ],
        "commonDiseases": [{"name": "Downy Mildew", "symptoms": "White fungal patches on pods.", "riskPeriod": "Cold hill fog."}],
        "commonPests": ["Pod Borer", "Thrips"],
        "generalPrevention": ["Provide strong wire trellis.", "Harvest pods at mature green stage."]
    },
    {
        "id": "rice-bean",
        "name": "Rice Bean",
        "localName": "राईस बीन / नवरंगी डाळ (Navrangi Dal)",
        "scientificName": "Vigna umbellata",
        "category": "Pulses & Legumes",
        "avatarEmoji": "🫘",
        "season": "Kharif",
        "maharashtraRegion": "Tribal hill tracts of Vidarbha and Western Ghats, Northeast India",
        "description": "Climate-hardy underutilized legume immune to many diseases of common pulses, highly nutritious.",
        "optimalTemp": "20°C - 30°C",
        "waterRequirement": "400 - 600 mm.",
        "soilPreference": "Acidic and poor mountain soils.",
        "growthStages": [
            {"stage": "Vegetative", "days": "Days 1-40", "description": "Twining vine with yellow flowers."},
            {"stage": "Pod Setting", "days": "Days 41-75", "description": "Slender cylindrical pods."},
            {"stage": "Harvest", "days": "Days 76-115", "description": "Small oblong colored seeds."}
        ],
        "commonDiseases": [{"name": "Cercospora Leaf Spot", "symptoms": "Brown leaf spots.", "riskPeriod": "Humid periods."}],
        "commonPests": ["Aphids", "Blister Beetle"],
        "generalPrevention": ["Grown without chemical pesticides in tribal eco-farms."]
    }
]

print(f"Pulses loaded: {len(PULSES)}")
