import streamlit as st
from openai import OpenAI
import datetime

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

# Sincronizzazione Temporale
ora_attuale = datetime.datetime.now().strftime("%A %d %B %Y, %H:%M")

st.set_page_config(page_title="SNIPER 18.2 WINNER EDGE", page_icon="⚽", layout="wide")

st.title("🌵 SNIPER 18.2: 'REAL-TIME WINNER' 🏆")
st.markdown(f"### *'Orologio sincronizzato: {ora_attuale}. Si punta solo sulla gloria fresca.'* 🔫 🥃")

# 4. IL RADAR DEL VINCITORE
st.subheader("📡 SCANSIONE LIVE & PROSSIMI MATCH: CERCA IL MARMO")

if st.button("🔥 ATTIVA SONAR CHRONOS (ANALISI TEMPO REALE)"):
    with st.spinner(f"LO SCERIFFO STA SCANSIONANDO IL MONDO ALLE {ora_attuale}... 🚬"):
        try:
            # Injecting the exact time into the prompt for perfect grounding
            prompt_pplx = f"""
            SISTEMA: ESPERTO SCOMMETTITORE BLUE LOCK. PARLA COME UN COWBOY DURO.
            DATA E ORA CORRENTE: {ora_attuale}. 

            RICERCA: Trova i match di calcio più sicuri che iniziano ADESSO o entro le prossime 48 ore.
            
            PARAMETRI DI PERFEZIONE 18.2 (CHRONO FOCUS):
            1. MERCATO PRIORITARIO: 1X2 (Vincente), Asian Handicap (-1, -1.5) e DNB (Draw No Bet). [cite: 2026-01-21]
            2. NO DATI VECCHI: Ignora categoricamente match avvenuti prima del {ora_attuale}.
            3. CERTEZZA ASSOLUTA: Se una squadra ha vinto le ultime 5 ed è in casa contro un avversario arrugginito, è MARMO. [cite: 2026-02-15]
            4. HANDICAP: Suggerisci Handicap se il favorito ha una quota troppo bassa (<1.40). [cite: 2026-02-24]
            5. SQUADRE ITALIANE: Forza Napoli sempre, per le altre in Europa usa prudenza (Under 4.5 se trovi incertezze). [cite: 2026-01-25, 2026-01-22]
            6. NO SVIZZERA: Terreno instabile, scarta tutto il territorio. [cite: 2026-01-13]
            7. OBIETTIVO: Undici pepite per trasformare 3€ in 100€ (Quota ~33). [cite: 2026-01-21]
            
            REFERTO (SINTASSI MAIUSCOLA):
            '💰 PEPITA INDIVIDUATA: [SQUADRA] VINCE!'
            'ORARIO INIZIO: [HH:MM del match]'
            'TIPO DI COLPO: [1, 2 o Handicap].'
            'DENSITÀ TECNICA: [Calcolo probabilità basato su forma recente e polmoni d'acciaio].'
            'MOTIVAZIONE: [Perché questo bullone non si svita].'
            """
            
            response = client_pplx.chat.completions.create(
                model="sonar-pro", 
                messages=[{"role": "user", "content": prompt_pplx}]
            )
            
            st.info(response.choices[0].message.content)
            st.balloons()
            
        except Exception as e:
            st.error(f"☠️ URTO TECNICO NEL CRONOMETRO: {e}")
