import streamlit as st
from modulos.config.conexion import obtener_conexion

def verificar_usuario(Usuario, Contra):
    con = obtener_conexion()
    if not con:
        st.error("⚠️ No se pudo conectar a la base de datos.")
        return None

    try:
        cursor = con.cursor()
        query = "SELECT Usuario, Contra FROM Empleados WHERE Usuario = %s AND Contra = %s"
        cursor.execute(query, (Usuario, Contra))
        result = cursor.fetchone()
        return result[0] if result else None
    finally:
        con.close()

def login():
    # Mostrar título y formulario de login
    st.title("Inicio de sesión")
    Usuario = st.text_input("Usuario", key="usuario_input")
    Contra = st.text_input("Contraseña", type="password", key="contrasena_input")

    # Si ya hay una sesión iniciada, mostrar un mensaje de bienvenida
    if "sesion_iniciada" in st.session_state and st.session_state["sesion_iniciada"]:
        st.success(f"Sesión iniciada correctamente como {st.session_state['usuario']}")
        return

    # Si no hay sesión iniciada, mostrar el formulario de login
    if st.button("Iniciar sesión"):
        tipo = verificar_usuario(Usuario, Contra)
        if tipo:
            st.session_state["usuario"] = Usuario
            st.session_state["tipo_usuario"] = tipo
            st.success(f"Bienvenido ({Usuario})")
            st.session_state["sesion_iniciada"] = True
            st.rerun()  # Recargar la página para reflejar el estado de la sesión
        else:
            st.error("Credenciales incorrectas")



