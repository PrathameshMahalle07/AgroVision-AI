#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

with open('scripts/crops_stage2.json', 'r', encoding='utf-8') as f:
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
# 3. OILSEEDS (16 crops)
# ==========================================
c("groundnut-peanut", "Groundnut (Peanut)", "भुईमूग / शेंगदाणा (Bhuimug / Shengdana)", "Arachis hypogaea", "Oilseeds", "🥜",
  "Kharif & Summer", "Western Maharashtra (Kolhapur, Satara, Sangli, Pune), Khandesh (Dhule, Jalgaon), Marathwada",
  "Premier edible oilseed and protein food of Maharashtra. Geocarpic crop where flowers bloom above ground and pegs penetrate soil to form subterranean pods.",
  "25°C - 30°C", "500 - 650 mm; critical water demand during flowering and peg penetration.", "Light sandy loam, well-drained friable red/black soils rich in calcium, pH 6.0 - 7.5.",
  [{"stage": "Emergence & Branching", "days": "Days 1-25", "description": "Rapid seedling emergence and lateral branching."},
   {"stage": "Flowering & Pegging", "days": "Days 26-50", "description": "Yellow self-pollinated flowers; fertilized gynophore (peg) grows geotropically into soil."},
   {"stage": "Pod Development", "days": "Days 51-85", "description": "Underground pod expansion; gypsum application ensures plump shells."},
   {"stage": "Pod Maturity & Harvest", "days": "Days 86-115", "description": "Internal pod shell displays dark brown reticulation; harvested by vine pullers."}],
  [{"name": "Tikka Disease / Leaf Spot (Cercospora arachidicola)", "symptoms": "Circular dark brown spots with prominent yellow halos on upper leaf surface.", "riskPeriod": "Warm, humid weather with prolonged leaf wetness (25-30°C)."},
   {"name": "Groundnut Rust (Puccinia arachidis)", "symptoms": "Orange-brown pustules on leaf undersides causing severe defoliation.", "riskPeriod": "High humidity and continuous cloudy monsoon spells."}],
  ["Groundnut Leaf Miner", "White Grub (Holotrichia consanguinea)", "Spodoptera litura", "Aphids"],
  ["Apply Gypsum @ 500 kg/ha at pegging (40-45 days) to ensure calcium for pod shell formation.",
   "Treat seed with Trichoderma viride @ 5g/kg + Imidacloprid @ 2ml/kg.",
   "Use high-yielding university varieties: Phule Unnati, JL-24 (Phule Pragati), TAG-24, or TG-37A."])

c("mustard-sarson", "Mustard (Rapeseed / Sarson)", "मोहरी / राई / सरसो (Mohari / Sarson)", "Brassica juncea", "Oilseeds", "🌼",
  "Rabi (Winter)", "Vidarbha, Khandesh, North Maharashtra, Rajasthan & MP border tracts",
  "Important winter oilseed yielding pungent cooking oil and nutrient-dense oilcake for dairy cattle.",
  "15°C - 25°C", "250 - 350 mm.", "Light to heavy loam with good drainage, pH 6.0 - 7.5.",
  [{"stage": "Rosette & Vegetative", "days": "Days 1-35", "description": "Broad radical leaves form dense ground rosette."},
   {"stage": "Bolting & Flowering", "days": "Days 36-65", "description": "Central flower stalk bolts into golden yellow blossoms."},
   {"stage": "Siliqua (Pod) Formation", "days": "Days 66-95", "description": "Slender beaked pods (siliquae) develop containing tiny round seeds."},
   {"stage": "Maturity", "days": "Days 96-125", "description": "Pods turn straw-yellow; harvested before shattering."}],
  [{"name": "White Rust (Albugo candida)", "symptoms": "White porcelain-like blisters on leaf undersides and swollen staghead floral malformations.", "riskPeriod": "Cool, humid morning fog."},
   {"name": "Alternaria Blight", "symptoms": "Concentric dark brown target spots on leaves and siliquae.", "riskPeriod": "Warm humid spells after flowering."}],
  ["Mustard Aphid (Lipaphis erysimi)", "Painted Bug", "Sawfly"],
  ["Sow early in October to escape severe aphid infestation in December-January.",
   "Spray Oxydemeton-methyl or Dimethoate 30 EC @ 1ml/L at first aphid appearance on inflorescence."])

c("sunflower", "Sunflower", "सूर्यफूल (Suryaphul)", "Helianthus annuus", "Oilseeds", "🌻",
  "Kharif, Rabi & Summer", "Marathwada (Beed, Latur, Osmanabad), Solapur, Ahmednagar, Vidarbha",
  "Heliotropic oilseed with premium heart-healthy polyunsaturated fatty acids (PUFA). Photo-insensitive crop suitable for any season in Maharashtra.",
  "20°C - 30°C", "450 - 600 mm; critical at button stage, flowering, and seed development.", "Deep, fertile black clay soils or fertile loams, pH 6.5 - 8.0.",
  [{"stage": "Emergence & Vegetative", "days": "Days 1-30", "description": "Rapid broad-leaf expansion and deep taproot development."},
   {"stage": "Star / Button Stage", "days": "Days 31-50", "description": "Inflorescence bud appears at stem apex; heliotropism active."},
   {"stage": "Flowering & Pollination", "days": "Days 51-70", "description": "Ray florets and disk florets open; honeybee pollination essential."},
   {"stage": "Seed Filling & Capitulum Bending", "days": "Days 71-95", "description": "Back of flower head turns lemon yellow; achenes harden."}],
  [{"name": "Alternaria Leaf Blight (Alternaria helianthi)", "symptoms": "Dark brown circular spots coalescing into large necrotic blights.", "riskPeriod": "Cloudy humid rainy weather."},
   {"name": "Necrosis Disease (Tobamovirus)", "symptoms": "Systemic mosaic, leaf malformation, and necrotic streaks on stem and capitulum; thrips vector.", "riskPeriod": "Hot dry spells with high thrips activity."}],
  ["Capitulum Borer (Helicoverpa armigera)", "Thrips", "Jassids"],
  ["Maintain 3-5 honeybee boxes per hectare to double pollination and prevent hollow seed formation.",
   "Spray Mancozeb @ 2.5g/L or Propiconazole @ 1ml/L at initiation of Alternaria spots."])

c("safflower-kardai", "Safflower (Kardai)", "करडई (Kardai)", "Carthamus tinctorius", "Oilseeds", "🌾",
  "Rabi (Winter)", "Marathwada (Osmanabad, Beed, Latur), Solapur, Ahmednagar, Western Maharashtra",
  "Traditional drought-resilient spiny oilseed of Maharashtra black soils. Known for cold-pressed cardi-oil (high linoleic acid) and tender winter vegetable greens.",
  "18°C - 28°C", "250 - 350 mm; extremely deep taproot extracts moisture from subsoil.", "Deep black soils (Vertisols) with high water retention capacity.",
  [{"stage": "Rosette Stage", "days": "Days 1-40", "description": "Slow prostrate growth while deep taproot penetrates 2-3 meters into subsoil."},
   {"stage": "Stem Elongation & Branching", "days": "Days 41-75", "description": "Stiff spiny stems and branches form."},
   {"stage": "Capitulum Flowering", "days": "Days 76-105", "description": "Vibrant orange-yellow florets bloom at branch tips."},
   {"stage": "Seed Maturation", "days": "Days 106-130", "description": "White shiny achenes mature inside spiny involucral bracts."}],
  [{"name": "Alternaria Leaf Spot", "symptoms": "Concentric brown spots with chlorotic haloes on leaves.", "riskPeriod": "Post-flowering winter humidity."},
   {"name": "Safflower Wilt (Fusarium oxysporum)", "symptoms": "Unilateral wilting and brown vascular discoloration.", "riskPeriod": "Damp soil during vegetative rosette phase."}],
  ["Safflower Aphid (Uroleucon carthami)", "Gram Pod Borer"],
  ["Sow in late September or early October to escape aphid explosion in peak winter.",
   "Use aphid-tolerant varieties like Phule Kusuma, Bhima, or NARI-6."])

c("sesame-til", "Sesame (Til)", "तीळ (Til)", "Sesamum indicum", "Oilseeds", "🌱",
  "Kharif & Summer", "Khandesh (Jalgaon, Dhule), Vidarbha, Solapur, Marathwada",
  "Queen of oilseeds; ancient oil-bearing plant rich in sesamin antioxidants and calcium. Sacred ingredient in Makar Sankranti Tilgul.",
  "25°C - 35°C", "300 - 400 mm; sensitive to waterlogging.", "Well-drained sandy loam or light black soil, pH 6.0 - 7.5.",
  [{"stage": "Vegetative", "days": "Days 1-30", "description": "Erect branching and opposite leaves."},
   {"stage": "Flowering", "days": "Days 31-55", "description": "Bell-shaped white to pale pink flowers open in leaf axils."},
   {"stage": "Capsule Formation", "days": "Days 56-80", "description": "Four-grooved erect capsules develop containing rows of seeds."},
   {"stage": "Maturity", "days": "Days 81-100", "description": "Bottom capsules turn yellow-brown; cut before dehiscence."}],
  [{"name": "Phyllody (Phytoplasma)", "symptoms": "Floral parts transform into green leafy structures; plant becomes sterile witches' broom; leafhopper vector.", "riskPeriod": "Continuous warm weather with leafhopper activity."},
   {"name": "Bacterial Blight", "symptoms": "Angular water-soaked spots on foliage.", "riskPeriod": "Wind-driven monsoon showers."}],
  ["Til Hawk Moth (Sphingid caterpillar)", "Antigastra Gall Fly"],
  ["Use varieties like Tapi (JLT-408), Phule Til-1, or RT-351.",
   "Control leafhopper vector using Imidacloprid @ 3ml/10L to prevent incurable Phyllody."])

c("castor-erandi", "Castor", "एरंडी (Erandi)", "Ricinus communis", "Oilseeds", "🌿",
  "Kharif", "Marathwada, Vidarbha, Khandesh, Gujarat border tracts",
  "High-value non-edible industrial oilseed producing ricinoleic acid used for high-grade aviation lubricants, cosmetics, and biodiesel.",
  "25°C - 35°C", "400 - 600 mm; hardy taproot system.", "Deep loam to gravelly light soil with good internal drainage.",
  [{"stage": "Seedling", "days": "Days 1-30", "description": "Large palmate leaves expand."},
   {"stage": "Primary Spike Flowering", "days": "Days 31-70", "description": "Monoecious flowers on terminal raceme."},
   {"stage": "Capsule Setting & Spikes", "days": "Days 71-120", "description": "Spiny capsules form on multiple spike orders."},
   {"stage": "Harvesting", "days": "Days 121-180", "description": "Spikes picked as capsules turn yellowish-brown."}],
  [{"name": "Castor Wilt (Fusarium oxysporum f. sp. ricini)", "symptoms": "Yellowing and wilting of plants with internal stem vascular browning.", "riskPeriod": "Flowering stage during soil moisture stress."},
   {"name": "Botrytis Gray Mold", "symptoms": "Woolly gray fungal mold rotting entire spikes during rain.", "riskPeriod": "Continuous humid overcast monsoon weather."}],
  ["Castor Semilooper (Achaea janata)", "Shoot & Capsule Borer"],
  ["Use wilt-resistant hybrids: DCH-177, GCH-7, or Phule Castor-1.",
   "Install bird perches @ 25/ha to encourage birds feeding on semiloopers."])

c("linseed-flaxseed-javas", "Linseed / Flaxseed (Javas)", "जवस / अळशी (Javas / Alsi)", "Linum usitatissimum", "Oilseeds", "🌱",
  "Rabi (Winter)", "Vidarbha (Chandrapur, Bhandara, Nagpur), Marathwada, Central India",
  "Ancient oilseed celebrated as modern superfood rich in Omega-3 (alpha-linolenic acid), lignans, and dietary fiber. Famous for Maharashtrian Javas Chutney.",
  "15°C - 25°C", "250 - 350 mm.", "Deep black moisture-retentive soils (Vertisols) or clay loams.",
  [{"stage": "Vegetative", "days": "Days 1-35", "description": "Slender fibrous erect stems with linear leaves."},
   {"stage": "Flowering", "days": "Days 36-65", "description": "Sky-blue to violet flowers open in morning sunshine."},
   {"stage": "Boll Formation", "days": "Days 66-95", "description": "Globular bolls (capsules) develop containing 10 flat shiny seeds."},
   {"stage": "Maturity", "days": "Days 96-120", "description": "Bolls turn golden brown; rustle when shaken."}],
  [{"name": "Linseed Rust (Melampsora lini)", "symptoms": "Bright orange-yellow uredial pustules on leaves and stems, later turning glossy black.", "riskPeriod": "Humid cool winter weather."}],
  ["Linseed Gall Midge (Dasyneura lini)", "Semilooper"],
  ["Use rust-resistant university varieties: PKV NL-260, Meera, Sharda, or JLS-9."])

c("niger-karale", "Niger Seed (Karale)", "कारळे / खुरसणी (Karale / Khursani)", "Guizotia abyssinica", "Oilseeds", "🌼",
  "Late Kharif", "Tribal hill zones of Nashik (Igatpuri, Surgana), Nandurbar, Thane, Western Ghats",
  "Hardy oilseed grown on impoverished tribal hill slopes. Core ingredient of authentic fiery Maharashtrian Karale Chutney.",
  "18°C - 28°C", "300 - 450 mm; thrives on residual monsoon moisture.", "Light gravelly laterite, poor stony or acidic soils.",
  [{"stage": "Vegetative", "days": "Days 1-35", "description": "Dense semi-bush with yellow composite flowers."},
   {"stage": "Flowering", "days": "Days 36-70", "description": "Bright golden daisy-like heads attract bees."},
   {"stage": "Seed Hardening & Harvest", "days": "Days 71-105", "description": "Small black glossy seeds fill capitula."}],
  [{"name": "Cercospora Leaf Spot", "symptoms": "Small brown spots on foliage.", "riskPeriod": "Post-monsoon mists."}],
  ["Semilooper"], ["Use improved varieties: Phule Karale, IGP-76, RCR-18."])

c("coconut-oil", "Coconut Palm (Copra & Oil)", "नारळ / खोबरे (Narel / Khobare)", "Cocos nucifera", "Oilseeds", "🥥",
  "Perennial / Year-round", "Konkan (Sindhudurg, Ratnagiri, Raigad, Palghar)", "Tree of life (Kalpavriksha) producing pure copra oil for culinary, hair care, and wellness.",
  "24°C - 32°C", "1,300 - 2,000 mm.", "Coastal alluvium and lateritic soils.",
  [{"stage": "Seedling", "days": "Years 1-3", "description": "Nursery sprout establishment."},
   {"stage": "Trunk & Canopy", "days": "Years 4-6", "description": "Crown of pinnate fronds."},
   {"stage": "Inflorescence Spathe", "days": "Monthly", "description": "Spadix blooms with male and female button nuts."},
   {"stage": "Dry Nut Maturity", "days": "Months 11-12", "description": "Husk browns; rich copra kernel."}],
  [{"name": "Bud Rot (Phytophthora palmivora)", "symptoms": "Heart leaf withers and rots with foul smell.", "riskPeriod": "Heavy continuous monsoon rains."}],
  ["Rhinoceros Beetle", "Red Palm Weevil"], ["Apply Bordeaux paste to crown before monsoon.", "Install pheromone traps for Red Palm Weevil."])

c("oil-palm", "Oil Palm", "ऑइल पाम / तेल ताड (Oil Palm)", "Elaeis guineensis", "Oilseeds", "🌴",
  "Perennial", "Konkan coast, Coastal Andhra Pradesh, Tamil Nadu, Kerala", "Highest yielding edible oil crop per hectare in the world; fresh fruit bunches processed for crude palm oil.",
  "24°C - 32°C", "2,000 - 2,500 mm or assured drip.", "Deep, fertile friable loams.",
  [{"stage": "Vegetative", "days": "Years 1-3", "description": "Massive frond whorls form."},
   {"stage": "Bunch Bearing", "days": "Year 4 onwards", "description": "Dense fruit bunches in leaf axils."},
   {"stage": "Harvesting", "days": "Every 10-14 days", "description": "Bunches harvested when outer fruits turn reddish-orange."}],
  [{"name": "Basal Stem Rot (Ganoderma)", "symptoms": "Yellowing fronds and brackets at trunk base.", "riskPeriod": "Humid wet plantations."}],
  ["Rhinoceros Beetle"], ["Field sanitation and root feeding with bio-control Trichoderma."])

c("cottonseed-oil", "Cottonseed (Binola)", "सरकी (Sarki / Binola)", "Gossypium hirsutum (Seed)", "Oilseeds", "🌱",
  "Kharif byproduct", "Vidarbha, Marathwada, Khandesh", "Massive source of edible washed cottonseed oil and protein-dense cattle feed cake across Maharashtra.",
  "22°C - 32°C", "500 - 700 mm.", "Deep black cotton soils.",
  [{"stage": "Boll Maturation", "days": "Days 100-140", "description": "Seeds accumulate oil inside cotton bolls."},
   {"stage": "Ginning", "days": "Post-harvest", "description": "Lint separated from seed at ginning mills."}],
  [{"name": "Seed Rot", "symptoms": "Discolored seeds.", "riskPeriod": "Late unseasonal rains."}],
  ["Pink Bollworm in seed kernel"], ["Delinting and thorough seed drying to 9% moisture."])

c("chia-seed", "Chia Seed", "चिया सीड (Chia Seeds)", "Salvia hispanica", "Oilseeds", "🌱",
  "Rabi", "Experimental trials in Pune, Ahmednagar, MP, Rajasthan", "Ancient superfood packed with Omega-3 fatty acids, antioxidants, and mucilage fiber.",
  "16°C - 26°C", "350 - 450 mm.", "Sandy loam with excellent drainage.",
  [{"stage": "Vegetative", "days": "Days 1-40", "description": "Opposite serrated leaves."},
   {"stage": "Flowering Spikes", "days": "Days 41-75", "description": "Purple or white spicate blossoms."},
   {"stage": "Seed Harvest", "days": "Days 76-115", "description": "Tiny mottle-patterned seeds mature."}],
  [{"name": "Root Rot", "symptoms": "Wilting in heavy clay.", "riskPeriod": "Excess watering."}],
  ["Aphids"], ["Plant on raised beds to guarantee zero standing water."])

c("tarameera", "Taramira (Arugula Seed)", "तरामिर / तारा मीरा (Taramira)", "Eruca sativa", "Oilseeds", "🌱",
  "Rabi", "North Maharashtra, Rajasthan, Punjab dry areas", "Extremely drought and salt tolerant oilseed yielding pungent oil used for illumination, lubricating, and cattle.",
  "12°C - 22°C", "150 - 250 mm.", "Light sandy impoverished soils.",
  [{"stage": "Vegetative", "days": "Days 1-30", "description": "Lobed aromatic leaves."},
   {"stage": "Flowering", "days": "Days 31-65", "description": "Creamy veined flowers."},
   {"stage": "Harvest", "days": "Days 66-95", "description": "Siliquae harvested."}],
  [{"name": "Downy Mildew", "symptoms": "White patches.", "riskPeriod": "Winter fog."}],
  ["Aphids"], ["Grows with minimum moisture."])

c("canola-oilseed", "Canola (Low Erucic Mustard)", "कॅनोला (Canola)", "Brassica napus", "Oilseeds", "🌼",
  "Rabi", "Punjab, Haryana, experimental zones in Vidarbha", "Specially bred low-erucic acid mustard yielding healthy cooking oil with high smoke point.",
  "14°C - 24°C", "300 - 400 mm.", "Fertile loam.",
  [{"stage": "Vegetative", "days": "Days 1-35", "description": "Foliage canopy."},
   {"stage": "Flowering", "days": "Days 36-70", "description": "Yellow racemes."},
   {"stage": "Siliqua Filling", "days": "Days 71-110", "description": "Pods fill with dark round seeds."}],
  [{"name": "Sclerotinia Stem Rot", "symptoms": "Bleached white stem lesions with black sclerotia inside.", "riskPeriod": "Dense humid canopy."}],
  ["Aphids"], ["Foliar spray of Carbendazim at flowering if sclerotinia is prevalent."])

c("neem-seed-oil", "Neem Seed (Oil & Karanj)", "कडुनिंब बी / निंबोळी (Nimboli)", "Azadirachta indica", "Oilseeds", "🌿",
  "Summer Harvest", "Throughout Maharashtra & India", "Priceless botanical biopesticide and soil nitrifying inhibitor (Neem Coated Urea) derived from dried wild nimboli.",
  "20°C - 42°C", "Rainfed.", "All soil types.",
  [{"stage": "Flowering", "days": "March-April", "description": "Fragrant white floral panicles."},
   {"stage": "Fruiting", "days": "May-July", "description": "Green drupes turn golden yellow and drop."}],
  [{"name": "Dieback", "symptoms": "Twig drying.", "riskPeriod": "Rainy humidity."}],
  ["Tea Mosquito Bug"], ["Collect freshly fallen yellow nimboli and sun-dry on clean tarpaulins."])

c("mahua-seed-oil", "Mahua Seed (Tora / Moha)", "मोह / तोरा (Moha / Mahua Oil)", "Madhuca longifolia", "Oilseeds", "🌳",
  "Summer", "Vidarbha forest tracts (Gadchiroli, Chandrapur, Gondia), Melghat", "Forest oilseed yielding rich butter-like fat used for tribal cooking, soap making, and lighting.",
  "22°C - 40°C", "Rainfed.", "Forest hills.",
  [{"stage": "Fruiting", "days": "May-June", "description": "Fleshy berries fall containing large brown oily seeds."}],
  [{"name": "Fungal Rot", "symptoms": "Kernel decay.", "riskPeriod": "Damp storage."}],
  ["Weevils"], ["Sun-dry seeds thoroughly to prevent aflatoxin contamination."])

# ==========================================
# 4. CASH & COMMERCIAL CROPS (14 crops)
# ==========================================
c("sugarcane", "Sugarcane", "ऊस (Oos)", "Saccharum officinarum", "Cash & Commercial Crops", "🎋",
  "Annual / Adsali (12-18 months)", "Western Maharashtra (Kolhapur, Sangli, Pune, Satara, Ahmednagar), Marathwada",
  "The lifeline of Maharashtra cooperative agro-economy and sugar capital of India. Massive biomass grass yielding crystalline sucrose, jaggery (gul), and bagasse bio-power.",
  "20°C - 35°C (high sunshine and warm weather)", "1,500 - 2,500 mm; well-scheduled canal or drip irrigation essential.",
  "Deep, well-drained fertile clay loam or medium black cotton soil with pH 6.5 - 8.0.",
  [{"stage": "Germination & Sprouting", "days": "Days 1-35", "description": "Buds on 2-3 budded setts swell and push through furrow soil."},
   {"stage": "Formative & Tillering", "days": "Days 36-120", "description": "Heavy underground tillering creates 6-8 millable canes per clump."},
   {"stage": "Grand Growth & Elongation", "days": "Days 121-270", "description": "Rapid internode elongation, cane thickening, and massive green foliage expansion."},
   {"stage": "Ripening & Maturity", "days": "Days 271-360", "description": "Sugar synthesizes from top to bottom internodes; brix reaches 18-22%."}],
  [{"name": "Red Rot (Colletotrichum falcatum)", "symptoms": "Third or fourth leaf from top yellows, canes lose turgidity, pith displays longitudinal red lesions with white cross-bands and alcohol smell.", "riskPeriod": "Waterlogged fields following heavy monsoon rains."},
   {"name": "Sugarcane Smut (Sporisorium scitamineum)", "symptoms": "Terminal growing point transforms into a long curved black whip-like structure covered in sooty spores.", "riskPeriod": "Ratoon crops during hot dry spells."},
   {"name": "Grassy Shoot Disease (Phytoplasma)", "symptoms": "Profuse thin chlorotic shoots emerging from base giving witches' broom appearance without cane formation.", "riskPeriod": "Infected setts transmitted by aphids."}],
  ["Early Shoot Borer (Chilo infuscatellus)", "Internode Borer", "Top Borer", "Whitefly", "Root Grub (Holotrichia serrata)"],
  ["Use premier university varieties: Co-86032 (Nira), CoM-0265 (Phule 265), or MS-10001.",
   "Treat seed setts in hot water or fungicide bath (Carbendazim @ 1g/L) before planting.",
   "Adopt wide-row planting (4 to 5 feet) with drip fertigation to save 50% water and boost sucrose yields.",
   "Apply bio-agent Metarhizium anisopliae @ 5 kg/ha to eradicate devastating White grubs."])

c("cotton-bt", "Cotton (BT Kapas)", "कापूस (Kapas)", "Gossypium hirsutum", "Cash & Commercial Crops", "☁️",
  "Kharif", "Vidarbha (Yavatmal, Amravati, Akola, Wardha), Marathwada (Nanded, Jalna, Aurangabad), Khandesh (Jalgaon, Dhule)",
  "The white gold of Maharashtra. Major fiber crop driving rural livelihoods across the black cotton soils of Vidarbha, Khandesh, and Marathwada.",
  "22°C - 34°C (warm days, plenty of sunshine during boll bursting)", "600 - 850 mm; sensitive to waterlogging as well as prolonged drought at flowering.",
  "Deep, moisture-retentive black cotton soil (Vertisols) with good drainage, pH 6.5 - 8.0.",
  [{"stage": "Germination & Square Formation", "days": "Days 1-45", "description": "Deep taproot development; pyramidal branching; floral buds (squares) appear in leaf axils."},
   {"stage": "Flowering & Boll Initiation", "days": "Days 46-90", "description": "Creamy-white flowers bloom, turn pinkish-purple on day two after pollination; young bolls set."},
   {"stage": "Boll Development & Maturation", "days": "Days 91-135", "description": "Bolls expand accumulating fiber and oil; pink bollworm vulnerable period."},
   {"stage": "Boll Bursting & Picking", "days": "Days 136-180", "description": "Mature bolls dehisce exposing fluffy white lint; handpicked in 3-4 pickings."}],
  [{"name": "Cotton Leaf Curl Virus (CLCuV)", "symptoms": "Upward or downward leaf curling, vein thickening, and leafy enations on underside of leaves; whitefly vector.", "riskPeriod": "Hot weather with high whitefly activity."},
   {"name": "Bacterial Blight / Angular Leaf Spot (Xanthomonas citri pv. malvacearum)", "symptoms": "Angular water-soaked spots bounded by veins on leaves, black arm lesions on branches, water-soaked spots on bolls.", "riskPeriod": "Warm humid conditions with stormy wind-driven rains."},
   {"name": "Grey Mildew / Dahiya Disease (Ramularia areola)", "symptoms": "White powdery frost-like angular patches on lower leaf surface leading to premature leaf shedding.", "riskPeriod": "Post-monsoon cool nights with high morning humidity."}],
  ["Pink Bollworm (Pectinophora gossypiella)", "American Bollworm", "Whitefly", "Thrips", "Cotton Jassid (Amrasca biguttula)"],
  ["Install pheromone traps @ 5/ha for early Pink bollworm monitoring and @ 20/ha for mass trapping.",
   "Spray Flonicamid 50 WG @ 3g/10L for effective control of sucking pests (jassids and thrips).",
   "Avoid late-season extension of cotton crop beyond January to break the life cycle of Pink bollworm.",
   "Plant non-Bt border rows to delay pest resistance development."])

c("desi-cotton", "Desi Cotton (Tree Cotton)", "देशी कापूस (Desi Kapas)", "Gossypium arboreum", "Cash & Commercial Crops", "☁️",
  "Kharif", "Marathwada, Vidarbha rainfed dry belts", "Hardy indigenous cotton immune to sucking pests, drought, and requiring minimal chemical inputs. Highly valued for medical cotton and denim.",
  "25°C - 36°C", "450 - 600 mm.", "Medium to shallow black soils.",
  [{"stage": "Vegetative", "days": "Days 1-45", "description": "Sturdy bush."},
   {"stage": "Flowering", "days": "Days 46-90", "description": "Yellow blossoms with red centers."},
   {"stage": "Boll Bursting", "days": "Days 91-140", "description": "Fluffy lint bolls."}],
  [{"name": "Fusarium Wilt", "symptoms": "Yellowing and wilting.", "riskPeriod": "Damp soil."}],
  ["Spotted Bollworm"], ["Use varieties: PA-255 (Turab), PA-402, PKV DH-1."])

c("tobacco", "Tobacco", "तंबाखू (Tambakhu)", "Nicotiana tabacum", "Cash & Commercial Crops", "🍂",
  "Late Kharif / Rabi", "Kolhapur (Nipani border belt), Sangli, Gujarat border tracts",
  "Commercial leaf crop processed for bidi and chewing tobacco. Kolhapur-Nipani tract is famous across India for high-nicotine bidi tobacco.",
  "20°C - 30°C", "400 - 550 mm.", "Light sandy loam to well-drained medium black soil.",
  [{"stage": "Nursery & Transplanting", "days": "Days 1-45", "description": "Tiny seeds raised in nursery; transplanted."},
   {"stage": "Vegetative & Topping", "days": "Days 46-85", "description": "Rapid broad leaf growth; terminal flower head nipped (topped) to direct energy to leaves."},
   {"stage": "Desuckering & Maturation", "days": "Days 86-125", "description": "Axillary suckers removed; leaves turn thick leathery yellow-green with brown spangles."},
   {"stage": "Harvesting & Curing", "days": "Days 126-150", "description": "Leaves cut and sun-cured or pit-cured on ground."}],
  [{"name": "Tobacco Mosaic Virus (TMV)", "symptoms": "Mottling of light and dark green patches, leaf blistering and distortion.", "riskPeriod": "Mechanical contact during topping and desuckering."},
   {"name": "Black Shank (Phytophthora nicotianae)", "symptoms": "Black discoloration of stem base and discing of pith.", "riskPeriod": "Continuous damp soil."}],
  ["Tobacco Caterpillar (Spodoptera litura)", "Aphid", "Whitefly"],
  ["Wash hands with soap and trisodium phosphate before handling plants to prevent TMV spread.",
   "Use recommended bidi varieties: Anand-119, Vedaganga-1, or Bhagyashree."])

c("jute-tag", "Jute (Golden Fiber)", "ताग / पाट (Tag / Pat)", "Corchorus olitorius", "Cash & Commercial Crops", "🌾",
  "Kharif", "Eastern India (West Bengal, Bihar, Assam), Konkan river basins", "The biodegradable golden fiber of India used for burlap bags, geotextiles, rope, and eco-packaging.",
  "24°C - 35°C (high humidity)", "1,200 - 1,800 mm.", "Alluvial silt loam near river deltas.",
  [{"stage": "Vegetative Elongation", "days": "Days 1-90", "description": "Unbranched straight tall cylindrical stems reaching 3-4 meters."},
   {"stage": "Small Pod / Flowering", "days": "Days 91-120", "description": "Yellow small blossoms; harvested at 50% flowering for best fiber quality."},
   {"stage": "Retting", "days": "Post-harvest", "description": "Bundles submerged in slow-moving water for 15-20 days for microbial pectin breakdown."}],
  [{"name": "Stem Rot (Macrophomina phaseolina)", "symptoms": "Brown to black lesions on stem causing breaking.", "riskPeriod": "Hot waterlogged soil."}],
  ["Jute Semilooper", "Yellow Mite", "Hairy Caterpillar"],
  ["Harvest promptly at small pod stage to secure fine silky fiber tensile strength."])

c("mesta-ambadi", "Mesta (Ambadi / Roselle)", "अंबाडी / मेस्टा (Ambadi)", "Hibiscus sabdariffa", "Cash & Commercial Crops", "🌿",
  "Kharif", "Marathwada, Vidarbha, Khandesh", "Multipurpose commercial crop: tough bast fibers extracted from stems; tender tangy leaves cooked as Maharashtra's famous culinary 'Ambadi Bhaji'.",
  "22°C - 34°C", "500 - 700 mm.", "Medium to light soils.",
  [{"stage": "Vegetative", "days": "Days 1-45", "description": "Tender red/green stalks; culinary leaf picking."},
   {"stage": "Flowering & Calyx", "days": "Days 46-100", "description": "Large yellow flowers with crimson center; fleshy calyx forms."},
   {"stage": "Fiber Retting", "days": "Days 101-140", "description": "Stalks cut and retted for twine and rope."}],
  [{"name": "Foot & Stem Rot", "symptoms": "Dark rotting at base.", "riskPeriod": "Excess rain."}],
  ["Flea Beetle", "Mealybug"], ["Use varieties: AMV-5, AS-73-CP-560."])

c("sunn-hemp", "Sunn Hemp (San)", "सन / ताग (San / Sunnhemp)", "Crotalaria juncea", "Cash & Commercial Crops", "🌱",
  "Kharif & Summer", "Throughout Maharashtra (Western Maharashtra, Vidarbha, Marathwada)", "Premier fast-growing green manure and fiber crop. Fixes 100 kg nitrogen per hectare and decomposes in 45 days to rejuvenate tired soils.",
  "22°C - 34°C", "350 - 500 mm.", "Adaptable to all well-drained soils.",
  [{"stage": "Rapid Emergence", "days": "Days 1-20", "description": "Vigorous thick growth suppressing all weeds."},
   {"stage": "Green Manure Incorporation", "days": "Days 45-50", "description": "Ploughed into moist soil at succulent flowering stage."},
   {"stage": "Fiber Harvest", "days": "Days 80-100", "description": "Left to mature if tough cordage fiber is required."}],
  [{"name": "Vascular Wilt", "symptoms": "Drooping leaves.", "riskPeriod": "Warm soils."}],
  ["Sunnhemp Hairy Caterpillar"], ["Plough in at 50% bloom for maximum organic nitrogen synthesis."])

c("mulberry-sericulture", "Mulberry (Reshim / Tuti)", "तुती / रेशीम शेती (Tuti / Mulberry)", "Morus alba", "Cash & Commercial Crops", "🍃",
  "Perennial (Pruned 5 times a year)", "Western Maharashtra (Pune, Satara, Sangli, Solapur), Marathwada (Beed, Osmanabad)",
  "Commercial agro-enterprise feeding silkworms (Bombyx mori) to harvest lustrous white bivoltine silk cocoons. Provides continuous monthly farm cash flow.",
  "24°C - 30°C", "1,000 - 1,200 mm or regular drip.", "Deep, fertile well-drained loams, pH 6.5 - 7.5.",
  [{"stage": "Bottom Pruning", "days": "Day 1", "description": "Canes pruned close to ground to stimulate fresh succulent shoots."},
   {"stage": "Shoot Elongation", "days": "Days 2-35", "description": "Rapid growth of protein-dense glossy green leaves."},
   {"stage": "Leaf / Shoot Harvesting", "days": "Days 36-65", "description": "Canes harvested daily and fed to voracious 5th instar silkworms in rearing sheds."}],
  [{"name": "Leaf Spot (Cercospora moricola)", "symptoms": "Brown circular spots on foliage reducing silkworm palatability.", "riskPeriod": "Monsoon humidity."},
   {"name": "Powdery Mildew (Phyllactinia corylea)", "symptoms": "White powdery patches on leaf undersides.", "riskPeriod": "Cool winter months."}],
  ["Thrips", "Mealybug (Tukra disease causing bunched leaf tips)", "Whitefly"],
  ["Use high-yielding university varieties: V-1 (Victory-1), S-36, or G-4.",
   "Release predator beetles Cryptolaemus montrouzieri @ 250 adults/acre to eradicate Tukra mealybugs."])

c("betel-vine-paan", "Betel Vine (Paanvel)", "पानवेल / विड्याचे पान (Paanvel)", "Piper betle", "Cash & Commercial Crops", "🍃",
  "Perennial Shade Vine", "Sangli, Solapur, Pune, Raigad, Vasai, Amaravati", "High-value perennial shade-loving creeper yielding glossy heart-shaped aromatic betel leaves for traditional Vidya paan and digestive use.",
  "22°C - 30°C (cool, moist conservatory microclimate)", "Frequent light misting; shade conservatories (bareja) required.",
  "Rich, fertile well-aerated sandy loam with heavy compost, pH 7.0 - 7.5.",
  [{"stage": "Vine Training", "days": "Months 1-3", "description": "Trained on live supports of Shevri or Sesbania inside thatched shade huts."},
   {"stage": "Leaf Plucking", "days": "Every 15-20 days", "description": "Mature lustrous green leaves carefully snapped with fingernail."}],
  [{"name": "Foot Rot / Phytophthora Wilt", "symptoms": "Sudden leaf wilting and blackening of stem internodes.", "riskPeriod": "Monsoon moisture stagnation inside humid bareja."},
   {"name": "Anthracnose / Leaf Spot", "symptoms": "Dark circular spots with yellow halo.", "riskPeriod": "High humidity."}],
  ["Betelvine Bug", "Mealybug", "Nematodes"],
  ["Drench root base with Trichoderma harzianum and apply 1% Bordeaux mixture on lower vines.",
   "Ensure optimal ditch drainage around thatched conservatories."])

c("rubber", "Natural Rubber", "रबर (Rubber)", "Hevea brasiliensis", "Cash & Commercial Crops", "🌳",
  "Perennial Tree (Tapping from Year 7)", "Kerala, Coastal Konkan (Sindhudurg trials), South India",
  "Strategic commercial plantation tree tapped for liquid milky latex, the raw material for vehicle tires and industrial goods.",
  "25°C - 34°C", "2,000 - 3,000 mm evenly distributed.", "Deep, well-drained acidic lateritic soils.",
  [{"stage": "Immature Tree", "days": "Years 1-6", "description": "Grafted sapling reaches 50 cm trunk girth."},
   {"stage": "Tapping Phase", "days": "Year 7 to 30", "description": "Controlled spiral cut on bark; latex collected in coconut shell cups every alternate morning."}],
  [{"name": "Abnormal Leaf Fall (Phytophthora)", "symptoms": "Extensive defoliation during southwest monsoon.", "riskPeriod": "Heavy continuous rains."},
   {"name": "Pink Disease (Corticium salmonicolor)", "symptoms": "Pink crust on trunk forks.", "riskPeriod": "Wet foggy months."}],
  ["Scale Insects", "Termites"], ["Aerial or tractor spraying of copper oxychloride in oil before monsoon onset."])

c("lemongrass-commercial", "Lemongrass (Oil Distillation)", "गवती चहा / लेमनग्रास (Lemongrass)", "Cymbopogon flexuosus", "Cash & Commercial Crops", "🌾",
  "Perennial Grass (Harvested 4 times a year)", "Western Maharashtra, Vidarbha, Marathwada wasteland tracts",
  "Hardy aromatic grass distilled for pure citral-rich essential oil used in perfumes, soaps, vitamin A synthesis, and herbal tea.",
  "24°C - 35°C", "700 - 1,000 mm; survives severe drought.", "Poor, gravelly, eroded soils or reclaimed wastelands.",
  [{"stage": "Establishment", "days": "Days 1-60", "description": "Rooted slips planted on ridges."},
   {"stage": "First Harvest Cut", "days": "Day 90", "description": "Foliage cut 10 cm above ground."},
   {"stage": "Ratoon Cuts", "days": "Every 60-70 days", "description": "Regrowth cut and loaded into steam distillation stills."}],
  [{"name": "Rust (Puccinia nakanishikii)", "symptoms": "Brown pustules on foliage.", "riskPeriod": "Winter humidity."}],
  ["Stem Borer"], ["Distill freshly wilted grass within 24 hours of cutting."])

c("sisal-ghaypat", "Sisal (Ghaypat)", "घायपात (Ghaypat / Sisal)", "Agave sisalana", "Cash & Commercial Crops", "🌵",
  "Perennial Succulent", "Dry rain-shadow belts of Solapur, Ahmednagar, Marathwada bunds",
  "Extremely drought-resilient succulent providing industrial leaf fibers for marine ropes, dartboards, and agricultural boundary fencing.",
  "25°C - 40°C", "200 - 400 mm.", "Arid rocky calcareous soils.",
  [{"stage": "Rosette Growth", "days": "Years 1-3", "description": "Thick sword-like spiny leaves expand."},
   {"stage": "Leaf Cutting", "days": "Years 4-10", "description": "Lower leaves harvested for mechanical decortication."},
   {"stage": "Pole Flower & Bulbils", "days": "Year 10", "description": "Giant 6-meter flower pole emerges; plant dies leaving bulbils."}],
  [{"name": "Leaf Rot", "symptoms": "Soft rot in waterlogged soils.", "riskPeriod": "Excess rains."}],
  ["Sisal Weevil"], ["Plant along field boundaries to prevent soil erosion and keep stray livestock out."])

c("bamboo-commercial", "Bamboo (Green Gold)", "बांबू / मानगा (Manvel / Bamboo)", "Dendrocalamus strictus / Bambusa tulda", "Cash & Commercial Crops", "🎋",
  "Perennial Fast Growing", "Konkan (Sindhudurg Manga bamboo), Vidarbha forests, Western Ghats",
  "Wonder woody grass harvested for furniture, construction scaffolding, paper pulp, ethanol, and charcoal. Fast-growing carbon sink.",
  "20°C - 35°C", "1,200 - 2,500 mm.", "Well-drained hill soils and riverbanks.",
  [{"stage": "Clump Establishment", "days": "Years 1-3", "description": "Rhizome spread and shoot emergence."},
   {"stage": "Culm Hardening", "days": "Years 4 onwards", "description": "Canes mature; 3-year-old culms selectively harvested annually."}],
  [{"name": "Culm Rot", "symptoms": "Discolored shoots.", "riskPeriod": "Water stagnation."}],
  ["Bamboo Shoot Borer", "Powder Post Beetle"], ["Treat felled bamboo with Borax-Boric acid solution to prevent wood borers."])

c("indigo", "True Indigo", "नीळ (Neel / Indigo)", "Indigofera tinctoria", "Cash & Commercial Crops", "🌱",
  "Kharif / Annual", "Historical regions of Central and South India",
  "Historic natural blue dye plant cultivated for organic textile artisans and herbal hair color formulations.",
  "22°C - 32°C", "400 - 600 mm.", "Sandy loam with good drainage.",
  [{"stage": "Vegetative Growth", "days": "Days 1-60", "description": "Pinnate leaves expand."},
   {"stage": "Harvest at Bloom", "days": "Days 70-90", "description": "Cut at early flowering when indican glucoside peaks."}],
  [{"name": "Leaf Blight", "symptoms": "Brown patches.", "riskPeriod": "Cloudy weather."}],
  ["Caterpillar"], ["Steep freshly cut foliage in water tanks for microbial dye fermentation."])

print(f"Stage 3 loaded. Total now: {len(crops)}")

with open('scripts/crops_stage3.json', 'w', encoding='utf-8') as f:
    json.dump(crops, f, ensure_ascii=False, indent=2)
