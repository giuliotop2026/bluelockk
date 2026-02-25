import streamlit as st
from openai import OpenAI

# --- GRAFICA DA SALOON (BLINDATA) ---
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(rgba(244, 236, 207, 0.85), rgba(244, 236, 207, 0.85)),
        url('https://images.unsplash.com/photo-1528563351349-3397da0533d1?q=80&w=2070&auto=format&fit=crop');
        background-size: cover; background-position: center; background-attachment: fixed;
        color: #5d4037; font-family: 'Georgia', serif;
    }
    .stButton>button { background-color: #d32f2f !important; color: white !important; font-weight: bold; width: 100%; height: 4em; border: 3px solid #3e2723; }
    .stAlert { background-color: rgba(224, 197, 160, 0.95); border: 2px solid #8b4513; }
    </style>
    """, unsafe_allow_html=True)

try:
    PPLX_API_KEY = st.secrets["PERPLEXITY_API_KEY"]
except KeyError:
    st.error("☠️ MANCANO LE MUNIZIONI (API KEY)!")
    st.stop()

client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="SNIPER 18.0 WINNER EDGE", page_icon="⚽", layout="wide")

st.title("🌵 SNIPER 18.0: 'THE WINNER'S EDGE' 🏆")
st.markdown("### *'Non contiamo i gol, contiamo i vincitori. Solo Marmo, zero pareggi.'* 🔫 🥃")

# 4. IL RADAR DEL VINCITORE
st.subheader("📡 SCANSIONE 'CHI VINCE': CERCA LA PEPITA 1X2")

if st.button("🔥 ATTIVA SONAR 'WINNER' (ANALISI CHIRURGICA)"):
    with st.spinner("LO SCERIFFO STA ANALIZZANDO LA CAZZIMMA DELLE SQUADRE... 🚬"):
        try:
            prompt_pplx = """
            SISTEMA: ESPERTO SCOMMETTITORE BLUE LOCK. PARLA COME UN COWBOY DURO.
            RICERCA: Trova i match di calcio più sicuri di oggi/domani.

            PARAMETRI DI PERFEZIONE 18.0 (WINNER FOCUS):
            1. MERCATO PRIORITARIO: 1X2 (Vincente), Asian Handicap (-1, -1.5) e DNB (Draw No Bet).
            2. CERTEZZA ASSOLUTA: Se una squadra ha vinto le ultime 5 ed è in casa contro un avversario arrugginito, è MARMO. [cite: 2026-02-15]
            3. HANDICAP: Suggerisci Handicap se il favorito ha una quota troppo bassa (<1.40). [cite: 2026-02-24]
            4. SQUADRE ITALIANE: Forza Napoli sempre, per le altre in Europa usa prudenza. [cite: 2026-01-25, 2026-01-22]
            5. NO SVIZZERA: Terreno instabile, scarta tutto il territorio. [cite: 2026-01-13]
            6. OBIETTIVO: Undici partite per trasformare 3€ in 100€. [cite: 2026-01-21]

            REFERTO (SINTASSI MAIUSCOLA):
            '💰 PEPITA INDIVIDUATA: [SQUADRA] VINCE!'
            'TIPO DI COLPO: [1, 2 o Handicap].'
            'DENSITÀ TECNICA: [Calcolo probabilità].'
            'MOTIVAZIONE: [Perché il bullone del nemico è allentato].'
            """

            response = client_pplx.chat.completions.create(model="sonar-pro", messages=[{"role": "user", "content": prompt_pplx}])
            st.info(response.choices[0].message.content)
            st.balloons()

        except Exception as e:
            st.error(f"☠️ URTO TECNICO: {e}")
