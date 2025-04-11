"""
Educational content used in the dashboard, supporting multiple languages (IT/EN).
Each section contains:
- title: a string with optional emoji
- body: markdown-supported informative content
- optionally: tip / info / warning / success / img_caption
"""

content = {
    "why_individuals_matter": {
        "it": {
            "title": "🌍 Perché ogni singolo individuo conta",
            "body": """
Molti credono che l'inquinamento digitale sia colpa solo delle grandi aziende, dei data center, dei voli intercontinentali... ma la verità è che **l'impatto collettivo nasce da milioni di piccole azioni quotidiane**. Ogni scroll, ogni mail, ogni stream ha un'impronta.

Se un miliardo di persone guarda 10 video YouTube al giorno, l'impatto è enorme. **Tu sei parte dell'equazione.**

👉 Il tuo contributo, anche se piccolo, **fa la differenza**.
""",
            "info": "Un video in 4K da 2 ore consuma fino a 7 kWh, come un viaggio in auto di 45 minuti.",
            "success": "Un'email senza allegato = 0.3 gCO₂, ma se ne mandi 100 al giorno, diventano 110 kg CO₂ l'anno!"
        },
        "en": {
            "title": "🌍 Why Every Individual Matters",
            "body": """
Many believe digital pollution is solely caused by big companies, data centers, intercontinental flights... but the truth is that **collective impact comes from millions of small daily actions**. Every scroll, email, and stream has a footprint.

If a billion people watch 10 YouTube videos a day, the impact is huge. **You are part of the equation.**

👉 Your contribution, even if small, **makes a difference**.
""",
            "info": "A 2-hour 4K video consumes up to 7 kWh, similar to a 45-minute car trip.",
            "success": "A plain email = 0.3 gCO₂. If you send 100 a day, it adds up to 110 kg CO₂ per year!"
        }
    },

    "data_centers": {
        "it": {
            "title": "🏢 Energia e Data Center",
            "body": """
La crescita dell'intelligenza artificiale e dei servizi cloud sta portando a un aumento vertiginoso del consumo energetico dei data center.

- I data center consumeranno il **2% dell'energia mondiale nel 2025**, con possibile raddoppio entro il 2030.
- L'**IA generativa** sta accelerando questo trend.
- In Europa, la domanda energetica dei data center potrebbe crescere del **30% entro il 2030**.

💡 **PUE medio globale**: 1.56 (nuovi impianti: 1.3 o meno)
""",
            "img_caption": "Metrica PUE (Power Usage Effectiveness)"
        },
        "en": {
            "title": "🏢 Energy and Data Centers",
            "body": """
The rise of artificial intelligence and cloud services is dramatically increasing data center energy consumption.

- Data centers will use **2% of global energy by 2025**, potentially doubling by 2030.
- **Generative AI** is accelerating this trend.
- In Europe, data center energy demand may rise by **30% by 2030**.

💡 **Global average PUE**: 1.56 (new sites: 1.3 or lower)
""",
            "img_caption": "PUE Metric (Power Usage Effectiveness)"
        }
    },

    "data_transmission": {
        "it": {
            "title": "📡 Trasmissione Dati e Reti",
            "body": """
La trasmissione dei dati ha un'impronta che dipende **dal tipo di rete**:

| Tipo di Rete       | Consumo Energetico (kWh/GB) |
|--------------------|-----------------------------|
| Fibra Ottica       | 0.00002 - 0.1               |
| Rame               | Intermedio                  |
| Reti Mobili (2G-5G)| 0.12 - 0.22                 |

🔌 Le reti mobili consumano **fino a 10x** rispetto alla fibra!
""",
            "tip": "Suggerimento: quando possibile, connettiti via WiFi (fibra) invece del 5G per ridurre l'impatto."
        },
        "en": {
            "title": "📡 Data Transmission and Networks",
            "body": """
Data transmission footprint depends **on the type of network**:

| Network Type       | Energy Use (kWh/GB)         |
|--------------------|-----------------------------|
| Fiber Optic        | 0.00002 - 0.1               |
| Copper             | Intermediate                |
| Mobile Networks    | 0.12 - 0.22                 |

🔌 Mobile networks consume **up to 10x more** than fiber!
""",
            "tip": "Tip: whenever possible, connect via WiFi (fiber) instead of 5G to reduce your impact."
        }
    },

    "device_lifecycle": {
        "it": {
            "title": "💻 Emissioni dei Dispositivi Digitali",
            "body": """
I dispositivi che usiamo ogni giorno hanno **una forte impronta di produzione**, spesso più dell'uso:

- 📱 Smartphone: **63 kg CO₂/anno**, di cui 80% dalla produzione  
- 💻 Laptop: **110 kg CO₂** solo per la produzione  
- 🖥️ Desktop + schermo: **778 kg CO₂** su 6 anni  

🔄 Solo il 15% degli smartphone viene riciclato.
""",
            "warning": "Allunga la vita del tuo dispositivo: ripara, aggiorna, evita upgrade frequenti."
        },
        "en": {
            "title": "💻 Emissions of Digital Devices",
            "body": """
The devices we use every day have **a high production footprint**, often more than usage:

- 📱 Smartphone: **63 kg CO₂/year**, 80% from manufacturing  
- 💻 Laptop: **110 kg CO₂** just for production  
- 🖥️ Desktop + monitor: **778 kg CO₂** over 6 years  

🔄 Only 15% of smartphones are recycled.
""",
            "warning": "Extend your device's life: repair, update, and avoid frequent upgrades."
        }
    },

    "reduction_strategies": {
        "it": {
            "title": "🧩 Strategie per ridurre l'impronta",
            "body": """
- 📉 **Riduci lo streaming ad alta risoluzione** quando non necessario  
- 📬 **Evita allegati email pesanti**, usa link cloud  
- 💡 **Attiva modalità risparmio energia** su smartphone e laptop  
- 🔌 **Stacca i caricabatterie** inutilizzati  
- 🧹 **Pulisci inbox, cloud, app inutilizzate**  
- 🌿 **Scegli fornitori green** (hosting, cloud)  

Ogni azione conta. Scegline una e inizia oggi. 💪
"""
        },
        "en": {
            "title": "🧩 Strategies to Reduce Your Footprint",
            "body": """
- 📉 **Lower HD/4K streaming quality** when not needed  
- 📬 **Avoid heavy email attachments**, use cloud links  
- 💡 **Enable power saving mode** on phones and laptops  
- 🔌 **Unplug unused chargers**  
- 🧹 **Clean inboxes, cloud, and unused apps**  
- 🌿 **Choose green providers** (hosting, cloud)  

Every action counts. Pick one and start today. 💪
"""
        }
    }
}
