#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Appends 56 Vegetable & Tuber crops across Maharashtra and India.
"""

import json

with open('scripts/crops_stage4.json', 'r', encoding='utf-8') as f:
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
# 6. VEGETABLES & TUBERS (56 crops)
# ==========================================
c("nashik-red-onion", "Onion (Nashik Red)", "नाशिक लाल कांदा (Nashik Kanda)", "Allium cepa", "Vegetables & Tubers", "🧅",
  "Kharif, Late Kharif (Rangada) & Rabi (Unalu)", "Nashik (Lasalgaon is Asia's largest onion market), Pune, Ahmednagar, Solapur, Dhule",
  "The culinary backbone of Indian cuisine holding GI status for Nashik Red Onion. Renowned for pungent sulfur flavor, tight crimson skin layers, and unmatched 6-month storage life in traditional chawls.",
  "15°C - 30°C (cool vegetative growth, warm sunny bulb enlargement and curing)",
  "450 - 650 mm through micro-sprinkler or drip; water withheld 15 days before harvest to seal bulbs.",
  "Deep, friable sandy loam or medium black cotton soil rich in organic humus, pH 6.5 - 7.8.",
  [{"stage": "Nursery & Transplanting", "days": "Days 1-50", "description": "Seedlings raised for 45-50 days; transplanted at 15x10 cm on flat or raised beds."},
   {"stage": "Vegetative Foliage Flush", "days": "Days 51-85", "description": "Active tubular hollow leaf production; photosynthesis drives bulb reserve accumulation."},
   {"stage": "Bulb Initiation & Swelling", "days": "Days 86-120", "description": "Leaf bases swell into tight fleshy concentric scales; critical moisture window."},
   {"stage": "Neck Fall & Curing", "days": "Days 121-140", "description": "50% tops fall naturally (neck fall); bulbs lifted and cured under field foliage for 4-5 days."}],
  [{"name": "Purple Blotch (Alternaria porri)", "symptoms": "Water-soaked lesions turning purple-brown with yellow halo on leaves and seed stalks.", "riskPeriod": "Warm humid conditions (25-30°C) with morning fog and dew."},
   {"name": "Stemphylium Leaf Blight", "symptoms": "Yellowish water-soaked oval spots rapidly coalescing into blighted tips.", "riskPeriod": "Post-monsoon overcast weather."},
   {"name": "Basal Rot / Collar Rot (Fusarium oxysporum f. sp. cepae)", "symptoms": "Progressive yellowing of leaf tips, basal plate rots with white fungal mycelium.", "riskPeriod": "High soil temperatures and poor drainage."}],
  ["Onion Thrips (Thrips tabaci)", "Maggot Fly (Delia antiqua)", "Cutworms", "Armyworm"],
  ["Spray Fipronil 5 SC @ 1.5ml/L or Profenofos @ 2ml/L with sticking agent for thrips control.",
   "Field cure bulbs thoroughly for 5-7 days before storing in ventilated wooden chawls.",
   "Use premier university varieties: Bhima Super, Bhima Red, Bhima Kiran (storage champ), or N-2-4-1.",
   "Apply 40 kg sulfur per hectare to boost onion pungency, scale color, and post-harvest shelf life."])

c("alibag-white-onion", "Alibag White Onion", "अलिबाग पांढरा कांदा (Alibag White Onion)", "Allium cepa", "Vegetables & Tubers", "🧅",
  "Rabi (Winter)", "Coastal Raigad (Alibag holding GI status)",
  "GI-tagged heritage coastal white onion celebrated for mild sweet taste, zero eye-burning sharpness, low pyruvic acid, and medicinal benefits for heart and insomnia.",
  "18°C - 28°C", "450 - 550 mm.", "Coastal sandy loam enriched with traditional organic fish manure.",
  [{"stage": "Nursery", "days": "Oct - Nov", "description": "Raised beds."},
   {"stage": "Bulbing", "days": "Jan - Feb", "description": "White bulb swelling."},
   {"stage": "Harvest", "days": "March", "description": "Hand harvested; braided into aesthetic hanging ropes (veni)."}],
  [{"name": "Purple Blotch", "symptoms": "Leaf spots.", "riskPeriod": "Humid mornings."}],
  ["Thrips"], ["Traditional organic cultivation using cow dung and local fish waste."])

c("potato-kufri-jyoti", "Potato (Kufri Jyoti)", "बटाटा (Kufri Jyoti Potato)", "Solanum tuberosum", "Vegetables & Tubers", "🥔",
  "Rabi in Plains / Kharif in Pune hills", "Western Maharashtra (Pune - Manchar & Khed, Satara), Nashik, UP, Punjab",
  "Widely cultivated staple potato producing oval, white-creamed, smooth-skinned tubers with pale yellow flesh, ideal for table boiling, curries, and chips.",
  "16°C - 22°C (cool nights below 18°C essential for underground tuber initiation)",
  "450 - 600 mm; well-spaced furrow irrigations; never allow ridges to dry out.",
  "Loose, friable sandy loam or well-drained silt loam rich in compost, pH 5.2 - 6.5.",
  [{"stage": "Sprouting & Emergence", "days": "Days 1-20", "description": "Sprouts emerge from seed eyes; roots establish."},
   {"stage": "Vegetative Canopy & Earthing Up", "days": "Days 21-45", "description": "Vigorous green leafy tops; soil hilled up around stems to bury stolons."},
   {"stage": "Tuber Initiation & Bulking", "days": "Days 46-75", "description": "Underground stolon tips swell into tubers; high water and potassium demand."},
   {"stage": "Senescence & Dehaulming", "days": "Days 76-95", "description": "Vines yellow; tops cut (dehaulmed) 10 days before digging to harden tuber skin."}],
  [{"name": "Late Blight (Phytophthora infestans)", "symptoms": "Water-soaked irregular dark lesions rotting leaves and stems rapidly with white downy mildew on undersides.", "riskPeriod": "Cool humid fog with night temperatures 12-18°C and relative humidity >90%."},
   {"name": "Early Blight (Alternaria solani)", "symptoms": "Concentric dark brown target rings on lower foliage with chlorotic halos.", "riskPeriod": "Warm alternating wet and dry spells."},
   {"name": "Common Scab (Streptomyces scabies)", "symptoms": "Rough corky lesions on tuber skin.", "riskPeriod": "Dry alkaline soil during tuber initiation."}],
  ["Potato Tuber Moth (Phthorimaea operculella)", "Aphids (Myzus persicae)", "Cutworms", "White Grubs"],
  ["Plant exclusively certified disease-free seed tubers.",
   "Hill up soil deeply to 25 cm to shield expanding tubers from greening and tuber moth oviposition.",
   "Spray Cymoxanil + Mancozeb (Curzate) @ 2g/L at first forecast of Late blight weather.",
   "Store tubers with neem leaves or sex pheromone traps to repel Potato tuber moth."])

c("potato-chipsona", "Processing Potato (Chipsona)", "चिप्स बटाटा (Chipsona Potato)", "Solanum tuberosum", "Vegetables & Tubers", "🥔",
  "Rabi", "Pune, Satara, Gujarat contract farming tracts",
  "Specialized industrial potato with high dry matter (>21%) and ultra-low reducing sugars (<0.1%) to prevent browning during potato chip frying.",
  "15°C - 22°C", "500 mm.", "Loose sandy loam.",
  [{"stage": "Bulking", "days": "Days 50-80", "description": "Starch accumulates."},
   {"stage": "Harvest", "days": "Days 90-105", "description": "Hard skin tubers dug."}],
  [{"name": "Late Blight", "symptoms": "Water-soaked rot.", "riskPeriod": "Foggy winter."}],
  ["Aphids"], ["Use Kufri Chipsona-1, Chipsona-3 varieties."])

c("tomato-narayangaon", "Tomato", "टोमॅटो (Narayangaon Tomato)", "Solanum lycopersicum", "Vegetables & Tubers", "🍅",
  "Kharif, Rabi & Summer", "Pune (Narayangaon is India's largest tomato market hub), Nashik, Satara, Ahmednagar",
  "High-yielding solanaceous vegetable producing firm, glossy red, lycopene-rich fruits grown on raised drip beds with wire trellising.",
  "20°C - 28°C", "500 - 700 mm; steady drip irrigation.", "Fertile, well-drained loam rich in organic matter, pH 6.0 - 7.0.",
  [{"stage": "Nursery & Trellising", "days": "Days 1-35", "description": "Seedlings transplanted; staked on wire trellises."},
   {"stage": "Flowering & Fruit Set", "days": "Days 36-65", "description": "Yellow blossoms open in clusters."},
   {"stage": "Fruit Development", "days": "Days 66-90", "description": "Green berries swell and firm up."},
   {"stage": "Harvesting", "days": "Days 91-140", "description": "Multiple pickings at breaker, pink, or red ripe stage."}],
  [{"name": "Early Blight (Alternaria solani)", "symptoms": "Target-board circular dark rings on lower leaves.", "riskPeriod": "Warm humid spells."},
   {"name": "Tomato Yellow Leaf Curl Virus (TYLCV)", "symptoms": "Upward cupping, yellow leaf margins, severe stunting; whitefly vector.", "riskPeriod": "Hot dry weather with whiteflies."},
   {"name": "Bacterial Wilt (Ralstonia solanacearum)", "symptoms": "Rapid green wilting of entire plant without initial leaf yellowing.", "riskPeriod": "Waterlogged warm soils."}],
  ["Fruit Borer (Helicoverpa armigera)", "Whitefly", "Leaf Miner (Liriomyza)", "Tuta absoluta (Tomato Pinworm)"],
  ["Install pheromone traps for Tuta absoluta and Helicoverpa.",
   "Spray Azoxystrobin + Difenoconazole @ 1ml/L for early and late blight.",
   "Use popular hybrids: Abhinav, US-440, Saaho, or Phule Raja."])

c("green-chilli", "Green Chilli (Mirchi)", "हिरवी मिरची (Mirchi)", "Capsicum annuum", "Vegetables & Tubers", "🌶️",
  "Year-round", "Kolhapur, Nandurbar, Nagpur, Solapur, Guntur (AP)",
  "Pungent spice and vegetable yielding slender fiery green pods rich in capsaicin and vitamin C.",
  "22°C - 32°C", "450 - 650 mm.", "Well-drained loam or medium black soil.",
  [{"stage": "Transplanting", "days": "Days 1-30", "description": "Seedlings established on ridges."},
   {"stage": "Flowering", "days": "Days 31-60", "description": "White star flowers."},
   {"stage": "Green Fruit Picking", "days": "Days 61-120", "description": "Pickings every 7-10 days."}],
  [{"name": "Chilli Leaf Curl Virus (Murda Disease)", "symptoms": "Upward curling (thrips) or downward curling (mites), stunted bushy canopy.", "riskPeriod": "Hot dry weather."},
   {"name": "Anthracnose / Dieback", "symptoms": "Sunken circular dark spots on fruits and dying of twigs from top.", "riskPeriod": "Warm humid rains."}],
  ["Thrips (Scirtothrips dorsalis)", "Yellow Mite", "Whitefly", "Fruit Borer"],
  ["Spray Diafenthiuron 50 WP @ 1g/L for thrips and mites to eradicate Murda curl disease.",
   "Use hybrids: Sitara, Teja-4, Jwala, or Phule Jyoti."])

c("brinjal-vangi", "Brinjal / Eggplant (Manjari Vangi)", "वांगी (Manjari / Jalgaon Vangi)", "Solanum melongena", "Vegetables & Tubers", "🍆",
  "Year-round", "Pune (Manjari), Jalgaon (famous Khandeshi Bharit Vangi), Kolhapur, Nagpur",
  "Beloved vegetable of Maharashtra; famous for purplish-green spiny 'Manjari' vangi and giant green 'Jalgaon' brinjal roasted for divine Baingan Bharta.",
  "22°C - 32°C", "500 - 700 mm.", "Deep fertile loam or clay loam.",
  [{"stage": "Transplanting", "days": "Days 1-30", "description": "Bush establishment."},
   {"stage": "Flowering", "days": "Days 31-60", "description": "Violet blossoms."},
   {"stage": "Fruit Harvest", "days": "Days 61-130", "description": "Glossy tender fruits picked."}],
  [{"name": "Little Leaf of Brinjal (Phytoplasma)", "symptoms": "Leaves become extremely tiny, chlorotic, and bushy with zero fruiting; leafhopper vector.", "riskPeriod": "High leafhopper activity."},
   {"name": "Phomopsis Blight", "symptoms": "Circular brown spots on leaves and soft fruit rot.", "riskPeriod": "Rains."}],
  ["Shoot and Fruit Borer (Leucinodes orbonalis)", "Jassids", "Epilachna Beetle"],
  ["Clip and destroy wilted drooping shoot tips harboring fruit borer larvae.",
   "Install Leucinodes pheromone traps @ 25/ha.",
   "Use varieties: Manjari Gota, Phule Harit, Pragati, or Krishna."])

c("okra-bhendi", "Okra / Ladyfinger (Bhendi)", "भेंडी (Bhendi)", "Abelmoschus esculentus", "Vegetables & Tubers", "🫛",
  "Kharif & Summer", "Throughout Maharashtra, Nashik, Pune, Thane, Vidarbha",
  "Popular mucilaginous pod vegetable producing tender green ridged fingers harvested every alternate day.",
  "25°C - 35°C", "400 - 550 mm.", "Well-drained fertile loam.",
  [{"stage": "Emergence", "days": "Days 1-25", "description": "Fast germination."},
   {"stage": "Flowering", "days": "Days 26-45", "description": "Creamy yellow flowers with maroon center."},
   {"stage": "Pod Picking", "days": "Days 46-90", "description": "Tender 3-4 inch pods picked daily."}],
  [{"name": "Yellow Vein Mosaic Virus (YVMV)", "symptoms": "Brilliant yellow vein clearing; veins turn entirely yellow; whitefly vector.", "riskPeriod": "Hot weather with whiteflies."},
   {"name": "Enation Leaf Curl Virus", "symptoms": "Upward curling and warty enations.", "riskPeriod": "Whitefly season."}],
  ["Shoot and Fruit Borer (Earias vittella)", "Jassids", "Whitefly"],
  ["Use resistant hybrids: Parbhani Kranti, Phule Utkarsha, Radhika, or Singham.",
   "Spray neem oil 1500 ppm regularly."])

c("cauliflower", "Cauliflower (Flower)", "फ्लॉवर / फुलकोबी (Cauliflower)", "Brassica oleracea var. botrytis", "Vegetables & Tubers", "🥦",
  "Winter (Rabi)", "Nashik, Pune, Satara, Kolhapur vegetable belts",
  "Crisp, dense, snow-white curds enclosed in protective inner wrapper leaves, high in fiber and vitamin C.",
  "15°C - 20°C (cool weather required for curd blanching and compactness)", "350 - 500 mm.", "Rich fertile loam rich in boron.",
  [{"stage": "Transplanting", "days": "Days 1-30", "description": "Rosette leaf expansion."},
   {"stage": "Curd Initiation", "days": "Days 31-60", "description": "Curd button forms inside inner leaves."},
   {"stage": "Curd Maturation", "days": "Days 61-85", "description": "Snow-white dense curd harvested before it ricens."}],
  [{"name": "Black Rot (Xanthomonas campestris)", "symptoms": "V-shaped yellow lesions on leaf margins with blackened veins.", "riskPeriod": "Warm wet spells."},
   {"name": "Whiptail (Molybdenum deficiency)", "symptoms": "Leaf blades fail to develop leaving thin whiplike midribs.", "riskPeriod": "Acidic soils."}],
  ["Diamondback Moth (Plutella xylostella)", "Cabbage Aphid"],
  ["Apply Borax @ 10 kg/ha and Ammonium molybdate @ 1 kg/ha.", "Spray Bt (Dipel) for Diamondback moth."])

c("cabbage", "Cabbage (Kobi)", "कोबी / पानकोबी (Cabbage)", "Brassica oleracea var. capitata", "Vegetables & Tubers", "🥬",
  "Winter", "Nashik, Pune, Satara, Kolhapur",
  "Dense, round, heavy heads composed of tightly overlapping smooth green leaves.",
  "14°C - 20°C", "350 - 500 mm.", "Moisture retentive loams.",
  [{"stage": "Vegetative", "days": "Days 1-35", "description": "Loose frame leaves."},
   {"stage": "Head Folding", "days": "Days 36-65", "description": "Central leaves cup and pack tightly."},
   {"stage": "Maturity", "days": "Days 66-90", "description": "Firm solid head harvested."}],
  [{"name": "Clubroot (Plasmodiophora brassicae)", "symptoms": "Spindle-shaped swollen root galls; daytime wilting.", "riskPeriod": "Acidic wet soil."}],
  ["Diamondback Moth", "Tobacco Caterpillar"], ["Apply lime to raise soil pH above 7.0 to prevent clubroot."])

c("knol-khol", "Knol Khol (Kohlrabi)", "गाठगोबी / नवलकोल (Knol Khol)", "Brassica oleracea var. gongylodes", "Vegetables & Tubers", "🥬",
  "Winter", "Pune, Nashik, Satara, North India",
  "Crisp globular swollen stem vegetable with sweet cabbage-turnip flavor.",
  "14°C - 22°C", "300 - 400 mm.", "Fertile sandy loam.",
  [{"stage": "Vegetative", "days": "Days 1-25", "description": "Stout stalk."},
   {"stage": "Knob Swelling", "days": "Days 26-55", "description": "Stem swells above ground into tender globe."},
   {"stage": "Harvest", "days": "Days 56-70", "description": "Picked tender before becoming fibrous."}],
  [{"name": "Damping Off", "symptoms": "Seedling collapse.", "riskPeriod": "Damp nursery."}],
  ["Aphids"], ["Use White Vienna or Purple Vienna varieties."])

c("capsicum-bell-pepper", "Capsicum / Bell Pepper (Shimla Mirchi)", "शिमला मिरची / ढोबळी मिरची (Capsicum)", "Capsicum annuum var. grossum", "Vegetables & Tubers", "🫑",
  "Year-round (Greenhouse & Open Field)", "Pune (Shirur, Junnar polyhouses), Satara, Nashik",
  "Blocky, thick-walled sweet peppers cultivated in green, yellow, and red varieties under shade nets and open fields.",
  "18°C - 26°C", "500 - 650 mm; drip fertigation.", "Rich porous loam with high organic compost.",
  [{"stage": "Vegetative", "days": "Days 1-35", "description": "Branching and staking."},
   {"stage": "Flowering & Fruit Set", "days": "Days 36-65", "description": "Bell-shaped white flowers; 4-lobed fruit setting."},
   {"stage": "Harvest", "days": "Days 66-120", "description": "Green blocky fruits or colored harvest at full red/yellow break."}],
  [{"name": "Powdery Mildew (Leveillula taurica)", "symptoms": "White fungal patches on leaf undersides with yellow chlorotic spots above.", "riskPeriod": "Warm dry spells inside polyhouse."},
   {"name": "Bacterial Spot", "symptoms": "Small brown water-soaked spots.", "riskPeriod": "High humidity."}],
  ["Thrips", "Broad Mites", "Whitefly"], ["Spray Abamectin @ 0.5ml/L for broad mites to prevent leaf downward curling."])

c("garlic-lasun", "Garlic (Lasun)", "लसूण (Lasun)", "Allium sativum", "Vegetables & Tubers", "🧄",
  "Rabi (Winter)", "Nashik, Ahmednagar, Pune, Khandesh, MP",
  "Pungent compound bulb composed of cloves (kudya) packed with medicinal allicin for cholesterol control and culinary seasoning.",
  "12°C - 25°C", "350 - 450 mm.", "Well-drained rich sandy loam, pH 6.0 - 7.5.",
  [{"stage": "Clove Sprouting", "days": "Days 1-20", "description": "Individual cloves planted root-down."},
   {"stage": "Vegetative Foliage", "days": "Days 21-70", "description": "Flat solid leaves expand."},
   {"stage": "Bulb Cloving & Maturation", "days": "Days 71-120", "description": "Cloves swell around central axis; tops turn brown and dry."},
   {"stage": "Curing", "days": "Days 121-135", "description": "Braided into bundles and cured in shade."}],
  [{"name": "Purple Blotch", "symptoms": "Purple leaf lesions.", "riskPeriod": "Winter humidity."},
   {"name": "White Rot (Sclerotium cepivorum)", "symptoms": "White fluffy fungus with black poppy-seed sclerotia at bulb base.", "riskPeriod": "Cold damp soil."}],
  ["Thrips"], ["Use high-yielding varieties: Phule Baswant, Bhima Omkar, G-282, or Yamuna Safed."])

c("ginger-ale", "Ginger (Ale)", "आले / अद्रक (Ale / Adrak)", "Zingiber officinale", "Vegetables & Tubers", "🫚",
  "8-9 Months Crop", "Satara (Wai, Koregaon is Ginger hub), Kolhapur, Sangli, Nanded, Kerala",
  "High-value aromatic rhizome crop yielding fiery gingerol oil used for fresh culinaries, dry sonth spice, and digestive wellness.",
  "22°C - 32°C (warm humid climate; shade-loving)", "1,200 - 1,500 mm through drip; raised beds mandatory.",
  "Deep, friable, well-aerated sandy loam rich in organic matter, pH 6.0 - 6.8.",
  [{"stage": "Rhizome Sprouting", "days": "Days 1-45", "description": "Mother rhizome setts planted on raised beds with drip; pseudostems emerge."},
   {"stage": "Tillering & Rhizome Expansion", "days": "Days 46-150", "description": "Fingers multiply horizontally in loose soil; heavy earthing up applied."},
   {"stage": "Rhizome Maturation", "days": "Days 151-240", "description": "Rhizomes accumulate pungency and starch; leaves yellow and dry."}],
  [{"name": "Rhizome Rot / Soft Rot (Pythium aphanidermatum)", "symptoms": "Water-soaked lesions on pseudostem base; foul-smelling soft decaying rhizomes.", "riskPeriod": "Monsoon waterlogging."},
   {"name": "Bacterial Wilt (Ralstonia solanacearum)", "symptoms": "Golden yellow leaf bronzing and milky bacterial stream from cut stem.", "riskPeriod": "Warm wet soils."}],
  ["Shoot Borer (Conogethes punctiferalis)", "Rhizome Scale"],
  ["Drench raised beds with Metalaxyl-Mancozeb @ 2.5g/L + Trichoderma to prevent devastating rhizome rot.",
   "Use certified varieties: Mahim, IISR Varada, or Rio de Janeiro."])

c("carrot-gajar", "Carrot (Gajar)", "गाजर (Gajar)", "Daucus carota", "Vegetables & Tubers", "🥕",
  "Rabi", "Pune, Nashik, Ahmednagar, North India",
  "Sweet crunchy taproot vegetable rich in beta-carotene; available as red Asiatic sweet carrots and orange European Nantes types.",
  "15°C - 20°C", "300 - 450 mm.", "Deep loose friable sandy loam free of stones.",
  [{"stage": "Emergence", "days": "Days 1-20", "description": "Feathery pinnate foliage."},
   {"stage": "Root Thickening", "days": "Days 21-65", "description": "Taproot penetrates and swells."},
   {"stage": "Harvest", "days": "Days 66-90", "description": "Plump crisp carrots pulled."}],
  [{"name": "Alternaria Leaf Blight", "symptoms": "Dark brown foliage spots.", "riskPeriod": "Humid periods."}],
  ["Carrot Rust Fly"], ["Use Pusa Kesar, Kuroda, or Super Kuroda varieties."])

c("radish-mula", "Radish (Mula)", "मुळा (Mula)", "Raphanus sativus", "Vegetables & Tubers", "🌱",
  "Year-round (Fast 35-45 days)", "Throughout Maharashtra & India",
  "Pungent crisp white root vegetable harvested in just 40 days; both root and green leaves (mulyachi bhaji) consumed.",
  "18°C - 26°C", "250 - 350 mm.", "Friable sandy loam.",
  [{"stage": "Vegetative & Root Swelling", "days": "Days 1-35", "description": "Rapid white taproot expansion."},
   {"stage": "Harvest", "days": "Days 36-50", "description": "Pulled while crisp before pithiness occurs."}],
  [{"name": "White Rust", "symptoms": "White pustules on leaves.", "riskPeriod": "Winter fog."}],
  ["Flea Beetle", "Aphids"], ["Use Pusa Chetki, Japanese White, or Phule Safed."])

c("beetroot", "Beetroot", "बीट (Beetroot)", "Beta vulgaris", "Vegetables & Tubers", "🫐",
  "Winter", "Pune, Nashik, Satara",
  "Deep ruby-red round root packed with betacyanin pigments, nitrates for cardiovascular stamina, and natural sugars.",
  "16°C - 22°C", "350 - 450 mm.", "Fertile sandy loam.",
  [{"stage": "Foliage", "days": "Days 1-30", "description": "Dark red-veined leaves."},
   {"stage": "Root Swelling", "days": "Days 31-65", "description": "Globe root swells."},
   {"stage": "Harvest", "days": "Days 66-80", "description": "Smooth round beets pulled."}],
  [{"name": "Cercospora Leaf Spot", "symptoms": "Circular spots with purple border.", "riskPeriod": "Rain."}],
  ["Leaf Miner"], ["Use Detroit Dark Red or Crimson Globe varieties."])

c("turnip-shalgam", "Turnip (Shalgam)", "शलजम / टर्निप (Shalgam)", "Brassica rapa subsp. rapa", "Vegetables & Tubers", "🥔",
  "Winter", "North India, Pune, Satara",
  "Cool-season white globe root with purple top, crisp pungent-sweet flesh.",
  "12°C - 20°C", "250 - 350 mm.", "Light sandy loam.",
  [{"stage": "Root Sizing", "days": "Days 20-45", "description": "Swollen globe root forms."},
   {"stage": "Harvest", "days": "Days 50-60", "description": "Harvested young."}],
  [{"name": "Clubroot", "symptoms": "Galls.", "riskPeriod": "Acid soils."}],
  ["Aphids"], ["Use Purple Top White Globe."])

c("spinach-palak", "Spinach (Palak)", "पालक (Palak)", "Spinacia oleracea / Beta vulgaris var. bengalensis", "Vegetables & Tubers", "🥬",
  "Year-round (Fast 25-30 days)", "Throughout Maharashtra & India",
  "Beloved tender leafy green packed with iron, folate, and calcium; continuous cut-and-come-again harvest.",
  "15°C - 25°C", "250 - 350 mm.", "Moist loamy soil.",
  [{"stage": "Foliage Expansion", "days": "Days 1-25", "description": "Broad succulent emerald leaves."},
   {"stage": "Multiple Pickings", "days": "Days 26-60", "description": "Harvested every 10-12 days."}],
  [{"name": "Cercospora Leaf Spot", "symptoms": "Spots on leaves.", "riskPeriod": "Humid spells."}],
  ["Aphids", "Leaf Miner"], ["Use All Green, Pusa Bharati, or Harit Shobha."])

c("fenugreek-methi", "Fenugreek Leaves (Methi)", "मेथी (Methi Bhaji)", "Trigonella foenum-graecum", "Vegetables & Tubers", "🌱",
  "Year-round", "Nashik, Pune, Ahmednagar, Marathwada",
  "Iconic fragrant green leaf vegetable of Maharashtra (Methi chi bhaji); high in fiber and blood sugar balancing trigonelline.",
  "15°C - 25°C", "250 - 300 mm.", "Well-drained loam.",
  [{"stage": "Quick Emergence", "days": "Days 1-7", "description": "Cotyledons emerge."},
   {"stage": "Vegetative Harvest", "days": "Days 21-30", "description": "Uprooted or cut at 4-6 inches height."}],
  [{"name": "Powdery Mildew", "symptoms": "White coating.", "riskPeriod": "Cool winter."}],
  ["Aphids"], ["Use Pusa Early Bunching or Kasturi Methi."])

c("coriander-kothimbir", "Coriander (Kothimbir)", "कोथिंबीर / धना (Kothimbir)", "Coriandrum sativum", "Vegetables & Tubers", "🌿",
  "Year-round", "Throughout Maharashtra, Nashik, Pune, Sangli",
  "Indispensable fresh garnishing herb yielding intoxicating linalool aroma; fast 35-45 day crop cycle.",
  "18°C - 26°C", "250 - 350 mm.", "Rich fertile loam.",
  [{"stage": "Emergence", "days": "Days 1-12", "description": "Split mericarps emerge."},
   {"stage": "Bushy Leaf Stage", "days": "Days 13-40", "description": "Aromatic feathery leaves harvested."}],
  [{"name": "Stem Gall (Protomyces macrosporus)", "symptoms": "Tumor-like swellings on stems.", "riskPeriod": "Cloudy humid weather."}],
  ["Aphids"], ["Use multi-cut varieties: Phule Mukta or CO-4."])

c("dill-shepu", "Dill Leaves (Shepu)", "शेपू (Shepu)", "Anethum graveolens", "Vegetables & Tubers", "🌿",
  "Year-round", "Western Maharashtra, Marathwada, Konkan",
  "Pungent, highly aromatic feathery green herb celebrated in traditional Maharashtrian garlic dal (Shepu chi bhaji).",
  "16°C - 26°C", "250 - 350 mm.", "Well-drained loam.",
  [{"stage": "Vegetative", "days": "Days 1-35", "description": "Feathery filiform leaves."},
   {"stage": "Harvest", "days": "Days 36-45", "description": "Cut fresh."}],
  [{"name": "Powdery Mildew", "symptoms": "White mold.", "riskPeriod": "Winter."}],
  ["Aphids"], ["Plant in successive fortnightly beds."])

c("amaranth-chaulai", "Amaranth Leaves (Chaulai / Tandulja)", "तांदुळजा / राजगिरा भाजी (Tandulja)", "Amaranthus tricolor", "Vegetables & Tubers", "🌿",
  "Summer & Kharif", "Throughout Maharashtra & India",
  "Heat-tolerant nutrient-rich ancient leafy green packed with iron, calcium, and beta-carotene; thrives under high temperatures.",
  "24°C - 35°C", "250 - 350 mm.", "All soils.",
  [{"stage": "Growth", "days": "Days 1-25", "description": "Red or green succulent leaves."},
   {"stage": "Multiple Cuttings", "days": "Days 26-55", "description": "Repeated foliage harvests."}],
  [{"name": "White Rust", "symptoms": "White blisters.", "riskPeriod": "Rains."}],
  ["Caterpillar"], ["Use Pusa Kiran or Pusa Lal Chaulai."])

c("colocasia-alu", "Colocasia (Alu / Arbi)", "अळू (Alu / Patra Leaves)", "Colocasia esculenta", "Vegetables & Tubers", "🥬",
  "Kharif & Summer", "Konkan Coast, Western Maharashtra, Thane, Pune",
  "Iconic heart-shaped elephant-ear leaves cooked for legendary Maharashtrian 'Aluwadi' (steamed spiced pinwheels) and tender starchy corms.",
  "22°C - 32°C", "1,200 - 1,500 mm; moisture loving.", "Heavy marshy loam rich in organic matter.",
  [{"stage": "Corm Sprouting", "days": "Days 1-30", "description": "Tubers send up giant peltate leaves."},
   {"stage": "Leaf Harvesting", "days": "Months 2-6", "description": "Periodic harvest of tender waxy leaves."},
   {"stage": "Corm Digging", "days": "Months 7-8", "description": "Starchy underground corms harvested."}],
  [{"name": "Leaf Blight (Phytophthora colocasiae)", "symptoms": "Water-soaked brown zonate lesions weeping yellow droplets.", "riskPeriod": "Heavy continuous monsoon rains."}],
  ["Aphids", "Spodoptera"], ["Use local sweet-leaf varieties devoid of calcium oxalate throat itch."])

c("bitter-gourd-karele", "Bitter Gourd (Karele)", "कारले (Karle)", "Momordica charantia", "Vegetables & Tubers", "🥒",
  "Kharif & Summer", "Pune, Nashik, Thane, Kolhapur",
  "Pungent bitter medicinal vegetable renowned for charantin and polypeptide-p insulin-like properties, grown on wire pandal trellises.",
  "24°C - 34°C", "400 - 600 mm.", "Well-drained loam.",
  [{"stage": "Vines on Trellis", "days": "Days 1-35", "description": "Vigorous tendril climbers."},
   {"stage": "Flowering & Pollination", "days": "Days 36-55", "description": "Yellow unisexual flowers."},
   {"stage": "Harvesting", "days": "Days 56-110", "description": "Crisp green warty fruits picked every 3-4 days."}],
  [{"name": "Downy Mildew", "symptoms": "Angular yellow spots.", "riskPeriod": "Humid spells."}],
  ["Fruit Fly (Bactrocera cucurbitae)"], ["Bag young fruits or install cue-lure pheromone traps."])

c("bottle-gourd-dudhi", "Bottle Gourd (Dudhi Bhopla)", "दुधी भोपळा (Dudhi Bhopla)", "Lagenaria siceraria", "Vegetables & Tubers", "🥒",
  "Kharif & Summer", "Throughout Maharashtra",
  "High-water content cylindrical or round pale-green gourd prized for light digestible curries, juice, and halwa.",
  "24°C - 34°C", "450 - 600 mm.", "Loamy soil.",
  [{"stage": "Vine Growth", "days": "Days 1-30", "description": "Trellised climbing vines."},
   {"stage": "Night Blooming", "days": "Days 31-50", "description": "White nocturnal flowers open at dusk."},
   {"stage": "Harvest", "days": "Days 51-90", "description": "Smooth tender gourds harvested."}],
  [{"name": "Powdery Mildew", "symptoms": "White coating.", "riskPeriod": "Winter."}],
  ["Fruit Fly"], ["Use varieties: Pusa Naveen, Samrat, or Phule Komal."])

c("ridge-gourd-dodka", "Ridge Gourd (Dodka / Shirale)", "दोडका / शिराळे (Dodka)", "Luffa acutangula", "Vegetables & Tubers", "🥒",
  "Kharif & Summer", "Pune, Nashik, Marathwada, Konkan",
  "Slender dark green gourd with prominent sharp longitudinal ridges and tender sweet sponge interior.",
  "24°C - 34°C", "400 - 550 mm.", "Fertile loam.",
  [{"stage": "Trellis", "days": "Days 1-30", "description": "Climbing."},
   {"stage": "Afternoon Bloom", "days": "Days 31-50", "description": "Yellow flowers bloom late afternoon."},
   {"stage": "Harvest", "days": "Days 51-90", "description": "Ridged tender fruits picked."}],
  [{"name": "Downy Mildew", "symptoms": "Foliar yellowing.", "riskPeriod": "Rain."}],
  ["Fruit Fly"], ["Use Phule Sucheta, Arka Sumeet."])

c("sponge-gourd-ghosale", "Sponge Gourd (Ghosale / Nenua)", "घोसाळे / गिल्के (Ghosale)", "Luffa aegyptiaca", "Vegetables & Tubers", "🥒",
  "Kharif", "Konkan, Western Maharashtra",
  "Smooth-skinned tender green gourd; fibrous vascular network inside mature dried fruit serves as natural loofah sponge.",
  "24°C - 35°C", "450 mm.", "Alluvial loam.",
  [{"stage": "Vines", "days": "Days 1-30", "description": "Rapid growth."},
   {"stage": "Harvest", "days": "Days 50-80", "description": "Smooth green fruits picked."}],
  [{"name": "Mosaic Virus", "symptoms": "Mottling.", "riskPeriod": "Whitefly."}],
  ["Epilachna Beetle"], ["Trellis on bower for straight fruits."])

c("snake-gourd-padwal", "Snake Gourd (Padwal)", "पडवळ (Padwal)", "Trichosanthes cucumerina", "Vegetables & Tubers", "🥒",
  "Kharif", "Konkan, Western Maharashtra, South India",
  "Spectacular elongated green-white striped twisting gourds reaching 1-1.5 meters, weighted with small stones to grow straight.",
  "24°C - 32°C", "500 mm.", "Rich loam.",
  [{"stage": "Foliage", "days": "Days 1-35", "description": "Bower climbing."},
   {"stage": "Night Bloom", "days": "Days 36-55", "description": "Exquisite white fringed lace-like flowers."},
   {"stage": "Harvest", "days": "Days 56-90", "description": "Long tender snake-like fruits."}],
  [{"name": "Fruit Rot", "symptoms": "Decay.", "riskPeriod": "Rains."}],
  ["Fruit Fly"], ["Use varieties: Kaumudi, PKM-1."])

c("ivy-gourd-tondli", "Ivy Gourd (Tondli / Kundru)", "तोंडली (Tondli)", "Coccinia grandis", "Vegetables & Tubers", "🥒",
  "Perennial Vine", "Pune, Thane, Raigad, Vasai",
  "Perennial dioecious climbing vine producing crisp small cylindrical green-striped gourds picked weekly for 3-4 years.",
  "22°C - 34°C", "600 - 800 mm.", "Deep loam with compost.",
  [{"stage": "Stem Cutting Establishment", "days": "Months 1-3", "description": "Stem cuttings trained on permanent bower."},
   {"stage": "Continuous Harvest", "days": "Years 1 to 4", "description": "Harvested every 3-4 days."}],
  [{"name": "Downy Mildew", "symptoms": "Yellow leaf spots.", "riskPeriod": "Humid periods."}],
  ["Gall Fly"], ["Maintain 1:10 male to female plant ratio on bower."])

c("pointed-gourd-parwal", "Pointed Gourd (Parwal)", "परवळ (Parwal)", "Trichosanthes dioica", "Vegetables & Tubers", "🥒",
  "Spring to Autumn", "Eastern India, Bihar, UP, experimental in Maharashtra",
  "High-value nutritious gourd with firm sweet pulp and soft seeds, celebrated in North and East Indian cuisine.",
  "25°C - 35°C", "800 mm.", "Riverbed sandy loam.",
  [{"stage": "Vine Canopy", "days": "Months 1-3", "description": "Vegetative."},
   {"stage": "Harvest", "days": "Months 4-8", "description": "Striped oval fruits picked."}],
  [{"name": "Fruit Rot", "symptoms": "Watery decay.", "riskPeriod": "Monsoon."}],
  ["Fruit Fly"], ["Propagate through mature vine cuttings."])

c("ash-gourd-kohla", "Ash Gourd (Kohla / Petha)", "कोहळा / पेठा (Kohla)", "Benincasa hispida", "Vegetables & Tubers", "🍈",
  "Kharif", "Throughout Maharashtra & India",
  "Large oblong melon with white chalky waxy coating; historic staple for cooling digestive wellness and famous Agra Petha confection.",
  "24°C - 34°C", "500 mm.", "Well-drained loam.",
  [{"stage": "Trailing", "days": "Days 1-45", "description": "Heavy ground runner."},
   {"stage": "Wax Coating & Harvest", "days": "Days 90-130", "description": "White chalky wax seals fruit for 1-year shelf life."}],
  [{"name": "Downy Mildew", "symptoms": "Leaf spots.", "riskPeriod": "Rains."}],
  ["Fruit Fly"], ["White wax coating makes it store for 12 months without refrigeration."])

c("pumpkin-lal-bhopla", "Red Pumpkin (Lal Bhopla)", "लाल भोपळा (Lal Bhopla)", "Cucurbita moschata", "Vegetables & Tubers", "🎃",
  "Kharif & Summer", "Throughout Maharashtra",
  "Heavy ribbed golden-orange squash rich in beta-carotene, used for puran poli savory stuffing and temple feasts.",
  "22°C - 34°C", "450 mm.", "All soils.",
  [{"stage": "Vine", "days": "Days 1-40", "description": "Massive runners."},
   {"stage": "Harvest", "days": "Days 80-110", "description": "Stems turn woody and corky."}],
  [{"name": "Powdery Mildew", "symptoms": "White powder.", "riskPeriod": "Dry spells."}],
  ["Red Pumpkin Beetle"], ["Use Arka Chandan or Pusa Vikas."])

c("drumstick-moringa", "Drumstick (Moringa / Shevga)", "शेवगा (Shevga)", "Moringa oleifera", "Vegetables & Tubers", "🫛",
  "Year-round bearing (Peak twice a year)", "Ahmednagar, Solapur, Pune, Marathwada, South India",
  "The miracle superfood tree. Yields long tender pods for sambar and nutrient-dense leaves rich in 7x vitamin C of oranges and 4x calcium of milk.",
  "25°C - 38°C (thrives in drought and heat)", "350 - 550 mm; zero waterlogging.", "Well-drained sandy loam or rocky gravelly soils.",
  [{"stage": "Rapid Shoot Growth", "days": "Months 1-3", "description": "Shoots reach 2 meters; topped at 1 meter to stimulate heavy lateral branches."},
   {"stage": "Creamy White Blossom", "days": "Months 4-5", "description": "Fragrant honey-scented flower panicles."},
   {"stage": "Pod Elongation & Harvest", "days": "Months 6-8", "description": "Slender pods grow up to 60-75 cm; picked tender before seeds harden."}],
  [{"name": "Pod Rot / Anthracnose", "symptoms": "Brown patches rotting developing pods.", "riskPeriod": "Monsoon rains."},
   {"name": "Twig Dieback", "symptoms": "Drying twigs.", "riskPeriod": "Water stagnation."}],
  ["Moringa Hairy Caterpillar (Eupterote mollifera)", "Pod Fly (Gitona distigma)", "Bud Midge"],
  ["Plant high-yielding annual varieties: PKM-1, PKM-2, ODC-3, or Bhagya (KDM-1).",
   "Apply light soil trenching and annual pruning after harvest to maintain bushy accessible canopy."])

c("sweet-potato-ratale", "Sweet Potato (Ratale)", "रताळे (Ratale)", "Ipomoea batatas", "Vegetables & Tubers", "🍠",
  "Kharif & Rabi", "Solapur, Satara, Kolhapur, Konkan",
  "Nutritious tuberous root staple eaten roasted or boiled during fasting (Upwas Ratale); rich in beta-carotene and complex carbs.",
  "20°C - 30°C", "500 - 700 mm.", "Loose sandy loam with great friability.",
  [{"stage": "Vine Cutting Planting", "days": "Days 1-20", "description": "Terminal vine cuttings planted on ridges."},
   {"stage": "Tuber Swelling", "days": "Days 50-90", "description": "Adventitious roots swell into purple/red-skinned tubers."},
   {"stage": "Harvest", "days": "Days 105-120", "description": "Leaves yellow; tubers lifted with forks."}],
  [{"name": "Black Rot", "symptoms": "Dark sunken tuber rot.", "riskPeriod": "Excess rain."}],
  ["Sweet Potato Weevil (Cylas formicarius)"], ["Use vine cuttings dipped in chlorpyrifos; varieties: Sree Bhadra, Varsha."])

c("elephant-foot-yam-suran", "Elephant Foot Yam (Suran)", "सुरण (Suran)", "Amorphophallus paeoniifolius", "Vegetables & Tubers", "🥔",
  "8-9 Months", "Konkan Coast, Western Maharashtra, South India",
  "Massive underground corm weighing up to 5-10 kg, highly prized for savory festival curries and traditional digestive health.",
  "24°C - 35°C", "1,200 - 1,800 mm.", "Deep fertile loose loam rich in organic compost.",
  [{"stage": "Sprouting", "days": "Days 1-45", "description": "Corm setts planted; umbrella-like spotted pseudostem emerges."},
   {"stage": "Corm Bulking", "days": "Months 4-7", "description": "Massive underground corm enlargement."},
   {"stage": "Harvest", "days": "Months 8-9", "description": "Foliage withers completely; corms dug."}],
  [{"name": "Collar Rot (Sclerotium)", "symptoms": "Soft rot at soil line.", "riskPeriod": "Monsoon waterlogging."}],
  ["Nematodes"], ["Plant non-acrid variety Gajendra."])

c("tapioca-cassava", "Tapioca (Cassava / Shabu)", "कसावा / साबुदाणा कंद (Cassava)", "Manihot esculenta", "Vegetables & Tubers", "🥔",
  "9-10 Months", "Kerala, Tamil Nadu, Konkan, Coastal India",
  "Drought-hardy starchy root tuber processed into India's beloved Sabudana pearls.",
  "24°C - 35°C", "1,000 - 1,500 mm.", "Laterite and sandy loam.",
  [{"stage": "Stem Sett Planting", "days": "Days 1-30", "description": "Woody stem stakes planted."},
   {"stage": "Tuber Filling", "days": "Months 4-8", "description": "Radial tubers swell with pure starch."},
   {"stage": "Harvest", "days": "Months 9-10", "description": "Heavy tubers harvested."}],
  [{"name": "Cassava Mosaic Virus", "symptoms": "Severe leaf mosaic; whitefly vector.", "riskPeriod": "Whitefly season."}],
  ["Red Spider Mites"], ["Use virus-free stem cuttings; varieties: Sree Padmanabha, H-226."])

c("cucumber-kakdi", "Cucumber (Kakdi)", "काकडी (Sheetal Kakdi)", "Cucumis sativus", "Vegetables & Tubers", "🥒",
  "Kharif & Summer", "Pune, Nashik, Thane, Solapur",
  "Crisp, cooling, high-water salad vegetable producing refreshing green cylindrical fruits in 45-50 days.",
  "22°C - 32°C", "350 - 450 mm.", "Well-drained sandy loam.",
  [{"stage": "Vegetative", "days": "Days 1-25", "description": "Rapid vine growth."},
   {"stage": "Flowering & Fruiting", "days": "Days 26-45", "description": "Yellow flowers; rapid fruit elongation."},
   {"stage": "Harvest", "days": "Days 46-75", "description": "Tender crisp cucumbers picked every alternate day."}],
  [{"name": "Downy Mildew", "symptoms": "Angular yellow patches.", "riskPeriod": "Dewy mornings."},
   {"name": "Powdery Mildew", "symptoms": "White coating.", "riskPeriod": "Dry spells."}],
  ["Fruit Fly", "Red Pumpkin Beetle"], ["Use Sheetal, Poinsette, or Phule Shubhangi."])

c("broccoli", "Broccoli", "ब्रोकोली (Broccoli)", "Brassica oleracea var. italica", "Vegetables & Tubers", "🥦",
  "Winter", "Pune (Khed, Junnar), Nashik, Satara",
  "Exotic dark emerald cruciferous head packed with sulforaphane antioxidant and vitamins, grown for premium urban retail.",
  "14°C - 20°C", "350 - 450 mm.", "Fertile loam.",
  [{"stage": "Transplanting", "days": "Days 1-30", "description": "Rosette canopy."},
   {"stage": "Head Formation", "days": "Days 31-60", "description": "Central dense green head develops."},
   {"stage": "Harvest", "days": "Days 61-75", "description": "Cut compact head before flower buds open."}],
  [{"name": "Black Rot", "symptoms": "V-shaped lesions.", "riskPeriod": "Humidity."}],
  ["Diamondback Moth"], ["Grow Green Magic or Marathon hybrids."])

c("zucchini", "Zucchini (Summer Squash)", "झुकिनी (Zucchini)", "Cucurbita pepo", "Vegetables & Tubers", "🥒",
  "Winter & Early Summer", "Pune, Satara, Nashik exotic vegetable clusters",
  "Bush squash producing glossy dark green or golden cylindrical tender fruits harvested young for gourmet cooking.",
  "18°C - 26°C", "350 mm.", "Rich loam.",
  [{"stage": "Bush Growth", "days": "Days 1-25", "description": "Non-trailing compact bush."},
   {"stage": "Harvest", "days": "Days 40-65", "description": "Harvested small (6-8 inches) with flower attached."}],
  [{"name": "Powdery Mildew", "symptoms": "White mold.", "riskPeriod": "Dry days."}],
  ["Aphids"], ["Use Cora or Green Beauty varieties."])

c("lettuce", "Lettuce (Iceberg & Romaine)", "लेट्युस (Lettuce)", "Lactuca sativa", "Vegetables & Tubers", "🥬",
  "Winter & Polyhouse", "Pune, Mahabaleshwar, Nilgiris, Nashik",
  "Crisp leafy salad vegetable cultivated for crunchy Iceberg heads and tender butterhead leaves for salad bowls.",
  "12°C - 20°C (cool temperatures prevent bitter bolting)", "300 mm.", "Rich organic sandy loam.",
  [{"stage": "Vegetative", "days": "Days 1-30", "description": "Leaf rosettes."},
   {"stage": "Heading", "days": "Days 31-55", "description": "Crisp head forms."},
   {"stage": "Harvest", "days": "Days 56-70", "description": "Cut at soil line."}],
  [{"name": "Tipburn (Calcium deficiency)", "symptoms": "Browning of inner leaf margins.", "riskPeriod": "Rapid growth."}],
  ["Aphids", "Slugs"], ["Maintain steady calcium and moisture."])

c("celery", "Celery", "सेलरी (Celery)", "Apium graveolens", "Vegetables & Tubers", "🥬",
  "Winter", "Pune, Ooty, Himachal",
  "Crisp, fibrous, aromatic ribbed stalks used in gourmet soups, salads, and slimming juices.",
  "14°C - 22°C", "450 mm.", "Rich moist muck loam.",
  [{"stage": "Stalk Elongation", "days": "Days 1-70", "description": "Tight cluster of ribbed petioles."},
   {"stage": "Blanching & Harvest", "days": "Days 71-100", "description": "Cut crisp heads."}],
  [{"name": "Early Blight", "symptoms": "Brown specks.", "riskPeriod": "Humid."}],
  ["Leaf Miner"], ["Blanch stalks by wrapping paper 2 weeks before harvest."])

c("parsley", "Parsley", "पार्सले (Parsley)", "Petroselinum crispum", "Vegetables & Tubers", "🌿",
  "Winter", "Pune, Ooty, polyhouses",
  "Bright green curly or flat-leaf herb packed with iron, vitamin K, and fresh herbal aroma.",
  "14°C - 24°C", "300 mm.", "Fertile loam.",
  [{"stage": "Harvest", "days": "Days 60-120", "description": "Periodic cutting of outer foliage."}],
  [{"name": "Leaf Spot", "symptoms": "Specks.", "riskPeriod": "Rain."}],
  ["Aphids"], ["Use Moss Curled or Italian Flat Leaf."])

c("mint-pudina", "Mint (Pudina)", "पुदिना (Pudina)", "Mentha spicata", "Vegetables & Tubers", "🌿",
  "Year-round", "Throughout Maharashtra & India",
  "Aromatic perennial herb spreading via stolons; refreshing menthol leaves essential for pani puri, chutneys, and biryani.",
  "18°C - 30°C", "Moisture loving.", "Rich moist loam.",
  [{"stage": "Stolon Spread", "days": "Days 1-30", "description": "Fast runners."},
   {"stage": "Continuous Harvest", "days": "Every 25-30 days", "description": "Cut leafy stalks."}],
  [{"name": "Mint Rust", "symptoms": "Orange pustules.", "riskPeriod": "Damp."}],
  ["Hairy Caterpillar"], ["Water regularly; partial shade enhances aroma."])

c("curry-leaves", "Curry Leaf (Kadi Patta)", "कढीपत्ता (Kadi Patta)", "Murraya koenigii", "Vegetables & Tubers", "🍃",
  "Perennial Shrub", "Throughout Maharashtra, Western Ghats, South India",
  "The soul of Indian tadka (tempering). Aromatic pinnate leaves rich in carbazole alkaloids and iron.",
  "22°C - 35°C", "Rainfed once established.", "Well-drained loam.",
  [{"stage": "Pruning & Flush", "days": "Year-round", "description": "Harvested branches stimulate fresh aromatic flushes."}],
  [{"name": "Leaf Spot", "symptoms": "Brown spots.", "riskPeriod": "Monsoon."}],
  ["Citrus Butterfly Caterpillar", "Psyllid"], ["Prune bushes to 1 meter height twice a year."])

c("spring-onion", "Spring Onion (Scallions)", "कांदा पात (Kanda Paat)", "Allium fistulosum / A. cepa", "Vegetables & Tubers", "🌱",
  "Year-round", "Pune, Nashik, peri-urban farms",
  "Crisp, hollow tubular green shoots with small tender white bulbs, used in stir-fries and street foods.",
  "15°C - 25°C", "300 mm.", "Fertile loam.",
  [{"stage": "Growth", "days": "Days 1-45", "description": "Tubular leaves."},
   {"stage": "Harvest", "days": "Days 45-60", "description": "Pulled in bunches with roots."}],
  [{"name": "Thrips", "symptoms": "Silvery streaks.", "riskPeriod": "Dry spells."}],
  ["Cutworm"], ["Harvest before bulbing starts."])

c("sweet-corn-veg", "Sweet Corn", "गोड मका (Sweet Corn)", "Zea mays var. saccharata", "Vegetables & Tubers", "🌽",
  "Year-round", "Pune (Manchar), Nashik, Kolhapur",
  "Specialty corn with high sugar content harvested at milk stage for fresh sweet boiling, roasting, and salads.",
  "20°C - 30°C", "450 - 550 mm.", "Fertile loam.",
  [{"stage": "Silking to Milk Stage", "days": "Days 55-75", "description": "Silks turn brown; kernels full of sweet milky juice."},
   {"stage": "Harvest", "days": "Days 75-80", "description": "Harvested at dawn for same-day retail."}],
  [{"name": "Blight", "symptoms": "Lesions.", "riskPeriod": "Humid."}],
  ["Fall Armyworm"], ["Use Sugar-75 or Madhu varieties."])

c("yardlong-bean", "Yardlong Bean (Borboti)", "चवळी शेंग / लांब शेंग (Yardlong Bean)", "Vigna unguiculata subsp. sesquipedalis", "Vegetables & Tubers", "🫛",
  "Kharif & Summer", "Konkan, Western Maharashtra",
  "Extra-long tender climbing bean producing 60-90 cm green pods harvested continuously.",
  "24°C - 35°C", "450 mm.", "Loamy soil.",
  [{"stage": "Trellising & Pods", "days": "Days 45-90", "description": "Enormous hanging pods picked tender."}],
  [{"name": "Anthracnose", "symptoms": "Pod spots.", "riskPeriod": "Rains."}],
  ["Aphids"], ["Use varieties: Arka Mangala, Lola."])

c("raw-banana-veg", "Raw Green Banana (Cooking Plantain)", "कच्ची केळी (Kachhi Keli)", "Musa paradisiaca", "Vegetables & Tubers", "🍌",
  "Year-round", "Konkan, Khandesh, South India",
  "Starchy unripened plantain banana cooked as savory vegetable, chips, and koftas.",
  "25°C - 35°C", "1,800 mm.", "Fertile clay loam.",
  [{"stage": "Bunch Harvest", "days": "Month 10", "description": "Fingers harvested fully filled but dark green."}],
  [{"name": "Sigatoka", "symptoms": "Leaf spots.", "riskPeriod": "Rains."}],
  ["Weevil"], ["Use Nendran or Monthan varieties."])

c("button-mushroom", "Button Mushroom (Dhingri / Alambi)", "अळंबी / बटन मशरूम (Button Mushroom)", "Agaricus bisporus", "Vegetables & Tubers", "🍄",
  "Controlled Climate", "Pune, Baramati, Satara, Solapur indoor farms",
  "Indoor cultivated white edible fungi grown on pasteurized compost beds under controlled temperature (16-18°C) and casing soil.",
  "16°C - 20°C (air-conditioned growing rooms)", "Humid misting (85-90% RH).", "Wheat straw / paddy straw pasteurized compost with casing.",
  [{"stage": "Spawn Run", "days": "Days 1-14", "description": "White mycelium colonizes compost."},
   {"stage": "Casing & Pinhead", "days": "Days 15-25", "description": "Peat casing layer triggers pinhead formation."},
   {"stage": "Harvesting", "days": "Days 26-60", "description": "Buttons plucked at tight veil stage in 3-4 flushes."}],
  [{"name": "Dry Bubble (Verticillium fungicola)", "symptoms": "Deformed puffy mushrooms covered in greyish mould.", "riskPeriod": "Poor hygiene in cropping room."},
   {"name": "Wet Bubble (Mycogone perniciosa)", "symptoms": "Foul-smelling decaying cauliflower-like masses weeping amber liquid.", "riskPeriod": "Contaminated casing soil."}],
  ["Sciarid Flies", "Phorid Flies", "Mites"],
  ["Maintain strict HEPA air filtration and room sanitation.", "Steam pasteurize casing soil at 65°C for 6 hours."])

c("oyster-mushroom", "Oyster Mushroom (Dhingri)", "धिंगरी अळंबी (Dhingri Mushroom)", "Pleurotus ostreatus / P. sajor-caju", "Vegetables & Tubers", "🍄",
  "Year-round in Shade", "Throughout Maharashtra rural agro-enterprises",
  "Fastest-growing edible mushroom cultivated in polythene bags filled with boiled wheat/paddy straw.",
  "22°C - 30°C", "80-85% humidity.", "Sterilized wheat or paddy straw.",
  [{"stage": "Spawn Colonization", "days": "Days 1-15", "description": "Dense white mycelium binds straw into solid block."},
   {"stage": "Fruiting Flushes", "days": "Days 16-35", "description": "Grey/white oyster shell clusters burst from bag cuts; harvested fresh."}],
  [{"name": "Green Mold (Trichoderma)", "symptoms": "Green contamination on straw.", "riskPeriod": "Improper straw sterilization."}],
  ["Mushroom Flies"], ["Soak and boil straw at 80°C for 1 hour before spawning."])

c("lotus-root-kamal-kakdi", "Lotus Root (Kamal Kakdi)", "कमळ काकडी / भें (Kamal Kakdi)", "Nelumbo nucifera", "Vegetables & Tubers", "🪷",
  "Autumn / Winter", "Lakes of Kashmir, Vidarbha, Bihar, MP",
  "Aquatic edible rhizome with wheel-like air hollows; crisp texture used for Kashmiri Rogan Josh and crunchy stir-fries.",
  "20°C - 32°C", "Standing aquatic lake water (30-60 cm).", "Lake mud and silt.",
  [{"stage": "Aquatic Growth", "days": "Months 1-5", "description": "Floating round leaves; pink/white lotus bloom."},
   {"stage": "Rhizome Digging", "days": "Months 6-8", "description": "Segmented hollow rhizomes harvested from lake bottom mud."}],
  [{"name": "Rhizome Rot", "symptoms": "Decaying corms.", "riskPeriod": "Stagnant foul water."}],
  ["Aquatic Snails"], ["Grown naturally in freshwater ponds and wetlands."])

c("water-chestnut-singhara", "Water Chestnut (Singhara)", "शिंगाडा (Singhada)", "Trapa natans", "Vegetables & Tubers", "🌰",
  "Winter (Oct - Jan)", "Lakes of Vidarbha (Bhandara, Gondia), UP, MP",
  "Floating aquatic plant yielding horned triangular nuts with crisp, sweet, starchy white kernel eaten raw or boiled for fasting flour.",
  "22°C - 32°C", "Freshwater lakes.", "Aquatic pond silt.",
  [{"stage": "Floating Mat", "days": "Monsoon", "description": "Rosette of floating rhombic leaves."},
   {"stage": "Harvest", "days": "Oct - Jan", "description": "Spiny green-purple fruits picked from boats."}],
  [{"name": "Leaf Blight", "symptoms": "Foliar rot.", "riskPeriod": "Rains."}],
  ["Singhara Beetle (Galerucella birmanica)"], ["Spray neem-based formulations on water surface against beetles."])

c("turmeric-rhizome-veg", "Fresh Turmeric Rhizome (Oli Halad)", "ओली हळद (Fresh Green Turmeric)", "Curcuma longa", "Vegetables & Tubers", "🫚",
  "Winter", "Sangli, Satara, Kolhapur, Nanded",
  "Freshly dug knobby golden-orange rhizomes pickled in lemon juice and salt or cooked into seasonal fresh turmeric subzi.",
  "22°C - 32°C", "1,200 mm.", "Rich fertile loam.",
  [{"stage": "Maturity", "days": "Months 8-9", "description": "Dug fresh with fragrant golden fingers."}],
  [{"name": "Rhizome Rot", "symptoms": "Soft rot.", "riskPeriod": "Waterlogging."}],
  ["Shoot Borer"], ["Wash clean and store in cool dry sand."])

print(f"Stage 5 loaded. Total now: {len(crops)}")

with open('scripts/crops_stage5.json', 'w', encoding='utf-8') as f:
    json.dump(crops, f, ensure_ascii=False, indent=2)
