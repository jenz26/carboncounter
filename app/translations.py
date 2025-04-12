translations = {
    "title": {
        "it": "Calcola la tua impronta digitale",
        "en": "Calculate your digital footprint"
    },
    "mode": {
        "it": "Modalità:",
        "en": "Mode:"
    },
    "simple": {
        "it": "Semplificata",
        "en": "Simplified"
    },
    "mode": {
    "it": "Modalità",
    "en": "Mode"
    },
    "mode_simple": {
        "it": "Semplificata",
        "en": "Simple"
    },
    "mode_advanced": {
        "it": "Avanzata",
        "en": "Advanced"
    },
    "advanced": {
        "it": "Avanzata",
        "en": "Advanced"
    },
    "total": {
        "it": "🌿 La tua impronta stimata è {co2:.2f} kg di CO₂",
        "en": "🌿 Your estimated footprint is {co2:.2f} kg of CO₂"
    },
    "equiv": {
        "it": "🌈 Equivalenze creative:",
        "en": "🌈 Creative equivalences:"
    },
    "eq_drive": {
        "it": "- 🚗 **{km:.1f} km** percorsi in auto (media EU)",
        "en": "- 🚗 **{km:.1f} km** driven (EU average)"
    },
    "eq_meat": {
        "it": "- 🍔 **{meals:.1f} pasti** a base di carne",
        "en": "- 🍔 **{meals:.1f} meat-based meals**"
    },
    "eq_social": {
        "it": "- 📱 **{hours:.0f} ore** di social media scroll",
        "en": "- 📱 **{hours:.0f} hours** of social media scrolling"
    },
    "eq_flight": {
        "it": "- ✈️ **{mins:.1f} minuti** di volo (tratta breve)",
        "en": "- ✈️ **{mins:.1f} minutes** of short-haul flight"
    },
    "eq_led": {
        "it": "- 💡 **{hours:.0f} ore** di lampadina LED accesa",
        "en": "- 💡 **{hours:.0f} hours** of LED light on"
    },
    "eq_gaming": {
        "it": "- 🎮 **{hours:.1f} ore** di cloud gaming",
        "en": "- 🎮 **{hours:.1f} hours** of cloud gaming"
    },
    "eq_amazon": {
        "it": "- 📦 **{boxes:.1f} pacchi** spediti da Amazon",
        "en": "- 📦 **{boxes:.1f} Amazon packages** shipped"
    },
    "forest": {
        "it": "🌳 Riforestazione equivalente:",
        "en": "🌳 Forest compensation:"
    },
    "eq_tree": {
        "it": "- 🌲 **{trees:.1f} alberi** per compensarla in 1 giorno",
        "en": "- 🌲 **{trees:.1f} trees** to absorb this in 1 day"
    },
    "eq_bamboo": {
        "it": "- 🎍 **{area:.0f} m² di bambù** per assorbirla in 1 giorno",
        "en": "- 🎍 **{area:.0f} m² of bamboo** to absorb it in 1 day"
    },
    "bio_bamboo_link": {
        "it": "👉 Vuoi compensare davvero? Scopri il progetto **[BioBambuItalia](https://www.biobambuzeroco2.it/)** per piantare bambù in modo sostenibile!",
        "en": "👉 Want to really compensate? Discover the **[BioBambuItalia](https://www.biobambuzeroco2.it/)** project to plant sustainable bamboo!"
    },
    "tips_title": {
        "it": " 💡 Come ridurre la tua impronta:",
        "en": " 💡 How to reduce your footprint:"
    },
    "tips_text": {
        "it": """
- Riduci la qualità dello streaming  
- Evita allegati pesanti via email  
- Usa audio invece di videochiamate dove possibile  
- Preferisci fornitori green (cloud, hosting)  
- Pulisci regolarmente la tua inbox e storage  
""",
        "en": """
- Lower your video streaming quality  
- Avoid heavy email attachments  
- Prefer audio over video calls when possible  
- Choose green cloud/hosting providers  
- Regularly clean your inbox and cloud storage  
"""
    }
}

def t(key: str, lang: str = "it") -> str:
    """Returns the translation for a given key and language. Defaults to Italian."""
    return translations.get(key, {}).get(lang, key)
