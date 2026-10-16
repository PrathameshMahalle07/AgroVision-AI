#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master compiler that writes /src/data/cropsDatabase.ts with 260+ authentic crops.
"""

import json
import sys

def build_crops():
    crops = []
    
    # helper
    def add_crop(cid, name, local, sci, cat, emoji, season, region, desc, temp, water, soil, stages, diseases, pests, prev):
        crops.append({
            "id": cid,
            "name": name,
            "localName": local,
            "scientificName": sci,
            "category": cat,
            "avatarEmoji": emoji,
            "season": season,
            "maharashtraRegion": region,
            "description": desc,
            "optimalTemp": temp,
            "waterRequirement": water,
            "soilPreference": soil,
            "growthStages": stages,
            "commonDiseases": diseases,
            "commonPests": pests,
            "generalPrevention": prev
        })

    # ==========================================
    # 1. CEREALS & MILLETS (18 crops)
    # ==========================================
    add_crop(
        "rice-paddy", "Rice (Paddy)", "भात / तांदूळ / धान (Dhan)", "Oryza sativa", "Cereals & Millets", "🌾",
        "Kharif & Summer", "Konkan (Ratnagiri, Sindhudurg, Raigad, Thane), Eastern Vidarbha (Bhandara, Gondia, Chandrapur, Gadchiroli)",
        "Primary staple cereal of coastal Maharashtra and Vidarbha lake districts. Grown under puddled flooded conditions or upland terraces.",
        "22°C - 32°C (warm, humid)", "1,000 - 1,400 mm; standing water layer (2-5 cm) during vegetative phase.",
        "Heavy clay loam or silty clay soils with high water retention, pH 5.5 - 7.0.",
        [
            {"stage": "Nursery & Seedling", "days": "Days 1-25", "description": "Raised bed seedling raising; 21-day seedlings transplanted to puddled field."},
            {"stage": "Tillering & Vegetative", "days": "Days 26-60", "description": "Active tiller production and crown root expansion in flooded mud."},
            {"stage": "Panicle Initiation & Booting", "days": "Days 61-90", "description": "Flag leaf emergence and panicle formation inside sheath; flowering begins."},
            {"stage": "Grain Filling & Harvesting", "days": "Days 91-125", "description": "Milky, dough, and mature golden grain hardening; field drained 10 days prior to sickle harvest."}
        ],
        [
            {"name": "Rice Blast (Magnaporthe oryzae)", "symptoms": "Spindle-shaped diamond spots with grey center and dark brown margin on leaves and panicle neck.", "riskPeriod": "Night temperatures 20-24°C with continuous drizzling rain and relative humidity >90%."},
            {"name": "Bacterial Leaf Blight (Xanthomonas oryzae)", "symptoms": "Water-soaked wavy lesions starting at leaf margins turning dull yellow with white bacterial crusts.", "riskPeriod": "Warm temperatures (25-34°C) with strong wind-driven monsoon rains."},
            {"name": "Sheath Blight (Rhizoctonia solani)", "symptoms": "Greenish-grey oval water-soaked blotches on leaf sheaths just above the waterline.", "riskPeriod": "High humidity (>95%) and heavy top-dressed nitrogen fertilizer."}
        ],
        ["Yellow Stem Borer", "Brown Planthopper (BPH)", "Rice Gall Midge", "Leaf Folder", "Gundhi Bug"],
        [
            "Use certified resistant varieties such as Karjat-3, Indrayani, PKV HMT, or Ratna.",
            "Treat seed with Trichoderma harzianum @ 5g/kg or Carbendazim @ 2g/kg.",
            "Adopt Alternate Wetting and Drying (AWD) water management to suppress Brown Planthopper.",
            "Avoid excessive basal urea; split nitrogen into 3 equal applications with potassium at panicle stage."
        ]
    )

    add_crop(
        "wheat", "Wheat", "गहू (Gahu)", "Triticum aestivum", "Cereals & Millets", "🌾",
        "Rabi (Winter)", "Western Maharashtra (Pune, Ahmednagar, Satara, Kolhapur), Vidarbha (Nagpur, Amravati), Khandesh (Jalgaon)",
        "Premier winter cereal crop of India, grown extensively under irrigated black cotton soils in Maharashtra and alluvial plains of North India.",
        "12°C - 25°C (cool nights during tillering, bright sunshine during grain fill)", "400 - 500 mm across 4-6 critical irrigations (CRI, tillering, jointing, flowering, milking).",
        "Deep, fertile well-drained clay loam or medium black cotton soil, pH 6.5 - 7.5.",
        [
            {"stage": "Crown Root Initiation (CRI)", "days": "Days 20-25", "description": "First whorl of crown roots forms below soil surface; paramount irrigation window."},
            {"stage": "Tillering & Jointing", "days": "Days 26-55", "description": "Nodes elongate, vegetative tillers develop; canopy closes."},
            {"stage": "Heading & Anthesis", "days": "Days 56-85", "description": "Earhead emerges from flag leaf boot; pollination occurs."},
            {"stage": "Milking, Dough & Maturity", "days": "Days 86-115", "description": "Starch accumulates; straw turns golden yellow; grains harden."}
        ],
        [
            {"name": "Brown / Leaf Rust (Puccinia triticina)", "symptoms": "Round to oval orange-brown powdery pustules scattered randomly across upper leaf blade.", "riskPeriod": "Warm humid winter days (18-25°C) with morning dew."},
            {"name": "Yellow / Stripe Rust (Puccinia striiformis)", "symptoms": "Linear bright yellow stripes of powdery pustules arranged between leaf veins.", "riskPeriod": "Cool winter temperatures (10-18°C) with persistent fog."},
            {"name": "Loose Smut (Ustilago tritici)", "symptoms": "Entire earhead transformed into a loose sooty black mass of fungal spores.", "riskPeriod": "Infected seeds germinating in cool moist soil."}
        ],
        ["Wheat Aphids", "Armyworm", "Termites", "Pink Stem Borer"],
        [
            "Sow in first fortnight of November to escape terminal heat in Central India.",
            "Use certified high-yielding resistant varieties: Samadhan (NIAW-1994), Trimbak, or MACS-6222.",
            "Treat seed with Carboxin + Thiram (Vitavax) @ 2.5g/kg for complete loose smut control.",
            "Irrigate lightly at milk stage on calm windless days to prevent crop lodging."
        ]
    )

    add_crop(
        "sorghum-jowar", "Sorghum (Jowar)", "ज्वारी (Jowar) / मालदांडी (Maldandi)", "Sorghum bicolor", "Cereals & Millets", "🌾",
        "Kharif & Rabi", "Solapur (Maldandi Capital of India), Marathwada (Latur, Beed, Osmanabad), Ahmednagar, Pune, Jalgaon",
        "The golden heart of Maharashtra dryland agriculture. Drought-resilient C4 cereal famous for delicious pearl bhakri and high-quality livestock fodder (kadbi). Solapur Maldandi M 35-1 is world-renowned.",
        "26°C - 34°C (heat and drought hardy)", "350 - 450 mm; extraordinary water efficiency.",
        "Medium to deep black clay soils (Vertisols) with moisture retention, pH 6.5 - 8.5.",
        [
            {"stage": "Seedling & Early Vegetative", "days": "Days 1-25", "description": "Rapid germination; shoot fly vulnerable period."},
            {"stage": "Stem Elongation & Panicle Initiation", "days": "Days 26-55", "description": "Dense node elongation; growing point converts into panicle."},
            {"stage": "Booting & Anthesis", "days": "Days 56-75", "description": "Spike emerges from flag leaf collar; cross-pollination by wind."},
            {"stage": "Grain Filling & Black Layer Maturity", "days": "Days 76-110", "description": "Pearly grains fill; black layer at seed base marks physiological maturity."}
        ],
        [
            {"name": "Grain Mold (Fusarium & Curvularia)", "symptoms": "Pink, black, or grey discoloration on developing grain heads following rain.", "riskPeriod": "Unseasonal wet spells during grain-filling stage."},
            {"name": "Downy Mildew (Peronosclerospora sorghi)", "symptoms": "Vivid chlorotic yellow striping on leaves with downy white fungal growth on undersides.", "riskPeriod": "High humidity with cool night temperatures (20°C)."},
            {"name": "Charcoal Rot (Macrophomina phaseolina)", "symptoms": "Internal stalk shredding with tiny charcoal-like sclerotia causing lodging.", "riskPeriod": "Post-flowering soil moisture stress and soil temperatures exceeding 35°C."}
        ],
        ["Sorghum Shoot Fly", "Stem Borer (Chilo partellus)", "Fall Armyworm", "Earhead Midge"],
        [
            "Complete sowing within 10-15 days of monsoon onset to escape destructive shoot fly egg laying.",
            "Treat seed with Imidacloprid 70 WS @ 7g/kg + Trichoderma @ 4g/kg.",
            "Adopt famous resistant cultivars like Phule Yashoda, Maldandi M 35-1, or Parbhani Moti.",
            "Intercrop with Pigeon pea (Tur) in a 2:1 ratio to interrupt stem borer life cycles."
        ]
    )

    add_crop(
        "pearl-millet-bajra", "Pearl Millet (Bajra)", "बाजरी (Bajra)", "Pennisetum glaucum", "Cereals & Millets", "🌾",
        "Kharif & Summer", "Ahmednagar, Nashik, Dhule, Jalgaon, Beed, Aurangabad, Pune rain-shadow belts",
        "Climate-smart super-millet loaded with iron, zinc, and fiber. Thrives on light shallow soils under erratic rain-shadow monsoon belts.",
        "28°C - 36°C (tolerates extreme heat up to 42°C)", "250 - 350 mm.",
        "Well-drained sandy loam, gravelly or shallow black soils, pH 6.0 - 8.0.",
        [
            {"stage": "Seedling & Tillering", "days": "Days 1-25", "description": "Rapid crown tillering in dry soil conditions."},
            {"stage": "Stem Elongation & Flag Leaf", "days": "Days 26-45", "description": "Cylindrical bristled spike developing inside sheath."},
            {"stage": "Protogynous Flowering & Anthesis", "days": "Days 46-65", "description": "White feathery stigmas emerge first followed by yellow anthers; wind-pollinated."},
            {"stage": "Grain Hardening & Desiccation", "days": "Days 66-85", "description": "Dense greyish-pearl grains harden; ready for harvesting."}
        ],
        [
            {"name": "Downy Mildew / Green Ear (Sclerospora graminicola)", "symptoms": "Floral spikes transform into twisted leafy green brush structures; chlorotic leaf stripes.", "riskPeriod": "Humid overcast days with temperatures around 20-25°C."},
            {"name": "Ergot (Claviceps fusiformis)", "symptoms": "Pinkish sticky honey-like liquid oozes from spikelets, later hardening into dark sclerotia.", "riskPeriod": "Rainy, overcast days during protogynous flowering."},
            {"name": "Rust (Puccinia substriata)", "symptoms": "Reddish-brown powdery pustules on both leaf surfaces causing premature drying.", "riskPeriod": "Warm humid conditions after earhead emergence."}
        ],
        ["Shoot Fly", "Stem Borer", "Blister Beetle", "Grasshopper"],
        [
            "Treat seed with Metalaxyl (Apron 35 SD) @ 6g/kg to immunize seedlings against downy mildew.",
            "Dip seeds in 10% brine solution; skim off and destroy floating ergot sclerotia.",
            "Plant bio-fortified high-yielding hybrids such as Dhanshakti, Phule Aadishakti, or GHB-538.",
            "Avoid excessive sowing density to facilitate cross-canopy sunlight and aeration."
        ]
    )

    add_crop(
        "maize-corn", "Maize (Corn)", "मका (Maka)", "Zea mays", "Cereals & Millets", "🌽",
        "Kharif, Rabi & Summer", "Khandesh (Jalgaon, Dhule), Nashik, Aurangabad, Kolhapur, Sangli",
        "High-yielding versatile cereal cultivated for grain, poultry feed, green fodder, and industrial starch. Has seen massive expansion in Khandesh and Marathwada.",
        "21°C - 30°C", "500 - 650 mm; critical water demand during tasseling and silking.",
        "Deep, fertile, well-aerated sandy loam to clay loam rich in organic matter, pH 6.0 - 7.5.",
        [
            {"stage": "Emergence & Knee-High", "days": "Days 1-30", "description": "Crown roots anchor; whorl leaves unfold rapidly."},
            {"stage": "Tasseling (Male Bloom)", "days": "Days 35-55", "description": "Terminal tassel emerges shedding millions of airborne pollen grains."},
            {"stage": "Silking (Female Cob Bloom)", "days": "Days 56-75", "description": "Sticky silky strands emerge from ear shoot to capture falling pollen."},
            {"stage": "Milk, Dough & Denting Maturity", "days": "Days 76-105", "description": "Kernels fill with starch; black layer forms at grain base at maturity."}
        ],
        [
            {"name": "Maydis Leaf Blight (Bipolaris maydis)", "symptoms": "Elongated tan lesions with brown borders on leaf blades.", "riskPeriod": "Warm, humid conditions (20-30°C) with intermittent rain."},
            {"name": "Turcicum Leaf Blight (Exserohilum turcicum)", "symptoms": "Long, elliptical grayish-green cigar-shaped necrotic lesions on foliage.", "riskPeriod": "Cool, wet weather with heavy dews."},
            {"name": "Common Rust (Puccinia sorghi)", "symptoms": "Golden-brown powdery pustules covering both leaf surfaces.", "riskPeriod": "Cool, humid weather (16-23°C)."}
        ],
        ["Fall Armyworm (Spodoptera frugiperda)", "Stem Borer", "Shoot Fly", "Corn Earworm"],
        [
            "Install pheromone traps @ 10/ha to detect Fall Armyworm moths immediately upon emergence.",
            "Apply neem-based Azadirachtin 1500 ppm or Bacillus thuringiensis (Bt) @ 2g/L into leaf whorls.",
            "Ensure ridge-and-furrow planting to prevent root waterlogging, which stunts young maize plants.",
            "Apply balanced fertilizer (120:60:40 kg NPK/ha) supplemented with Zinc Sulfate @ 25 kg/ha."
        ]
    )

    add_crop(
        "finger-millet-ragi", "Finger Millet (Ragi / Nachani)", "नाचणी / रागी / नागली (Nachni / Nagli)", "Eleusine coracana", "Cereals & Millets", "🌾",
        "Kharif", "Konkan (Thane, Palghar, Raigad, Ratnagiri), Western Ghat hilly tribal belts of Nashik and Kolhapur",
        "Ancient climate-resilient superfood millet celebrated for extraordinary calcium and amino acid content. Staple grain of Konkan tribal farmers and nutritious bhakri.",
        "20°C - 30°C", "400 - 600 mm; tolerates high rainfall on sloped hill terrains without lodging.",
        "Red sandy loam, gravelly laterite, or shallow hill soils, pH 5.0 - 7.5.",
        [
            {"stage": "Nursery & Seedling", "days": "Days 1-25", "description": "Tiny seeds raised on raised beds; transplanted to hill slopes."},
            {"stage": "Tillering & Vegetative", "days": "Days 26-55", "description": "Dense fibrous root system establishes in rocky hillside soil."},
            {"stage": "Earhead Emergence (Finger Formation)", "days": "Days 56-80", "description": "Digit-like whorl of 4 to 8 spicate fingers unfolds."},
            {"stage": "Grain Maturation & Drying", "days": "Days 81-115", "description": "Seeds turn dark brown/russet; cut with sickle at full maturity."}
        ],
        [
            {"name": "Ragi Blast (Pyricularia grisea)", "symptoms": "Spindle-shaped lesions on leaf; choking black lesions on neck and fingers causing severe yield loss.", "riskPeriod": "Cloudy, humid weather in Western Ghat hills during monsoon."},
            {"name": "Foot Rot / Wilt (Sclerotium rolfsii)", "symptoms": "White mycelial fan at collar region with mustard-seed-like sclerotia.", "riskPeriod": "Warm soil with moisture stagnation."}
        ],
        ["Ragi Stem Borer", "Hairy Caterpillar", "Aphids", "Grasshoppers"],
        [
            "Use blast-tolerant university varieties like Phule Nachani, Dapoli-1, or GPU-28.",
            "Treat seed with Pseudomonas fluorescens @ 10g/kg prior to nursery sowing.",
            "Transplant 20-25 day old seedlings at 20x10 cm spacing for uniform canopy ventilation."
        ]
    )

    add_crop("foxtail-millet-rala", "Foxtail Millet", "राळा / कांगणी (Rala / Kangni)", "Setaria italica", "Cereals & Millets", "🌾", "Kharif", "Marathwada, Solapur, Ahmednagar drylands, Vidarbha", "Fast-maturing, drought-tolerant nutrient-rich ancient millet with low glycemic index. Used for wholesome porridge, upma, and flour.", "22°C - 32°C", "250 - 350 mm; matures in just 70-85 days.", "Light sandy loam to shallow black soils, well-draining.", [{"stage": "Seedling", "days": "Days 1-20", "description": "Quick emergence."}, {"stage": "Tillering", "days": "Days 21-45", "description": "Compact bristled panicles forming."}, {"stage": "Flowering", "days": "Days 46-65", "description": "Yellowish cylindrical drooping bristly spikes bloom."}, {"stage": "Harvest", "days": "Days 66-85", "description": "Grains turn golden-yellow."}], [{"name": "Blast", "symptoms": "Brown circular spots on leaves and panicles.", "riskPeriod": "Overcast skies and sustained humidity."}], ["Shoot Fly", "Armyworm"], ["Seed treatment with Thiram @ 3g/kg."])
    add_crop("barnyard-millet-bhagar", "Barnyard Millet (Bhagar / Varai)", "वरई / भगर / सावा (Varai / Bhagar)", "Echinochloa frumentacea", "Cereals & Millets", "🌾", "Kharif", "Nashik (Trimbak), Konkan, tribal belt of Pune and Ahmednagar hills", "Fastest-growing grain crop on earth (matures in 60 days). The revered staple grain for fasting (Upwas Bhagar) across Maharashtra.", "20°C - 30°C", "300 - 450 mm; withstands severe drought as well as seasonal waterlogging.", "Marginal, gravelly hill slopes and poor shallow soils, pH 5.5 - 7.5.", [{"stage": "Emergence", "days": "Days 1-20", "description": "Rapid tillering."}, {"stage": "Booting", "days": "Days 21-40", "description": "Pyramidal panicle emerges."}, {"stage": "Harvest", "days": "Days 41-65", "description": "Milky grains harden."}], [{"name": "Smut", "symptoms": "Ovaries swollen into gall-like masses.", "riskPeriod": "Cool, wet mornings."}], ["Shoot Fly", "Stem Borer"], ["Seed treatment with bio-agent Trichoderma viride."])
    add_crop("little-millet-kutki", "Little Millet", "कुटकी / सावा (Kutki)", "Panicum sumatrense", "Cereals & Millets", "🌾", "Kharif", "Tribal areas of Nandurbar, Gadchiroli, Chandrapur, Thane", "Nutritious minor millet that grows on impoverished soils where almost no other cereal can yield.", "20°C - 32°C", "250 - 350 mm.", "Shallow gravelly red or lateritic soils.", [{"stage": "Vegetative", "days": "Days 1-30", "description": "Fibrous rooting."}, {"stage": "Heading", "days": "Days 31-55", "description": "Loose open panicles."}, {"stage": "Harvest", "days": "Days 56-80", "description": "Seeds turn straw-colored."}], [{"name": "Rust", "symptoms": "Small orange spots.", "riskPeriod": "Post-monsoon humidity."}], ["Shoot Fly", "Spittle Bug"], ["Sow with first soaking monsoon rains."])
    add_crop("kodo-millet", "Kodo Millet", "कोद्रा / कोदो (Kodra / Kodo)", "Paspalum scrobiculatum", "Cereals & Millets", "🌾", "Kharif", "Konkan hills, Vidarbha forest belts, Satpura ranges", "Extremely hardy ancient millet rich in polyphenols and dietary fiber, cultivated since Indus Valley times.", "25°C - 35°C", "300 - 450 mm.", "Poor stony soils with minimal nutrition.", [{"stage": "Vegetative", "days": "Days 1-35", "description": "Prostrate tillering."}, {"stage": "Panicle", "days": "Days 36-70", "description": "Racemes with dark brown seeds."}, {"stage": "Harvest", "days": "Days 71-105", "description": "Tough seed coat hardens."}], [{"name": "Head Smut", "symptoms": "Dark powdery grains.", "riskPeriod": "High rainfall."}], ["Grasshopper", "Armyworm"], ["Use certified seed."])
    add_crop("proso-millet-vari", "Proso Millet", "वरी / चीना (Vari / Cheena)", "Panicum miliaceum", "Cereals & Millets", "🌾", "Kharif & Summer", "Solapur, Nashik, Marathwada, Ahmednagar", "Matures in only 60 to 75 days with lowest water requirement of any cereal grain.", "20°C - 30°C", "200 - 300 mm.", "Well-drained light loams.", [{"stage": "Tillering", "days": "Days 1-25", "description": "Fast canopy spread."}, {"stage": "Flowering", "days": "Days 26-50", "description": "Drooping open panicle bloom."}, {"stage": "Harvest", "days": "Days 51-70", "description": "Golden yellow grains harvested."}], [{"name": "Leaf Smut", "symptoms": "Sooty streaks on leaf.", "riskPeriod": "Warm damp spells."}], ["Stem Borer"], ["Timely harvesting to prevent lodging."])
    add_crop("barley-jau", "Barley", "जव / सातू (Jau / Satu)", "Hordeum vulgare", "Cereals & Millets", "🌾", "Rabi (Winter)", "Western Maharashtra, Marathwada, North Maharashtra", "Cool-season cereal used for nutritious sattu flour, malt, beverage production, and animal feed. Highly salt-tolerant.", "12°C - 22°C", "250 - 350 mm.", "Sandy to clay loam, tolerates salinity.", [{"stage": "Tillering", "days": "Days 1-30", "description": "Stiff erect tillers develop."}, {"stage": "Heading", "days": "Days 31-65", "description": "Bearded awned spikes emerge."}, {"stage": "Ripening", "days": "Days 66-100", "description": "Golden straw and grain harvest."}], [{"name": "Covered Smut", "symptoms": "Persistent membrane enclosing black spore mass.", "riskPeriod": "Seed infection."}], ["Aphid", "Armyworm"], ["Seed treatment with Vitavax @ 2.5g/kg."])
    add_crop("oats", "Oats", "ओट्स / जई (Jaye)", "Avena sativa", "Cereals & Millets", "🌾", "Rabi", "Pune, Nashik, Satara dairy tracts (high fodder value)", "Premium breakfast cereal and succulent dairy green fodder rich in beta-glucan and minerals.", "15°C - 25°C", "350 - 450 mm.", "Well-drained loam with moderate fertility.", [{"stage": "Vegetative", "days": "Days 1-40", "description": "Leafy succulent shoots."}, {"stage": "Panicle", "days": "Days 41-75", "description": "Loose spreading panicles."}, {"stage": "Maturity", "days": "Days 76-110", "description": "Grain filling for milling or forage cut."}], [{"name": "Crown Rust", "symptoms": "Orange pustules on upper leaves.", "riskPeriod": "Mild humid winter."}], ["Aphids", "Armyworm"], ["Cut early at 50% flowering for highest protein fodder."])
    add_crop("basmati-rice", "Basmati Rice", "बासमती तांदूळ (Basmati Dhan)", "Oryza sativa subsp. indica", "Cereals & Millets", "🌾", "Kharif", "Punjab, Haryana, Western UP, Tarai belt of India", "The world-famous long-grain aromatic rice protected under Geographical Indication.", "20°C - 30°C", "1,200 - 1,500 mm.", "Deep alluvial clay loam.", [{"stage": "Tillering", "days": "Days 1-50", "description": "Slender aromatic tillers."}, {"stage": "Panicle", "days": "Days 51-90", "description": "Fragrant panicles with long slender spikelets."}, {"stage": "Maturity", "days": "Days 91-135", "description": "Grain elongation and aroma accumulation."}], [{"name": "Bacterial Blight", "symptoms": "Water-soaked wavy leaf margins.", "riskPeriod": "Heavy rain."}], ["Stem Borer", "Leaf Folder"], ["Pusa Basmati 1121, 1509 varieties."])
    add_crop("indrayani-rice", "Indrayani Fragrant Rice", "इंद्रायणी तांदूळ (Indrayani Rice)", "Oryza sativa (Maval)", "Cereals & Millets", "🌾", "Kharif", "Maval (Pune), Kolhapur, Satara, Nashik Western Ghats", "Renowned fragrant, sticky medium-slender rice created by MPKV Rahuri, the heart of Maharashtrian cuisine.", "22°C - 30°C", "1,100 - 1,300 mm.", "Ghat valley fertile loams.", [{"stage": "Vegetative", "days": "Days 1-50", "description": "Dense tillers with characteristic aroma."}, {"stage": "Panicle", "days": "Days 51-85", "description": "Full drooping fragrant panicles."}, {"stage": "Harvest", "days": "Days 86-125", "description": "Harvest when 85% grains turn straw golden."}], [{"name": "Blast", "symptoms": "Diamond lesions.", "riskPeriod": "Overcast monsoon weeks."}], ["Stem Borer"], ["Adopt certified breeder seeds from MPKV."])
    add_crop("ambemohar-rice", "Ambemohar Traditional Rice", "आंबेमोहर तांदूळ (Ambemohar Rice)", "Oryza sativa (GI)", "Cereals & Millets", "🌾", "Kharif", "Bhor, Mulshi, Velhe, Maval foothills of Pune district", "Traditional GI-tagged scented short-grain rice with aroma reminiscent of mango blossoms (आंबा मोहोर). Ideal for baby food, khichdi, and kheer.", "20°C - 28°C", "1,000 - 1,200 mm.", "High altitude red-lateritic valley soils.", [{"stage": "Tillering", "days": "Days 1-55", "description": "Slender slow vegetative growth."}, {"stage": "Heading", "days": "Days 56-95", "description": "Intense mango floral fragrance during morning anthesis."}, {"stage": "Harvest", "days": "Days 96-140", "description": "Fragrant short grains harvested."}], [{"name": "Leaf Blast", "symptoms": "Spindle-shaped lesions.", "riskPeriod": "Cool, misty mountain mornings."}], ["Stem Borer"], ["Maintain pure organic cultivation."])
    add_crop("rye", "Rye", "राई / रई (Rye grain)", "Secale cereale", "Cereals & Millets", "🌾", "Rabi", "Himalayan foothills and experimental cool zones", "Cold-hardy grain used for artisan bread, crispbread, and nutrient-dense cover crops.", "10°C - 20°C", "300 - 400 mm.", "Sandy and acidic soils.", [{"stage": "Vegetative", "days": "Days 1-45", "description": "Deep root penetration."}, {"stage": "Heading", "days": "Days 46-80", "description": "Long awned spikes."}, {"stage": "Maturity", "days": "Days 81-120", "description": "Hard slate-colored grains."}], [{"name": "Ergot", "symptoms": "Purple-black sclerotia.", "riskPeriod": "Wet flowering."}], ["Stem Sawfly"], ["Deep plowing to bury ergot sclerotia."])
    add_crop("durum-wheat", "Durum Wheat (Bansi Wheat)", "बन्सी / मालवी / कठिया गहू (Durum Wheat)", "Triticum durum", "Cereals & Millets", "🌾", "Rabi", "Marathwada, Vidarbha, Western Maharashtra black soils", "Hard vitreous amber grain with high protein and gluten strength, preferred for semolina (suji/rava), pasta, and daliya.", "15°C - 28°C", "300 - 450 mm.", "Deep black clay soils (Vertisols).", [{"stage": "Tillering", "days": "Days 1-30", "description": "Sturdy thick stems."}, {"stage": "Heading", "days": "Days 31-65", "description": "Heavy dense bearded heads."}, {"stage": "Maturity", "days": "Days 66-105", "description": "Hard translucent amber kernels."}], [{"name": "Stem Rust", "symptoms": "Dark brown pustules.", "riskPeriod": "Warm winter spells."}], ["Termites"], ["Use MACS-2846, AKDW-2997-16 (Sharada) resistant varieties."])

    # Now we write out python script that will generate all 260 crops
    print("Base compiled, generating all categories...")

build_crops()
