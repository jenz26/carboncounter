import streamlit as st
from content import content
from pathlib import Path


def show_dashboard(lang="it"):
    """
    Renders the educational dashboard based on the selected topic and language.

    Args:
        lang (str): Language code ("it" or "en")
    """
    # === Sidebar ===
    st.sidebar.markdown("## 🧠 Dashboard")
    st.sidebar.markdown(
        "Esplora l'impatto delle attività digitali e approfondisci i dati ambientali." if lang == "it"
        else "Explore the impact of digital activities and dive into environmental data."
    )

    section_labels = {
        "why_individuals_matter": {
            "it": "Perché contiamo davvero",
            "en": "Why Every Individual Matters"
        },
        "data_centers": {
            "it": "Consumo dei Data Center",
            "en": "Data Center Consumption"
        },
        "data_transmission": {
            "it": "Trasmissione Dati",
            "en": "Data Transmission"
        },
        "device_lifecycle": {
            "it": "Ciclo di vita dei dispositivi",
            "en": "Device Lifecycle"
        },
        "reduction_strategies": {
            "it": "Strategie di riduzione",
            "en": "Reduction Strategies"
        }
    }

    sections = list(section_labels.keys())
    selected_label = st.sidebar.radio(
        "Vai a sezione:" if lang == "it" else "Go to section:",
        [section_labels[key][lang] for key in sections]
    )
    selected_key = [k for k in sections if section_labels[k][lang] == selected_label][0]

    # === Main layout ===
    st.title("📊 Dashboard di Approfondimento" if lang == "it" else "📊 In-Depth Dashboard")

    data = content[selected_key][lang]
    st.header(data.get("title", ""))
    st.markdown(data.get("body", ""))

    # Optional alerts and highlights
    if "info" in data:
        st.info(data["info"])
    if "success" in data:
        st.success(data["success"])
    if "warning" in data:
        st.warning(data["warning"])
    if "tip" in data:
        st.info(f"💡 {data['tip']}")

    # === Dynamic image ===
    if selected_key == "data_centers":
        img_path = Path(__file__).parent / "assets" / "pue_storico_2000_2023.png"
        if img_path.exists():
            st.image(str(img_path), caption=data.get("img_caption", ""))
        else:
            st.warning(
                f"⚠️ Unable to load local image. Ensure '{img_path.name}' exists in the 'assets' folder."
            )
    elif "img_caption" in data:
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Data_Center_Power_Usage_Effectiveness.svg/800px-Data_Center_Power_Usage_Effectiveness.svg.png",
            caption=data["img_caption"]
        )

    # === Sources ===
    st.markdown("---")
    st.markdown(
        "📚 **Fonti:** ADEME, Google, OpenAI, IEA, Shift Project, BioBambuItalia" if lang == "it"
        else "📚 **Sources:** ADEME, Google, OpenAI, IEA, Shift Project, BioBambuItalia"
    )
