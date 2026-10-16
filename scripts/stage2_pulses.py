#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates the complete 260 crops database.
Loads stage1 (cereals) and appends all other categories.
"""

import json
import os

with open('scripts/crops_stage1.json', 'r', encoding='utf-8') as f:
    crops = json.load(f)

def c(cid, name, local, sci, cat, emoji, season, region, desc, temp, water, soil, stages, diseases, pests, prev):
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
# 2. PULSES & LEGUMES (18 crops)
# ==========================================
c("pigeon-pea-tur", "Pigeon Pea (Tur / Arhar)", "तूर / अरहर (Tur / Arhar)", "Cajanus cajan", "Pulses & Legumes", "🫘",
  "Kharif", "Marathwada (Latur is Asia's largest Tur dal trading hub), Vidarbha (Akola, Amravati), Khandesh",
  "The foundation of Indian dal. Deep-rooted legume fixing nitrogen and enriching black soils; grown predominantly as intercrop with Soybean or Cotton.",
  "25°C - 35°C", "600 - 800 mm; drought-hardy due to deep taproot.", "Deep, well-drained black cotton soil or loam, pH 6.5 - 7.5.",
  [{"stage": "Seedling & Branching", "days": "Days 1-45", "description": "Slow early growth while deep taproot establishes."},
   {"stage": "Canopy & Flowering", "days": "Days 46-100", "description": "Profuse yellow blooms attract pollinators."},
   {"stage": "Pod Formation & Filling", "days": "Days 101-140", "description": "Green pods develop; pod borer vulnerable stage."},
   {"stage": "Maturity & Harvest", "days": "Days 141-180", "description": "Pods turn dry brown; harvested with threshers."}],
  [{"name": "Fusarium Wilt (Fusarium udum)", "symptoms": "Gradual wilting, purple bands on stems, vascular browning when stem is split.", "riskPeriod": "Flowering stage during soil moisture fluctuations."},
   {"name": "Sterility Mosaic Disease (SMD)", "symptoms": "Excessive bushiness, pale green mosaic leaves, complete lack of flowers; transmitted by eriophyid mites.", "riskPeriod": "Dense canopies with high mite vector populations."}],
  ["Gram Pod Borer (Helicoverpa armigera)", "Plume Moth", "Pod Fly (Melanagromyza obtusa)"],
  ["Use wilt and SMD-resistant varieties like BSMR-736, BDN-711, or Maruti (ICP-8863).",
   "Seed treatment with Trichoderma viride @ 4g/kg + Rhizobium culture."])

c("chickpea-chana", "Chickpea (Bengal Gram / Chana)", "हरभरा / चणा (Harbhara / Chana)", "Cicer arietinum", "Pulses & Legumes", "🫘",
  "Rabi (Winter)", "Marathwada (Latur, Osmanabad), Western Maharashtra (Ahmednagar, Solapur), Vidarbha",
  "Premier winter pulse crop of Maharashtra. Consumed as fresh green pods (Hurda/Harbhara ghaati), roasted gram, besan flour, and dry dal.",
  "15°C - 25°C (cool nights, dry sunny days)", "250 - 350 mm; requires 1-2 protective irrigations.",
  "Deep, moisture-retentive black cotton soil with pH 6.0 - 8.0.",
  [{"stage": "Emergence & Nipping", "days": "Days 1-25", "description": "Terminal bud nipping done at 25-30 days to stimulate heavy lateral branching."},
   {"stage": "Flowering", "days": "Days 26-55", "description": "Delicate pinkish or white flowers appear in leaf axils."},
   {"stage": "Pod Development", "days": "Days 56-85", "description": "Pods swell containing 1-2 plump seeds."},
   {"stage": "Maturity", "days": "Days 86-110", "description": "Foliage turns golden brown; grains harden."}],
  [{"name": "Fusarium Wilt (Fusarium oxysporum f. sp. ciceris)", "symptoms": "Leaves drop, roots exhibit internal dark brown vascular discoloration.", "riskPeriod": "Warm early winter soils or mid-season moisture stress."},
   {"name": "Ascochyta Blight", "symptoms": "Circular lesions with concentric rings of pycnidia on leaves, stems, and pods.", "riskPeriod": "Cool, wet, cloudy winter spells."}],
  ["Gram Pod Borer (Helicoverpa armigera)", "Cutworms", "Aphids"],
  ["Plant wilt-resistant varieties like Digvijay, Vijay, Phule Vikram, or Jaki-9218.",
   "Perform terminal nipping at 30 days to double pod-bearing branches."])

c("green-gram-moong", "Green Gram (Moong)", "मूग (Moong)", "Vigna radiata", "Pulses & Legumes", "🌱",
  "Kharif & Summer", "Marathwada, Vidarbha, Jalgaon, Dhule, Ahmednagar",
  "Quick-maturing (60-70 days) protein-rich pulse crop ideal for crop rotations and soil health regeneration.",
  "25°C - 35°C", "300 - 400 mm.", "Well-drained loam to clay loam.",
  [{"stage": "Vegetative", "days": "Days 1-25", "description": "Rapid leaf canopy and root nodulation."},
   {"stage": "Flowering", "days": "Days 26-45", "description": "Yellow blossoms in clusters."},
   {"stage": "Pod Maturity", "days": "Days 46-65", "description": "Black cylindrical pods ready for picking."}],
  [{"name": "Yellow Mosaic Virus (MYMV)", "symptoms": "Irregular yellow and green patches on leaves; transmitted by whiteflies.", "riskPeriod": "Hot dry weather with high whitefly activity."},
   {"name": "Powdery Mildew", "symptoms": "White powdery coating on foliage.", "riskPeriod": "Humid mornings."}],
  ["Whitefly", "Thrips", "Pod Borer"],
  ["Grow MYMV-resistant varieties (BM-2002-1, BM-2003-2, Vaibhav).", "Seed treatment with Imidacloprid @ 5g/kg."])

c("black-gram-urad", "Black Gram (Urad)", "उडीद (Udid / Urad)", "Vigna mungo", "Pulses & Legumes", "🫘",
  "Kharif & Summer", "Vidarbha (Nagpur, Wardha), Marathwada (Nanded, Latur), Khandesh",
  "Indispensable pulse in Indian culinary traditions for papad, idli, vada, and dal makhani.",
  "25°C - 35°C", "350 - 450 mm.", "Medium to heavy black cotton soils with good drainage.",
  [{"stage": "Vegetative", "days": "Days 1-25", "description": "Dense hairy stems and trifoliate leaves."},
   {"stage": "Flowering", "days": "Days 26-45", "description": "Bright yellow flowers."},
   {"stage": "Pod Ripening", "days": "Days 46-70", "description": "Hairy pods turn black when ripe."}],
  [{"name": "Yellow Mosaic Virus", "symptoms": "Bright golden yellow mottling.", "riskPeriod": "Whitefly outbreaks."},
   {"name": "Cercospora Leaf Spot", "symptoms": "Brown spots with reddish margins.", "riskPeriod": "Warm rainy periods."}],
  ["Whitefly", "Pod Borer", "Stem Fly"],
  ["Use resistant varieties like TAU-1, TPU-4, AKU-15.", "Seed treatment with Trichoderma."])

c("soybean", "Soybean", "सोयाबीन (Soybean)", "Glycine max", "Pulses & Legumes", "🌱",
  "Kharif", "Marathwada (Latur, Nanded), Vidarbha (Amravati, Akola, Yavatmal, Nagpur), Western Maharashtra (Kolhapur, Sangli)",
  "The golden bean that revolutionized Maharashtra agriculture. Miracle crop delivering 40% protein and 20% edible oil, supporting millions of rural livelihoods.",
  "24°C - 30°C", "450 - 650 mm; highly sensitive to dry spells at pod-filling.", "Deep, fertile well-drained black cotton soil, pH 6.5 - 7.5.",
  [{"stage": "Germination & Vegetative (V1-V4)", "days": "Days 1-30", "description": "Emergence, unifoliate and trifoliate leaf expansion, root nodulation with Bradyrhizobium."},
   {"stage": "Flowering (R1-R2)", "days": "Days 31-50", "description": "Tiny purple or white flowers open in leaf axils."},
   {"stage": "Pod Development (R3-R4)", "days": "Days 51-70", "description": "Pods elongate; critical moisture-sensitive phase."},
   {"stage": "Seed Filling & Senescence (R5-R8)", "days": "Days 71-100", "description": "Leaves yellow and drop; pods turn golden brown containing 2-3 round seeds."}],
  [{"name": "Soybean Rust (Phakopsora pachyrhizi)", "symptoms": "Tiny brown to reddish-brown lesions with erupting volcanic pustules on leaf undersides.", "riskPeriod": "Extended cloudiness, high relative humidity (>85%), temp 18-26°C."},
   {"name": "Charcoal Rot (Macrophomina phaseolina)", "symptoms": "Sub-epidermal black specks (microsclerotia) causing premature plant death and stem splitting.", "riskPeriod": "Post-flowering drought accompanied by high soil temp (>33°C)."},
   {"name": "Collar Rot / Root Rot (Sclerotium rolfsii)", "symptoms": "White fan-shaped fungal mycelium with brown mustard-like seeds at soil line.", "riskPeriod": "Waterlogged soil conditions during seedling stage."}],
  ["Girdle Beetle (Obereopsis brevis)", "Spodoptera litura (Tobacco Caterpillar)", "Semilooper", "Gram Pod Borer"],
  ["Use high-yielding university varieties: JS-335, JS-9305, Phule Sangam (KDS-726), Phule Kimaya (KDS-753).",
   "Inoculate seed with Bradyrhizobium japonicum + PSB culture @ 250g per 10kg seed."])

c("moth-bean-matki", "Moth Bean (Matki)", "मटकी (Matki / Moth)", "Vigna aconitifolia", "Pulses & Legumes", "🫘",
  "Kharif", "Ahmednagar, Solapur, Beed, Dhule, Jalgaon dry zones", "Super-drought hardy pulse; soul of Maharashtra's beloved breakfast dish 'Misal Pav' when sprouted.",
  "25°C - 38°C", "200 - 300 mm; survives severe dry spells.", "Light, sandy, gravelly marginal soils.",
  [{"stage": "Vegetative", "days": "Days 1-30", "description": "Prostrate spreading ground cover."},
   {"stage": "Flowering", "days": "Days 31-50", "description": "Yellow blossoms."},
   {"stage": "Pod Ripening", "days": "Days 51-75", "description": "Slender pods turn brown."}],
  [{"name": "Yellow Mosaic Virus", "symptoms": "Yellowing of leaves.", "riskPeriod": "Hot dry weather."}],
  ["Jassids", "Whitefly"], ["Use improved varieties like Phule Matki-15, RMO-40."])

c("cowpea-chawli", "Cowpea (Chawli / Lobia)", "चवळी (Chawli / Lobia)", "Vigna unguiculata", "Pulses & Legumes", "🫘",
  "Kharif & Summer", "Konkan, Western Maharashtra, Marathwada, Vidarbha", "Versatile dual-purpose crop grown for tender green vegetable pods, nutritious dry pulse, and green manure.",
  "24°C - 34°C", "350 - 450 mm.", "Adaptable to poor acid or alkaline soils.",
  [{"stage": "Vegetative", "days": "Days 1-30", "description": "Vigorous twining or bush growth."},
   {"stage": "Pod Setting", "days": "Days 31-55", "description": "Long green hanging pods."},
   {"stage": "Maturity", "days": "Days 56-85", "description": "Dry grain pods harvested."}],
  [{"name": "Anthracnose", "symptoms": "Sunken brown lesions on pods.", "riskPeriod": "Continuous rain."}],
  ["Aphids (Aphis craccivora)", "Pod Borer"], ["Use Phule CP-05040, Konkan Safed varieties."])

c("lentil-masoor", "Lentil (Masoor)", "मसूर (Masoor)", "Lens culinaris", "Pulses & Legumes", "🫘",
  "Rabi (Winter)", "Vidarbha (Nagpur, Bhandara), Marathwada, Central India", "Ancient quick-cooking protein-rich pulse cultivated in residual soil moisture after paddy.",
  "15°C - 24°C", "200 - 300 mm.", "Well-drained clay loam or alluvial soils.",
  [{"stage": "Seedling", "days": "Days 1-25", "description": "Delicate pinnate leaves."},
   {"stage": "Flowering", "days": "Days 26-55", "description": "Small bluish-white blossoms."},
   {"stage": "Pod Filling & Harvest", "days": "Days 56-90", "description": "Flat pods holding 1-2 lens-shaped seeds."}],
  [{"name": "Rust", "symptoms": "Uredial pustules on leaves.", "riskPeriod": "Cool humid conditions."}],
  ["Pod Borer", "Aphids"], ["Seed treatment with Trichoderma.", "Use KLS-218, JL-3 varieties."])

c("field-pea-vatana", "Field Pea (Dry Vatana / Green Peas)", "वाटाणा (Vatana / Matar)", "Pisum sativum", "Pulses & Legumes", "🫛",
  "Rabi", "Nashik, Pune, Satara, Ahmednagar cool winter pockets", "Grown for sweet tender fresh green peas and sun-dried white/green vatana for famous street foods and curries.",
  "13°C - 20°C", "300 - 400 mm.", "Well-drained fertile loamy soil, pH 6.0 - 7.5.",
  [{"stage": "Vegetative", "days": "Days 1-30", "description": "Tendril-bearing climbing foliage."},
   {"stage": "Blossom & Podding", "days": "Days 31-60", "description": "White butterfly-like flowers; sweet pods swell."},
   {"stage": "Harvest", "days": "Days 61-90", "description": "Green pods handpicked or left to dry."}],
  [{"name": "Powdery Mildew (Erysiphe pisi)", "symptoms": "White powdery coating covering leaves, stems, and pods.", "riskPeriod": "Dry warm days and cool humid nights."}],
  ["Pea Pod Borer", "Pea Aphid"], ["Grow powdery mildew resistant varieties (Arkel, Azad P-1, Phule Priya)."])

c("horse-gram-kulthi", "Horse Gram (Kulthi / Kulith)", "कुळीथ / हुलगा (Kulith / Hulga)", "Macrotyloma uniflorum", "Pulses & Legumes", "🫘",
  "Kharif & Late Kharif", "Konkan (Ratnagiri, Sindhudurg), Western Ghats, Solapur, Ahmednagar", "Nutritional powerhouse known for dissolving kidney stones and making soul-warming Konkani Pithla and soup.",
  "20°C - 32°C", "200 - 300 mm; extreme drought resistance.", "Gravelly lateritic, red or impoverished hill soils.",
  [{"stage": "Vegetative", "days": "Days 1-35", "description": "Dense low-creeping vine."},
   {"stage": "Flowering", "days": "Days 36-65", "description": "Small yellow blossoms."},
   {"stage": "Maturity", "days": "Days 66-95", "description": "Curved dry pods with flat hard seeds."}],
  [{"name": "Dry Root Rot", "symptoms": "Bark shredded at collar.", "riskPeriod": "Extreme heat."}],
  ["Pod Borer"], ["Use Dapoli-1, Sina varieties."])

c("rajma-kidney-beans", "Kidney Bean (Rajma)", "राजमा (Rajma)", "Phaseolus vulgaris", "Pulses & Legumes", "🫘",
  "Rabi in Maharashtra / Kharif in Hills", "Western Maharashtra (Pune, Satara, Ahmednagar irrigated winter tracts), Jammu & Kashmir, Himachal", "High-value protein pulse yielding plump red kidney beans with rich savory flavor.",
  "15°C - 25°C", "400 - 500 mm.", "Rich, fertile loamy soil with excellent drainage.",
  [{"stage": "Vegetative", "days": "Days 1-30", "description": "Bush or pole type upright stems."},
   {"stage": "Flowering", "days": "Days 31-55", "description": "White or purple blooms."},
   {"stage": "Pod Maturity", "days": "Days 56-95", "description": "Large kidney-shaped seeds fill."}],
  [{"name": "Bean Anthracnose", "symptoms": "Sunken dark cankers on pods.", "riskPeriod": "Wet humid spells."}],
  ["Aphid", "Pod Borer"], ["Apply 100-120 kg N/ha since Rajma lacks active root nodulation."])

c("cluster-bean-guar", "Cluster Bean (Guar)", "गवार (Gawar / Guar)", "Cyamopsis tetragonoloba", "Pulses & Legumes", "🫛",
  "Kharif & Summer", "Nashik, Pune, Ahmednagar, Marathwada, Rajasthan border tracts", "Drought-hardy legume grown for delicious green vegetable clusters and industrial guar gum (galactomannan).",
  "26°C - 35°C", "250 - 350 mm.", "Sandy to loamy well-drained soils.",
  [{"stage": "Vegetative", "days": "Days 1-30", "description": "Stiff upright branching."},
   {"stage": "Clustering", "days": "Days 31-55", "description": "Pods form in tight clusters at leaf nodes."},
   {"stage": "Maturity", "days": "Days 56-90", "description": "Tender vegetable pickings or seed drying."}],
  [{"name": "Bacterial Blight", "symptoms": "V-shaped brown lesions on leaf margins.", "riskPeriod": "Monsoon humidity."}],
  ["Jassids", "Aphids"], ["Grow Pusa Navbahar, Phule Gaurav."])

c("broad-bean-fava", "Broad Bean (Fava Bean)", "घेवडा / बाकला (Bakla / Broad Bean)", "Vicia faba", "Pulses & Legumes", "🫘",
  "Rabi", "Mahabaleshwar, Pune, Western Ghat plateaus, North India", "Cool-season ancient legume producing large succulent nutrient-rich beans in thick leathery pods.",
  "12°C - 20°C", "350 - 450 mm.", "Heavy fertile clay loams.",
  [{"stage": "Vegetative", "days": "Days 1-35", "description": "Square hollow stems and glaucous leaves."},
   {"stage": "Flowering", "days": "Days 36-65", "description": "White flowers with dark blotches."},
   {"stage": "Pod Harvest", "days": "Days 66-105", "description": "Large thick pods."}],
  [{"name": "Chocolate Spot (Botrytis fabae)", "symptoms": "Reddish-brown spots across leaves.", "riskPeriod": "Cool overcast weather."}],
  ["Black Bean Aphid"], ["Ensure wide row spacing (45 cm) for cross-ventilation."])

c("hyacinth-bean-wal", "Hyacinth Bean (Wal / Pavta)", "वाल / पावटा (Wal / Kadve Wal / Surti Wal)", "Lablab purpureus", "Pulses & Legumes", "🫘",
  "Late Kharif & Rabi", "Konkan (Alibag Wal has GI status!), Pune, Satara, Western Maharashtra", "Iconic pulse of Maharashtra coastal cuisine (Alibag Walachi Usal / Birde). Famous for distinct aromatic taste and high medicinal value.",
  "18°C - 28°C", "350 - 450 mm; grown on residual moisture in rice fallows.", "Medium black to coastal alluvium.",
  [{"stage": "Vegetative & Trailing", "days": "Days 1-45", "description": "Vigorous climbing vine trained on bunds or rice stubble."},
   {"stage": "Blossoming", "days": "Days 46-75", "description": "White or purple fragrant flower racemes."},
   {"stage": "Pod Picking", "days": "Days 76-120", "description": "Broad flat pods harvested for fresh beans or dried."}],
  [{"name": "Yellow Mosaic", "symptoms": "Golden leaf discoloration.", "riskPeriod": "Whitefly season."}],
  ["Aphids", "Pod Borer"], ["Plant famous Konkan Wal, Phule Wal varieties."])

c("french-bean", "French Bean (Snap Bean)", "फरसबी / श्रावण घेवडा (Pharasbi / Shravan Ghevda)", "Phaseolus vulgaris var. humilis", "Pulses & Legumes", "🫛",
  "Kharif, Rabi & Zaid", "Pune, Satara (Wai), Nashik, Kolhapur vegetable tracts", "Crisp, tender stringless green pods highly prized in premium urban vegetable markets.",
  "15°C - 25°C", "350 - 450 mm; regular light irrigations.", "Friable sandy loam rich in organic compost, pH 6.0 - 6.8.",
  [{"stage": "Vegetative", "days": "Days 1-25", "description": "Compact bush or climbing habit."},
   {"stage": "Flowering", "days": "Days 26-40", "description": "Self-pollinating blossoms."},
   {"stage": "Pod Picking", "days": "Days 41-65", "description": "Harvest pods when tender and snap easily before seeds bulge."}],
  [{"name": "Rust", "symptoms": "Reddish pustules on leaves.", "riskPeriod": "High humidity."}],
  ["Whitefly", "Leafhopper"], ["Grow Contender, Phule Suyash varieties."])

c("winged-bean", "Winged Bean (Goa Bean)", "चौधारी घेवडा (Chaudhari Ghevda)", "Psophocarpus tetragonolobus", "Pulses & Legumes", "🫛",
  "Kharif", "Konkan, Western Ghats, Goa border", "All-edible miracle plant: tender four-winged pods, leaves, flowers, seeds, and tuberous roots are all protein-rich.",
  "22°C - 32°C", "600 - 800 mm.", "Moist laterite and alluvial soils.",
  [{"stage": "Vegetative", "days": "Days 1-45", "description": "Strong vine requiring trellising."},
   {"stage": "Flowering", "days": "Days 46-75", "description": "Sky-blue edible flowers."},
   {"stage": "Pod Harvest", "days": "Days 76-120", "description": "Four-angled frilled pods picked tender."}],
  [{"name": "Collar Rot", "symptoms": "Damping off in waterlogged beds.", "riskPeriod": "Heavy rains."}],
  ["Caterpillars"], ["Provide strong bamboo trellis support."])

c("lima-bean", "Lima Bean (Butter Bean)", "डबल बी / लीमा बीन (Double Bee)", "Phaseolus lunatus", "Pulses & Legumes", "🫘",
  "Rabi", "Mahabaleshwar, Panchgani, Satara cool hill tracts", "Large buttery flat beans cultivated in cool Western Ghat hill slopes, famous specialty in Mahabaleshwar.",
  "15°C - 24°C", "400 - 550 mm.", "Deep rich mountain loams.",
  [{"stage": "Vine Growth", "days": "Days 1-40", "description": "Perennial or annual vigorous vine."},
   {"stage": "Flowering", "days": "Days 41-70", "description": "White or violet flowers."},
   {"stage": "Pod Picking", "days": "Days 71-110", "description": "Large flat pods with creamy butter beans."}],
  [{"name": "Downy Mildew", "symptoms": "White fungal patches on pods.", "riskPeriod": "Cold hill fog."}],
  ["Pod Borer"], ["Harvest pods at mature green stage."])

c("rice-bean", "Rice Bean", "राईस बीन / नवरंगी डाळ (Navrangi Dal)", "Vigna umbellata", "Pulses & Legumes", "🫘",
  "Kharif", "Tribal hill tracts of Vidarbha and Western Ghats, Northeast India", "Climate-hardy underutilized legume immune to many diseases of common pulses, highly nutritious.",
  "20°C - 30°C", "400 - 600 mm.", "Acidic and poor mountain soils.",
  [{"stage": "Vegetative", "days": "Days 1-40", "description": "Twining vine with yellow flowers."},
   {"stage": "Pod Setting", "days": "Days 41-75", "description": "Slender cylindrical pods."},
   {"stage": "Harvest", "days": "Days 76-115", "description": "Small oblong colored seeds."}],
  [{"name": "Cercospora Leaf Spot", "symptoms": "Brown leaf spots.", "riskPeriod": "Humid periods."}],
  ["Aphids"], ["Grown naturally in tribal eco-farms."])

print(f"Pulses loaded. Total now: {len(crops)}")

with open('scripts/crops_stage2.json', 'w', encoding='utf-8') as f:
    json.dump(crops, f, ensure_ascii=False, indent=2)
