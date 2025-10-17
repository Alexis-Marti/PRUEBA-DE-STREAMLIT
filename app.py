# app.py
import streamlit as st
from modulos.conexion import conectar_db  # Importamos la función conectar_db del módulo conexion
from modulos.venta import mostrar_venta  # Importamos la función mostrar_venta del módulo venta

# Intentamos conectar con la base de datos usando la función de conexion.py
conn, error = conectar_db()

if conn:
    # Si la conexión fue exitosa
    st.success("Conexión exitosa a la base de datos MySQL.")
    
    # Llamamos a la función para mostrar las ventas
    mostrar_venta()

else:
    # Si hubo un error en la conexión
    st.error(error)


