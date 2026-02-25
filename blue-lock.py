import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import datetime

# --- GRAFICA DA SALOON BLUE LOCK (MARMO PURO) ---
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(rgba(244, 236, 207, 0.85), rgba(244, 236, 207, 0.85)), 
        url('https://images.unsplash.com/photo-1528563351349-3397da0533d1?q=80&w=2070&auto=format&fit=crop');
        background-size: cover; background-position: center; background-attachment: fixed;
        color: #5d4037; font-family: 'Georgia', serif;
    }
    .stButton>button { background-color: #d32f2f !important; color: white !important; font-weight: bold; width: 100%; height: 4.5em; border: 3px solid #3e2723; text-transform: uppercase; }
    .stAlert { background-color: rgba(224, 197, 160, 0.95); border: 2px solid #8b4513; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. CASSAFORTE API
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    PPLX_API_KEY = st.secrets["PERPLEXITY_API_KEY"]
except KeyError:
    st.error("☠️ MANCANO LE MUNIZIONI (API KEY) NEI SECRETS!")
    st.stop()

client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")
ora_attuale = datetime.datetime.now().strftime("%H:%M")

st.set_page_config(page_title="SNIPER 21.0 SNAI VISION", page_icon="⚽", layout="wide")
st.title("🌵 SNIPER 21.0: 'SNAI VISION COMMANDER' 📡")
st.markdown(f"### *'Leggi lo schermo, domina il Live. Orologio: {ora_attuale}.'* 🔫 🥃")

# 3. INTERFACCIA DI COMANDO
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📸 CARICA SCREENSHOT SNAI")
    uploaded_snai = st.file_uploader("APPICCICA L'IMMAGINE DEL PALINSESTO LIVE:", type=["jpg", "png", "jpeg"])

with col2:
    st.subheader("🕹️ COSA DEVE FARE LO SCERIFFO?")
    modalita = st.radio("SELEZIONA AZIONE:", ["ANALISI VISION (DA FOTO)", "SONAR WEB (CERCA LIVE ORA)"])

if st.button("🔥 ESEGUI ORDINE TATTICO"):
    with st.spinner("LO SCERIFFO STA ANALIZZANDO IL CANTIERE... 🚬"):
        try:
            if modalita == "ANALISI VISION (DA FOTO)" and uploaded_snai:
                # FASE 1: GEMINI LEGGE SNAI
                img = Image.open(uploaded_snai)
                prompt_vision = "ESTRAI TUTTI I MATCH LIVE: Squadre, Minuto, Risultato, Quote 1X2, Quote Over/Under."
                res_vision = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt_vision, img])
                dati_snai = res_vision.text
            else:
                dati_snai = "CERCA SUL WEB I MATCH LIVE SU SNAI ADESSO."

            # FASE 2: PERPLEXITY DECIDE IL COLPO
            prompt_pplx = f"""
            SISTEMA: COMANDANTE TATTICO BLUE LOCK. PARLA COME UN COWBOY DURO.
            DATI LIVE: {dati_snai}
            
            PARAMETRI DI COMANDO (LIVE SNAI RULES):
            1. MARMO LIVE: Se un favorito (quota iniziale <1.60) è ancora 0-0 dopo il 20', ORDINA DI PUNTARE SUL VINCITORE. [cite: 2026-01-21]
            2. LOGICA SILEKS: Se una squadra ha quota 1.30-1.40 e domina, ORDINA 'PUNTA ORA' o 'HANDICAP LIVE'. [cite: 2026-02-24]
            3. BIAS FEMMINILE: Se vedi match femminili (Mozambico, Madagascar, ecc.), ORDINA 'OVER 1.5/2.5'. [cite: 2026-01-18]
            4. PROTEZIONE ITALIANA: Se è un match europeo di italiane, ORDINA 'UNDER 4.5' O 'DNB'. [cite: 2026-01-22]
            5. OBIETTIVO: 11 PEPITE PER 100€ (QUOTA ~33). [cite: 2026-01-21]

            REFERTO (SINTASSI MAIUSCOLA):
            '⚠️ ORDINE TATTICO: [MATCH] - [MINUTO/RISULTATO]'
            'AZIONE SNAI: [Es: Punta 2 Live / Carica Handicap / Aspetta]'
            'DENSITÀ TECNICA: [Perché il marmo sta per crepare].'
            """
            
            response = client_pplx.chat.completions.create(model="sonar-pro", messages=[{"role": "user", "content": prompt_pplx}])
            st.info(response.choices[0].message.content)
            st.balloons()
            
        except Exception as e:
            st.error(f"☠️ URTO NEL REATTORE: {e}")
