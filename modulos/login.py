import streamlit as st
from modulos.config.conexion import obtener_conexion

def verificar_usuario(usuario, contrasena):
    con = obtener_conexion()
    if not con:
        st.error("⚠️ No se pudo conectar a la base de datos.")
        return None

    try:
        cursor = con.cursor()
        # Cambié la tabla a Empleados y las columnas a Usuario y Contra
        query = "SELECT Id_Empleado FROM Empleados WHERE Usuario = %s AND Contra = %s"
        cursor.execute(query, (usuario, contrasena))
        result = cursor.fetchone()
        return result[0] if result else None
    finally:
        con.close()

def login():
    st.title("Inicio de sesión")
    usuario = st.text_input("Usuario", key="usuario_input")
    contrasena = st.text_input("Contraseña", type="password", key="contrasena_input")

    if st.button("Iniciar sesión"):
        id_empleado = verificar_usuario(usuario, contrasena)
        if id_empleado:
            st.session_state["usuario"] = usuario
            st.session_state["id_empleado"] = id_empleado
            st.success(f"Bienvenido {usuario}")
            st.rerun()
        else:
            st.error("Credenciales incorrectas")

