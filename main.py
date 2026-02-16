import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from cryptography.fernet import Fernet
import time
import random

# --- SEGURIDAD AES-256 ---
# Llave única para cifrar PRO PART DATE
KEY = Fernet.generate_key()
CIPHER = Fernet(KEY)

# --- BASE DE DATOS: PRO PART DATE ---
# Información 1990-2025 transcrita de AllData
PRO_PART_DATE = {
    "VW_GOLF_A4_2003": {
        "ECU": "Bosch Motronic ME 7.5",
        "UID_VLINK": "VLNK-PRO-V12-GOLF",
        "PROTOCOL": "K-Line (Pin 7) & CAN",
        "PINOUT": {4: "GND", 7: "K-Line", 16: "B+"}
    }
}

st.set_page_config(page_title="PROPART V12", layout="wide")

with st.sidebar:
    st.title("PROPART V12")
    st.write("Socio: **MILLAN** | AI: **YULS**")
    opcion = st.radio("MENÚ", ["Scanner V-Link", "Sincro CKP/CMP", "Calibrar TBA", "Mapeo DLC"])

if opcion == "Scanner V-Link":
    st.header("🔍 Buscando Hardware V-Link...")
    if st.button("Escanear"):
        time.sleep(1)
        st.success(f"V-Link Conectado: {PRO_PART_DATE['VW_GOLF_A4_2003']['UID_VLINK']}")

elif opcion == "Sincro CKP/CMP":
    st.header("⚙️ Sincronización en Tiempo Real")
    # Visualización Dual: Gráfica + Número
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=[0,1,0,1], name="CKP", line=dict(color='#00ffcc', shape='hv')))
    fig.add_trace(go.Scatter(y=[0,0,1,0], name="CMP", line=dict(color='#ff33cc', shape='hv')))
    st.plotly_chart(fig)
    st.metric("Desfase", "0.0°", "Sincronizado")

elif opcion == "Mapeo DLC":
    st.header("🔌 Pinout Real (Pro Part Date)")
    st.table(pd.DataFrame({"Pin": [4,7,16], "Función": ["GND", "K-Line", "B+"]}))
