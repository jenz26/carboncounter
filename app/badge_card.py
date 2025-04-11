import streamlit as st

# Define the badge levels based on daily CO₂ impact
BADGES = [
    {
        "min": 0.0,
        "max": 0.5,
        "title": {"it": "Asceta digitale", "en": "Digital Ascetic"},
        "desc": {
            "it": "Hai uno stile di vita digitale impeccabile.",
            "en": "You live a perfectly minimal digital life."
        },
        "icon": "🧘‍♀️",
        "color": "#1b5e20",
        "bg_color": "#e8f5e9",
        "score": 10
    },
    {
        "min": 0.5,
        "max": 1.2,
        "title": {"it": "Consapevole", "en": "Conscious"},
        "desc": {
            "it": "Il tuo impatto digitale è sotto controllo.",
            "en": "Your digital impact is under control."
        },
        "icon": "🌱",
        "color": "#388e3c",
        "bg_color": "#f1f8e9",
        "score": 8
    },
    {
        "min": 1.2,
        "max": 2.5,
        "title": {"it": "Equilibrista", "en": "Balancer"},
        "desc": {
            "it": "Sei sulla linea di confine, ma bilanciato.",
            "en": "You're walking the line, but balanced."
        },
        "icon": "🤹‍♂️",
        "color": "#f9a825",
        "bg_color": "#fffde7",
        "score": 6
    },
    {
        "min": 2.5,
        "max": 3.5,
        "title": {"it": "Distratto", "en": "Unaware"},
        "desc": {
            "it": "Serve un po' più di attenzione alle tue abitudini.",
            "en": "Time to reflect a bit on your habits."
        },
        "icon": "😅",
        "color": "#ef6c00",
        "bg_color": "#fff3e0",
        "score": 4
    },
    {
        "min": 3.5,
        "max": float("inf"),
        "title": {"it": "Ingordo di byte", "en": "Data Devourer"},
        "desc": {
            "it": "Le tue emissioni digitali sono altine...",
            "en": "Your digital emissions are quite high..."
        },
        "icon": "🐙",
        "color": "#c62828",
        "bg_color": "#ffebee",
        "score": 2
    }
]

def get_badge_data(co2: float) -> dict:
    """
    Returns the badge configuration matching the user's CO2 value.
    
    Parameters:
        co2 (float): Daily CO2 footprint in kg.
    
    Returns:
        dict: Badge data (icon, title, description, etc.)
    """
    for badge in BADGES:
        if badge["min"] <= co2 < badge["max"]:
            return badge
    return BADGES[-1]  # Fallback if no match

def render_badge_card(co2: float, lang: str):
    """
    Renders a badge card in Streamlit based on the user's CO2 impact.
    
    Parameters:
        co2 (float): Daily CO2 footprint in kg.
        lang (str): Language code ("it" or "en").
    """
    badge = get_badge_data(co2)

    st.markdown(f"""
        <div style="
            max-width: 700px;
            margin: 1rem auto;
            border-radius: 12px;
            border: 2px solid {badge['color']};
            background-color: {badge['bg_color']};
            padding: 1.5rem 2rem;
            color: #111;
            text-align: center;">
            
            <h2 style='margin-bottom: 0.5rem;'>
                {badge['icon']} <span style='color: {badge['color']};'>Badge:</span>
                <strong style='font-size: 1.5rem;'>{badge['title'][lang]}</strong>
            </h2>

            <p style='margin: 0.3rem 0;'>📊 
                <strong style='color: #444;'>Punteggio ambientale:</strong> {badge['score']} / 10
            </p>
            
            <p style='margin: 0.3rem 0;'>💬 {badge['desc'][lang]}</p>
        </div>
    """, unsafe_allow_html=True)
