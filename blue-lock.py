import streamlit as st
from openai import OpenAI
import datetime

# --- ESTETICA DA SALOON BLUE LOCK ---
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

st.set_page_config(page_title="SNIPER 19.0 LIVE COMMANDER", page_icon="⚽", layout="wide")

st.title("🌵 SNIPER 19.0: 'LIVE COMMANDER' 📡")
st.markdown(f"### *'Comandi Tattici in Tempo Reale. Orologio: {ora_attuale}.'* 🔫 🥃")

# 3. IL RADAR TATTICO
st.subheader("📡 SONAR LIVE: COSA FARE IN QUESTO MOMENTO?")

if st.button("🔥 ATTIVA COMANDO LIVE (ORDINI IMMEDIATI)"):
    with st.spinner(f"LO SCERIFFO STA ANALIZZANDO LA PRESSIONE DEI CAMPI ALLE {ora_attuale}... 🚬"):
        try:
            # Prompt evoluto per istruzioni tattiche dirette
            prompt_pplx = f"""
            SISTEMA: COMANDANTE TATTICO BLUE LOCK. PARLA COME UN COWBOY DURO E DECISO.
            DATA E ORA: {ora_attuale}. 

            OBIETTIVO: Trova i match di calcio che si stanno giocando ADESSO e dimmi COSA FARE.
            
            PARAMETRI DI COMANDO (LIVE RULES):
            1. COSA FARE: Se una squadra domina (AP > 1.5/min) ma è 0-0, ordina di puntare 'OVER 0.5 HT' o 'SEGNO 1 LIVE'. [cite: 2026-01-21]
            2. ITALIANE IN EUROPA: Se c'è un match di Atalanta, Juve o Fiorentina, ordina 'UNDER 4.5' o 'DNB' per protezione. [cite: 2026-01-22]
            3. NO SVIZZERA: Se intercetti match svizzeri, ordina di 'EVITARE IL TERRITORIO'. [cite: 2026-01-13]
            4. BIAS FEMMINILE: Se giocano in Australia/Scozia, ordina 'CARICARE OVER'. [cite: 2026-01-18]
            5. OBIETTIVO 100€: Seleziona colpi con quote tra 1.40 e 2.00 per la nostra multipla da 3€ -> 100€. [cite: 2026-01-21]

            REFERTO TATTICO (SINTASSI MAIUSCOLA):
            '⚠️ ORDINE LIVE: [SQUADRE] - [RISULTATO/MINUTO]'
            'AZIOINE DA COMPIERE: [Es: Punta ora / Aspetta minuto X / Esci dalla scommessa]'
            'INTENSITÀ DEL CANTIERE: [0-100]%'
            'DENSITÀ TECNICA: [Perché il marmo sta per crepare].'
            """
            
            response = client_pplx.chat.completions.create(
                model="sonar-pro", 
                messages=[{"role": "user", "content": prompt_pplx}]
            )
            
            st.info(response.choices[0].message.content)
            st.balloons()
            
        except Exception as e:
            st.error(f"☠️ URTO NEL COMANDO LIVE: {e}")

# 4. MONITOR DEL CANTIERE
st.sidebar.image("https://images.unsplash.com/photo-1508098682722-e99c43a406b2?q=80&w=2070&auto=format&fit=crop", caption="Blue Lock Monitoring")
st.sidebar.markdown(f"**Socio, il Napoli è nel cuore, il Marmo è nella testa.** [cite: 2026-01-25]")
