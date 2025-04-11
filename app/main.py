# main.py
# Main entry point for the CarbonCounter Streamlit application

import streamlit as st
import json
from pathlib import Path
from translations import t
from translations_label import get_label_and_desc
from dashboard import show_dashboard
from co2_calc import calculate_emissions
from badge_card import render_badge_card

# === Streamlit Page Configuration ===
st.set_page_config(page_title="CarbonCounter", layout="wide")

# === Load Estimates from JSON ===
@st.cache_data
def load_estimates():
    data_path = Path(__file__).resolve().parent.parent / "data" / "co2_estimates.json"
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)

estimates = load_estimates()

# === Initialize Session State ===
if "step" not in st.session_state:
    st.session_state.step = "input"
if "user_input" not in st.session_state:
    st.session_state.user_input = {}
if "total_emissions_kg" not in st.session_state:
    st.session_state.total_emissions_kg = 0.0

# === Sidebar Configuration ===
with st.sidebar:
    lang = st.radio(
        "🌍 Lingua / Language", 
        ["it", "en"], 
        format_func=lambda l: "Italiano 🇮🇹" if l == "it" else "English 🇬🇧"
    )
    st.markdown("## 🌿 CarbonCounter")
    st.write({
        "it": "Scopri quanto pesa la tua vita digitale in termini di CO₂.",
        "en": "Find out how much your digital life weighs in terms of CO₂."
    }[lang])
    st.markdown("[by Marco Contin](https://www.linkedin.com/in/contin-marco-padova/)")

# === INPUT STEP ===
if st.session_state.step == "input":
    st.title(t("title", lang))
    mode = st.radio("Modalità", ["Semplificata", "Avanzata"], horizontal=True)

    keys_basic = [
        "email_simple", "email_attachment_small", "google_search",
        "streaming_hd", "chatbot_query", "download_gb"
    ]

    keys_advanced_groups = {
        "🌐 Navigazione & Email": [
            "email_simple", "email_attachment_small", "google_search", "web_browsing"
        ],
        "🎵 Streaming": [
            "streaming_music", "streaming_sd", "streaming_hd", "streaming_4k"
        ],
        "💬 Messaggistica & Comunicazioni": [
            "instant_msg_text", "instant_msg_photo", "instant_msg_video",
            "sms", "videocall_1to1", "videocall_group"
        ],
        "🧠 Intelligenza Artificiale": [
            "chatbot_query", "image_gen_ai", "ai_software_hour"
        ],
        "☁️ Cloud & Download": [
            "download_gb", "cloud_storage_gb_month"
        ],
        "🎮 Gaming & Entertainment": [
            "gaming_online", "gaming_cloud"
        ],
        "🛒 Shopping & IoT": [
            "ads_view", "ecommerce_purchase", "iot_device_day"
        ]
    }

    selected_keys = keys_basic if mode == "Semplificata" else [k for group in keys_advanced_groups.values() for k in group]
    time_related_keys = [k for k in selected_keys if any(x in k for x in ["hour", "streaming", "videocall", "gaming"])]

    for group_title, group_keys in (keys_advanced_groups.items() if mode == "Avanzata" else {"Activities": keys_basic}.items()):
        with st.expander(group_title, expanded=False):
            for key in group_keys:
                label_data = get_label_and_desc(key, lang)
                label = label_data.get("label", key)
                help_text = label_data.get("descrizione", "")
                max_val = 24 if any(x in key for x in ["hour", "streaming", "videocall", "gaming"]) else 500
                st.session_state.user_input[key] = st.slider(
                    label,
                    0,
                    max_val,
                    int(st.session_state.user_input.get(key, 0)),
                    help=help_text,
                    key=f"slider_{key}"
                )

    total_hours = sum(st.session_state.user_input.get(k, 0) for k in time_related_keys)

    if total_hours > 16:
        st.warning(
            f"⚠️ Sei un super multitasker!\nOcchio però: l'OMS consiglia di dormire almeno 8 ore al giorno... ti restano solo {24 - total_hours}h per tutto il resto! 😴"
        )

    with st.form(key="form_submit"):
        submitted = st.form_submit_button({
            "it": "Calcola la mia impronta 🌍",
            "en": "Calculate my footprint 🌍"
        }[lang])

        if submitted:
            st.session_state.total_emissions_kg = calculate_emissions(st.session_state.user_input, estimates) / 1000
            st.session_state.step = "result"
            st.rerun()

    st.stop()

# === RESULT STEP ===
elif st.session_state.step == "result":
    co2 = st.session_state.total_emissions_kg
    st.title(t("total", lang).format(co2=co2))

    render_badge_card(co2, lang)

    st.markdown(t("equiv", lang))
    st.markdown(t("eq_drive", lang).format(km=co2 * 5))
    st.markdown(t("eq_meat", lang).format(meals=co2 * 0.333))
    st.markdown(t("eq_social", lang).format(hours=co2 * 12))
    st.markdown(t("eq_flight", lang).format(mins=co2 / 0.254))
    st.markdown(t("eq_led", lang).format(hours=co2 * 50))
    st.markdown(t("eq_gaming", lang).format(hours=co2 * 5))
    st.markdown(t("eq_amazon", lang).format(boxes=co2 / 0.5))

    st.subheader(t("forest", lang))
    trees_needed = co2 / 0.0575
    bamboo_area_m2 = co2 / 0.219
    st.markdown(t("eq_tree", lang).format(trees=trees_needed))
    st.markdown(t("eq_bamboo", lang).format(area=bamboo_area_m2))
    st.markdown(t("bio_bamboo_link", lang))

    st.markdown("---")
    st.subheader("📚 " + {
        "it": "Vuoi capire *perché* queste attività hanno un impatto?",
        "en": "Want to understand *why* these activities have an impact?"
    }[lang])

    if st.button("👉 " + {
        "it": "Vai alla Dashboard Educativa",
        "en": "Go to the Educational Dashboard"
    }[lang]):
        st.session_state.step = "dashboard"
        st.rerun()

    st.markdown("---")
    st.subheader(t("tips_title", lang))
    st.markdown(t("tips_text", lang))

    if st.button({
        "it": "🖙 Ricalcola",
        "en": "🖙 Recalculate"
    }[lang]):
        st.session_state.step = "input"
        st.rerun()

    st.stop()

# === DASHBOARD STEP ===
elif st.session_state.step == "dashboard":
    show_dashboard(lang)

    st.markdown("---")
    if st.button({
        "it": "🖙 Torna al calcolatore",
        "en": "🖙 Back to calculator"
    }[lang]):
        st.session_state.step = "input"
        st.rerun()

    st.stop()
