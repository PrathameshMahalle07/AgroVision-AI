# -*- coding: utf-8 -*-
"""
Appends Oilseeds, Cash crops, Fruits, Vegetables, Spices, Floriculture, Medicinal, and Plantation crops.
"""

OILSEEDS = [
    {
        "id": "groundnut-peanut",
        "name": "Groundnut (Peanut)",
        "localName": "भुईमूग / शेंगदाणा (Bhuimug / Shengdana)",
        "scientificName": "Arachis hypogaea",
        "category": "Oilseeds",
        "avatarEmoji": "🥜",
        "season": "Kharif & Summer",
        "maharashtraRegion": "Western Maharashtra (Kolhapur, Satara, Sangli, Pune), Khandesh (Dhule, Jalgaon), Marathwada",
        "description": "Premier edible oilseed and protein food of Maharashtra. Geocarpic crop where flowers bloom above ground and pegs penetrate soil to form subterranean pods.",
        "optimalTemp": "25°C - 30°C",
        "waterRequirement": "500 - 650 mm; critical water demand during flowering and peg penetration.",
        "soilPreference": "Light sandy loam, well-drained friable red/black soils rich in calcium, pH 6.0 - 7.5.",
        "growthStages": [
            {"stage": "Emergence & Branching", "days": "Days 1-25", "description": "Rapid seedling emergence and lateral branching."},
            {"stage": "Flowering & Pegging", "days": "Days 26-50", "description": "Yellow self-pollinated flowers; fertilized gynophore (peg) grows geotropically into soil."},
            {"stage": "Pod Development", "days": "Days 51-85", "description": "Underground pod expansion; gypsum application ensures plump shells."},
            {"stage": "Pod Maturity & Harvest", "days": "Days 86-115", "description": "Internal pod shell displays dark brown reticulation; harvested by vine pullers."}
        ],
        "commonDiseases": [
            {"name": "Tikka Disease / Leaf Spot (Cercospora arachidicola)", "symptoms": "Circular dark brown spots with prominent yellow halos on upper leaf surface.", "riskPeriod": "Warm, humid weather with prolonged leaf wetness (25-30°C)."},
            {"name": "Groundnut Rust (Puccinia arachidis)", "symptoms": "Orange-brown pustules on leaf undersides causing severe defoliation.", "riskPeriod": "High humidity and continuous cloudy monsoon spells."},
            {"name": "Collar Rot (Aspergillus niger)", "symptoms": "Black sooty fungal mass on collar region leading to seedling damping off.", "riskPeriod": "High soil temperatures at sowing."}
        ],
        "commonPests": ["Groundnut Leaf Miner", "White Grub (Holotrichia consanguinea)", "Spodoptera litura", "Aphids", "Thrips"],
        "generalPrevention": [
            "Apply Gypsum @ 500 kg/ha at pegging (40-45 days) to ensure calcium for pod shell formation.",
            "Treat seed with Trichoderma viride @ 5g/kg + Imidacloprid @ 2ml/kg.",
            "Use high-yielding university varieties: Phule Unnati, JL-24 (Phule Pragati), TAG-24, or TG-37A.",
            "Install pheromone traps for Spodoptera and light traps for White grub beetles after first rains."
        ]
    },
    {
        "id": "mustard-sarson",
        "name": "Mustard (Rapeseed / Sarson)",
        "localName": "मोहरी / राई / सरसो (Mohari / Sarson)",
        "scientificName": "Brassica juncea",
        "category": "Oilseeds",
        "avatarEmoji": "🌼",
        "season": "Rabi (Winter)",
        "maharashtraRegion": "Vidarbha, Khandesh, North Maharashtra, Rajasthan & MP border tracts",
        "description": "Important winter oilseed yielding pungent cooking oil and nutrient-dense oilcake for dairy cattle.",
        "optimalTemp": "15°C - 25°C",
        "waterRequirement": "250 - 350 mm; requires 2-3 light irrigations.",
        "soilPreference": "Light to heavy loam with good drainage, pH 6.0 - 7.5.",
        "growthStages": [
            {"stage": "Rosette & Vegetative", "days": "Days 1-35", "description": "Broad radical leaves form dense ground rosette."},
            {"stage": "Bolting & Flowering", "days": "Days 36-65", "description": "Central flower stalk bolts into golden yellow blossoms."},
            {"stage": "Siliqua (Pod) Formation", "days": "Days 66-95", "description": "Slender beaked pods (siliquae) develop containing tiny round seeds."},
            {"stage": "Maturity", "days": "Days 96-125", "description": "Pods turn straw-yellow; harvested before shattering."}
        ],
        "commonDiseases": [
            {"name": "White Rust (Albugo candida)", "symptoms": "White porcelain-like blisters on leaf undersides and swollen staghead floral malformations.", "riskPeriod": "Cool, humid morning fog."},
            {"name": "Alternaria Blight", "symptoms": "Concentric dark brown target spots on leaves and siliquae.", "riskPeriod": "Warm humid spells after flowering."}
        ],
        "commonPests": ["Mustard Aphid (Lipaphis erysimi)", "Painted Bug", "Sawfly"],
        "generalPrevention": [
            "Sow early in October to escape severe aphid infestation in December-January.",
            "Spray Oxydemeton-methyl or Dimethoate 30 EC @ 1ml/L at first aphid appearance on inflorescence.",
            "Use resistant varieties: Pusa Bold, NRCHB-101, Varuna, or Bio-902 (Pusa Jaikisan)."
        ]
    },
    {
        "id": "sunflower",
        "name": "Sunflower",
        "localName": "सूर्यफूल (Suryaphul)",
        "scientificName": "Helianthus annuus",
        "category": "Oilseeds",
        "avatarEmoji": "🌻",
        "season": "Kharif, Rabi & Summer",
        "maharashtraRegion": "Marathwada (Beed, Latur, Osmanabad), Solapur, Ahmednagar, Vidarbha",
        "description": "Heliotropic oilseed with premium heart-healthy polyunsaturated fatty acids (PUFA). Photo-insensitive crop suitable for any season in Maharashtra.",
        "optimalTemp": "20°C - 30°C",
        "waterRequirement": "450 - 600 mm; critical at button stage, flowering, and seed development.",
        "soilPreference": "Deep, fertile black clay soils or fertile loams, pH 6.5 - 8.0.",
        "growthStages": [
            {"stage": "Emergence & Vegetative", "days": "Days 1-30", "description": "Rapid broad-leaf expansion and deep taproot development."},
            {"stage": "Star / Button Stage", "days": "Days 31-50", "description": "Inflorescence bud appears at stem apex; heliotropism active."},
            {"stage": "Flowering & Pollination", "days": "Days 51-70", "description": "Ray florets and disk florets open; honeybee pollination essential."},
            {"stage": "Seed Filling & Capitulum Bending", "days": "Days 71-95", "description": "Back of flower head turns lemon yellow; achenes harden."}
        ],
        "commonDiseases": [
            {"name": "Alternaria Leaf Blight (Alternaria helianthi)", "symptoms": "Dark brown circular spots coalescing into large necrotic blights.", "riskPeriod": "Cloudy humid rainy weather."},
            {"name": "Necrosis Disease (Tobamovirus)", "symptoms": "Systemic mosaic, leaf malformation, and necrotic streaks on stem and capitulum; thrips vector.", "riskPeriod": "Hot dry spells with high thrips activity."},
            {"name": "Head Rot (Rhizopus stolonifer)", "symptoms": "Soft, pulpy brown rotting of capitulum covered with fungal whiskers.", "riskPeriod": "Damage by birds or earhead borers during rain."}
        ],
        "commonPests": ["Capitulum Borer (Helicoverpa armigera)", "Thrips", "Jassids", "Leaf Eating Caterpillar"],
        "generalPrevention": [
            "Maintain 3-5 honeybee boxes per hectare to double pollination and prevent hollow seed formation.",
            "Spray Mancozeb @ 2.5g/L or Propiconazole @ 1ml/L at initiation of Alternaria spots.",
            "Use popular hybrids: Phule Bhaskar, KBSH-1, MSFH-17, or DRSH-1."
        ]
    },
    {
        "id": "safflower-kardai",
        "name": "Safflower (Kardai)",
        "localName": "करडई (Kardai)",
        "scientificName": "Carthamus tinctorius",
        "category": "Oilseeds",
        "avatarEmoji": "🌾",
        "season": "Rabi (Winter)",
        "maharashtraRegion": "Marathwada (Osmanabad, Beed, Latur), Solapur, Ahmednagar, Western Maharashtra",
        "description": "Traditional drought-resilient spiny oilseed of Maharashtra black soils. Known for cold-pressed cardi-oil (high linoleic acid) and tender winter vegetable greens.",
        "optimalTemp": "18°C - 28°C",
        "waterRequirement": "250 - 350 mm; extremely deep taproot extracts moisture from subsoil.",
        "soilPreference": "Deep black soils (Vertisols) with high water retention capacity.",
        "growthStages": [
            {"stage": "Rosette Stage", "days": "Days 1-40", "description": "Slow prostrate growth while deep taproot penetrates 2-3 meters into subsoil."},
            {"stage": "Stem Elongation & Branching", "days": "Days 41-75", "description": "Stiff spiny stems and branches form."},
            {"stage": "Capitulum Flowering", "days": "Days 76-105", "description": "Vibrant orange-yellow florets bloom at branch tips."},
            {"stage": "Seed Maturation", "days": "Days 106-130", "description": "White shiny achenes mature inside spiny involucral bracts."}
        ],
        "commonDiseases": [
            {"name": "Alternaria Leaf Spot", "symptoms": "Concentric brown spots with chlorotic haloes on leaves.", "riskPeriod": "Post-flowering winter humidity."},
            {"name": "Safflower Wilt (Fusarium oxysporum)", "symptoms": "Unilateral wilting and brown vascular discoloration.", "riskPeriod": "Damp soil during vegetative rosette phase."}
        ],
        "commonPests": ["Safflower Aphid (Uroleucon carthami)", "Gram Pod Borer"],
        "generalPrevention": [
            "Sow in late September or early October to escape aphid explosion in peak winter.",
            "Use aphid-tolerant varieties like Phule Kusuma, Bhima, or NARI-6.",
            "Spray Thiamethoxam 25 WG @ 2g/10L at initiation of aphid colonies."
        ]
    },
    {
        "id": "sesame-til",
        "name": "Sesame (Til)",
        "localName": "तीळ (Til)",
        "scientificName": "Sesamum indicum",
        "category": "Oilseeds",
        "avatarEmoji": "🌱",
        "season": "Kharif & Summer",
        "maharashtraRegion": "Khandesh (Jalgaon, Dhule), Vidarbha, Solapur, Marathwada",
        "description": "Queen of oilseeds; ancient oil-bearing plant rich in sesamin antioxidants and calcium. Sacred ingredient in Makar Sankranti Tilgul.",
        "optimalTemp": "25°C - 35°C",
        "waterRequirement": "300 - 400 mm; sensitive to waterlogging.",
        "soilPreference": "Well-drained sandy loam or light black soil, pH 6.0 - 7.5.",
        "growthStages": [
            {"stage": "Vegetative", "days": "Days 1-30", "description": "Erect branching and opposite leaves."},
            {"stage": "Flowering", "days": "Days 31-55", "description": "Bell-shaped white to pale pink flowers open in leaf axils."},
            {"stage": "Capsule Formation", "days": "Days 56-80", "description": "Four-grooved erect capsules develop containing rows of seeds."},
            {"stage": "Maturity", "days": "Days 81-100", "description": "Bottom capsules turn yellow-brown; cut before dehiscence."}
        ],
        "commonDiseases": [
            {"name": "Phyllody (Phytoplasma)", "symptoms": "Floral parts transform into green leafy structures; plant becomes sterile witches' broom; leafhopper vector.", "riskPeriod": "Continuous warm weather with leafhopper activity."},
            {"name": "Bacterial Blight", "symptoms": "Angular water-soaked spots on foliage.", "riskPeriod": "Wind-driven monsoon showers."}
        ],
        "commonPests": ["Til Hawk Moth (Sphingid caterpillar)", "Antigastra Gall Fly / Shoot Webbed Borer"],
        "generalPrevention": [
            "Use varieties like Tapi (JLT-408), Phule Til-1, or RT-351.",
            "Control leafhopper vector using Imidacloprid @ 3ml/10L to prevent incurable Phyllody.",
            "Intercrop with green gram or moth bean."
        ]
    },
    {
        "id": "castor-erandi",
        "name": "Castor",
        "localName": "एरंडी (Erandi)",
        "scientificName": "Ricinus communis",
        "category": "Oilseeds",
        "avatarEmoji": "🌿",
        "season": "Kharif",
        "maharashtraRegion": "Marathwada, Vidarbha, Khandesh, Gujarat border tracts",
        "description": "High-value non-edible industrial oilseed producing ricinoleic acid used for high-grade aviation lubricants, cosmetics, and biodiesel.",
        "optimalTemp": "25°C - 35°C",
        "waterRequirement": "400 - 600 mm; hardy taproot system.",
        "soilPreference": "Deep loam to gravelly light soil with good internal drainage.",
        "growthStages": [
            {"stage": "Seedling", "days": "Days 1-30", "description": "Large palmate leaves expand."},
            {"stage": "Primary Spike Flowering", "days": "Days 31-70", "description": "Monoecious flowers on terminal raceme (female flowers on upper half, male below)."},
            {"stage": "Capsule Setting & Spikes", "days": "Days 71-120", "description": "Spiny capsules form on multiple spike orders."},
            {"stage": "Harvesting", "days": "Days 121-180", "description": "Spikes picked as capsules turn yellowish-brown."}
        ],
        "commonDiseases": [
            {"name": "Castor Wilt (Fusarium oxysporum f. sp. ricini)", "symptoms": "Yellowing and wilting of plants with internal stem vascular browning.", "riskPeriod": "Flowering stage during soil moisture stress."},
            {"name": "Botrytis Gray Mold", "symptoms": "Woolly gray fungal mold rotting entire spikes during rain.", "riskPeriod": "Continuous humid overcast monsoon weather."}
        ],
        "commonPests": ["Castor Semilooper (Achaea janata)", "Shoot & Capsule Borer (Conogethes punctiferalis)", "Tobacco Caterpillar"],
        "generalPrevention": [
            "Use wilt-resistant hybrids: DCH-177, GCH-7, or Phule Castor-1.",
            "Install bird perches @ 25/ha to encourage mynas and crows feeding on semiloopers.",
            "Handpick early gregarious egg masses and young semilooper clusters."
        ]
    },
    {
        "id": "linseed-flaxseed-javas",
        "name": "Linseed / Flaxseed (Javas)",
        "localName": "जवस / अळशी (Javas / Alsi)",
        "scientificName": "Linum usitatissimum",
        "category": "Oilseeds",
        "avatarEmoji": "🌱",
        "season": "Rabi (Winter)",
        "maharashtraRegion": "Vidarbha (Chandrapur, Bhandara, Nagpur), Marathwada, Central India",
        "description": "Ancient oilseed celebrated as modern superfood rich in Omega-3 (alpha-linolenic acid), lignans, and dietary fiber. Famous for Maharashtrian Javas Chutney.",
        "optimalTemp": "15°C - 25°C",
        "waterRequirement": "250 - 350 mm.",
        "soilPreference": "Deep black moisture-retentive soils (Vertisols) or clay loams.",
        "growthStages": [
            {"stage": "Vegetative", "days": "Days 1-35", "description": "Slender fibrous erect stems with linear leaves."},
            {"stage": "Flowering", "days": "Days 36-65", "description": "Sky-blue to violet flowers open in morning sunshine."},
            {"stage": "Boll Formation", "days": "Days 66-95", "description": "Globular bolls (capsules) develop containing 10 flat shiny seeds."},
            {"stage": "Maturity", "days": "Days 96-120", "description": "Bolls turn golden brown; rustle when shaken."}
        ],
        "commonDiseases": [
            {"name": "Linseed Rust (Melampsora lini)", "symptoms": "Bright orange-yellow uredial pustules on leaves and stems, later turning glossy black.", "riskPeriod": "Humid cool winter weather."},
            {"name": "Fusarium Wilt", "symptoms": "Drooping stem tips (shepherd's crook) and root death.", "riskPeriod": "Warm soils."}
        ],
        "commonPests": ["Linseed Gall Midge (Dasyneura lini)", "Semilooper"],
        "generalPrevention": [
            "Use rust-resistant university varieties: PKV NL-260, Meera, Sharda, or JLS-9.",
            "Seed treatment with Trichoderma viride @ 5g/kg."
        ]
    },
    {
        "id": "niger-karale",
        "name": "Niger Seed (Karale)",
        "localName": "कारळे / खुरसणी (Karale / Khursani)",
        "scientificName": "Guizotia abyssinica",
        "category": "Oilseeds",
        "avatarEmoji": "🌼",
        "season": "Late Kharif",
        "maharashtraRegion": "Tribal hill zones of Nashik (Igatpuri, Surgana), Nandurbar, Thane, Western Ghats",
        "description": "Hardy oilseed grown on impoverished tribal hill slopes. Core ingredient of authentic fiery Maharashtrian Karale Chutney.",
        "optimalTemp": "18°C - 28°C",
        "waterRequirement": "300 - 450 mm; thrives on residual monsoon moisture.",
        "soilPreference": "Light gravelly laterite, poor stony or acidic soils.",
        "growthStages": [
            {"stage": "Vegetative", "days": "Days 1-35", "description": "Dense semi-bush with yellow composite flowers."},
            {"stage": "Flowering", "days": "Days 36-70", "description": "Bright golden daisy-like heads attract bees."},
            {"stage": "Seed Hardening & Harvest", "days": "Days 71-105", "description": "Small black glossy seeds fill capitula."}
        ],
        "commonDiseases": [{"name": "Cercospora Leaf Spot", "symptoms": "Small brown spots on foliage.", "riskPeriod": "Post-monsoon mists."}],
        "commonPests": ["Semilooper", "Capsule Fly"],
        "generalPrevention": ["Use improved varieties: Phule Karale, IGP-76, RCR-18.", "Cultivated naturally without chemical sprays."]
    }
]

print(f"Oilseeds loaded: {len(OILSEEDS)}")
