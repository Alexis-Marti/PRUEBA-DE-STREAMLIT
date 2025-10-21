import streamlit as st
from modulos.config.conexion import obtener_conexion


def verificar_usuario(Usuario, Contra):
    con = obtener_conexion()
    if not con:
        st.error("⚠️ No se pudo conectar a la base de datos.")
        return None
    else:
        # ✅ Mostrar el mensaje de conexión solo una vez
        if "conexion_exitosa" not in st.session_state:
            st.session_state["conexion_exitosa"] = True

    try:
        cursor = con.cursor()
        query = "SELECT Usuario, Contra FROM Empleados WHERE Usuario = %s AND Contra = %s"
        cursor.execute(query, (Usuario, Contra))
        result = cursor.fetchone()
        return result[0] if result else None
    finally:
        con.close()


def login():
    st.title("Inicio de sesión")

    # 🟢 Mostrar el mensaje de conexión si ya se estableció
    if st.session_state.get("conexion_exitosa"):
        st.success("✅ Conexión a la base de datos establecida correctamente.")

    Usuario = st.text_input("Usuario", key="usuario_input")
    Contra = st.text_input("Contraseña", type="password", key="contrasena_input")

    if st.button("Iniciar sesión"):
        tipo = verificar_usuario(Usuario, Contra)
        if tipo:
            st.session_state["usuario"] = Usuario
            st.success(f"Bienvenido ({Usuario}) 👋")
            st.session_state["sesion_iniciada"] = True
            st.rerun()
        else:
            st.error("❌ Credenciales incorrectas.")


