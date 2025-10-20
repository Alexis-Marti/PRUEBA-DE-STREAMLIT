import streamlit as st
from modulos.login import login  # Importa la función de login
from modulos.venta import mostrar_venta  # Importa la función para mostrar ventas

# Comprobamos si la sesión ya está iniciada
if "sesion_iniciada" in st.session_state and st.session_state["sesion_iniciada"]:
    # Si la sesión está iniciada, mostrar el contenido de ventas
    mostrar_venta()
else:
    # Si la sesión no está iniciada, mostrar el login
    login()













