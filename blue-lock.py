import streamlit as st
from openai import OpenAI
import datetime

# --- ESTETICA DA SALOON BLUE LOCK (BLINDATA) ---
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(rgba(244, 236, 207, 0.85), rgba(244, 236, 207, 0.85)), 
        url('https://images.unsplash.com/photo-1528563351349-3397da0533d1?q=80&w=2070&auto=format&fit=crop');
        background-size: cover; background-position: center; background-attachment: fixed;
        color: #5d4037; font-family: 'Georgia', serif;
    }
    .stButton>button { background-color: #d32f2f !important; color: white !important; font-weight: bold; width: 100%; height: 4em; border: 3px solid #3e2723; text-transform: uppercase; }
    .stAlert { background-color: rgba(224, 197, 160, 0.95); border: 2px solid #8b4513; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. CASSAFORTE API
try:
    PPLX_API_KEY = st.secrets["PERPLEXITY_API_KEY"]
except KeyError:
    st.error("☠️ MANCANO LE MUNIZIONI (API KEY) NEI SECRETS!")
    st.stop()

client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

# Sincronizzazione Temporale per il Live
ora_attuale = datetime.datetime.now().strftime("%A %d %B %Y, %H:%M")

st.set_page_config(page_title="SNIPER 20.0 LIVE SCRAPER", page_icon="⚽", layout="wide")

st.title("🌵 SNIPER 20.0: 'LIVE BOOKIE-SCRAPER' 📡")
st.markdown(f"### *'Scansione Live su SNAI/Eurobet. Orologio: {ora_attuale}.'* 🔫 🥃")

# 3. IL RADAR DEI VANTAGGI
st.subheader("📡 PALINSESTO LIVE: SU CHI PUNTARE ORA?")

if st.button("🔥 SCANSIONA BOOKMAKERS (IDENTIFICA IL MARMO LIVE)"):
    with st.spinner(f"LO SCERIFFO STA SETACCIANDO I PORTALI DI SCOMMESSE ALLE {ora_attuale}... 🚬"):
        try:
            # Prompt specifico per scraping/ricerca su siti di scommesse
            prompt_pplx = f"""
            SISTEMA: ESPERTO TRADER LIVE BLUE LOCK. PARLA COME UN COWBOY DURO.
            DATA E ORA: {ora_attuale}. 

            RICERCA: Scansiona i principali portali di scommesse (SNAI, Eurobet, PlanetWin365, Bet365) per trovare match di calcio IN CORSO (Live).
            
            PARAMETRI DI SELEZIONE (BOOKIE RULES):
            1. IDENTIFICA: Squadre, Minuto, Punteggio e Quota attuale (1, X, 2).
            2. LOGICA BLUE LOCK: Cerca match dove la squadra favorita (quota iniziale <1.60) è ancora 0-0 o sta perdendo, ma domina le statistiche (AP > 1.5/min). [cite: 2026-01-21]
            3. MERCATI: Suggerisci 1X2, Handicap o DNB per la nostra multipla da 11 pepite (3€ -> 100€). [cite: 2026-01-21]
            4. FILTRI: Niente Svizzera, protezione totale sulle italiane (Under 4.5). [cite: 2026-01-13, 2026-01-22]
            5. SERIE C (B/C): Se trovi match live di queste categorie, dagli la priorità. [cite: 2026-01-26]

            REFERTO LIVE (SINTASSI MAIUSCOLA):
            '⚠️ OPPORTUNITÀ SNAI/LIVE: [SQUADRE] - [MINUTO/RISULTATO]'
            'QUOTA ATTUALE: [Valore quota]'
            'ORDINE TATTICO: [Es: Punta ora sul Segno 1 / Aspetta quota 1.80]'
            'DENSITÀ TECNICA: [Perché questo colpo è marmo puro].'
            """
            
            response = client_pplx.chat.completions.create(
                model="sonar-pro", 
                messages=[{"role": "user", "content": prompt_pplx}]
            )
            
            st.info(response.choices[0].message.content)
            st.balloons()
            
        except Exception as e:
            st.error(f"☠️ URTO NELLO SCRAPER: {e}")

# 4. MONITOR DEL CANTIERE
st.sidebar.markdown(f"**Socio, il Napoli è nel cuore, il Marmo è nella testa.** [cite: 2026-01-25]")
st.sidebar.write("Obiettivo: 3€ -> 100€ [cite: 2026-01-21]")
