import streamlit as st
import mysql.connector

st.set_page_config(page_title="Ventas - Clever Cloud", page_icon="💰")
st.title("💰 Registro de Ventas")

try:
    # 🔗 Conexión a la base de datos
    conn = mysql.connector.connect(
        host="be5bmntqvmjb45dbc68h-mysql.services.clever-cloud.com",
        user="ufrsewvahgrdaghy",
        password="UxDnJbPxibZaLwBC6Xt1",
        database="ufrsewvahgrdaghy",  # ⚠️ Verifica el nombre exacto de tu base
        po

