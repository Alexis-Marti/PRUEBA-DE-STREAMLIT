import streamlit as st
from modulos.config.conexion import obtener_conexion

def verificar_usuario(Usuario, Contra):
    con = obtener_conexion()
    if not con:
        st.error("⚠️ No se pudo conectar a la base de datos.")
        return None

    try:
        cursor = con.cursor()
        query = "SELECT * FROM Empleados WHERE Usuario = %s AND Contra = %s"
        cursor.execute(query, (Usuario, Contra))
        result = cursor.fetchone()
        
        # Si encontramos un resultado, devolvemos toda la fila
        return result if result else None
    finally:
        con.close()

def login():
    st.title("Inicio de sesión")
    Usuario = st.text_input("Usuario", key="usuario_input")
    Contra = st.text_input("Contraseña", type="password", key="contrasena_input")

    if st.button("Iniciar sesión"):
        usuario_data = verificar_usuario(Usuario, Contra)
        
        if usuario_data:
            # Extraemos el Id_Empleado y el nombre del resultado
            Id_Empleado = usuario_data[0]  # Suponiendo que el Id_Empleado es el primer campo
            st.session_state["usuario"] = Usuario
            st.session_state["Id_Empleado"] = Id_Empleado
            st.success(f"Bienvenido, {Usuario} (ID: {Id_Empleado})")
        else:
            st.error("Credenciales incorrectas")

