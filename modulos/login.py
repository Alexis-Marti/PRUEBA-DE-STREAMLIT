import streamlit as st
from modulos.config.conexion import obtener_conexion
import mysql.connector

# Función para verificar usuario y contraseña
def verificar_usuario(usuario, contrasena):
    con = obtener_conexion()
    if not con:
        st.error("⚠️ No se pudo conectar a la base de datos.")
        return None

    try:
        cursor = con.cursor()
        query = "SELECT usuario, contrasena FROM empleado WHERE usuario = %s AND contrasena = %s"
        st.write(f"Ejecutando consulta: {query} con parámetros: ({usuario}, {contrasena})")
        cursor.execute(query, (usuario, contrasena))
        result = cursor.fetchone()

        # Si el usuario existe, retorna el resultado
        return result if result else None

    except mysql.connector.Error as e:
        # Agregamos más detalles sobre el error
        st.error(f"❌ Error de MySQL: {e}")
        return None

    finally:
        # Aseguramos el cierre de la conexión
        if con.is_connected():
            con.close()

# Función de login
def login():
    st.title("Inicio de sesión")
    
    # Entradas de usuario y contraseña
    usuario = st.text_input("Usuario", key="usuario_input")
    contrasena = st.text_input("Contraseña", type="password", key="contrasena_input")

    # Botón de login
    if st.button("Iniciar sesión"):
        # Verificar las credenciales
        usuario_validado = verificar_usuario(usuario, contrasena)
        
        if usuario_validado:
            # Si las credenciales son correctas, guardamos la sesión
            st.session_state["usuario"] = usuario
            st.session_state["tipo_usuario"] = usuario_validado[0]  # Puede ser algún tipo de validación adicional si es necesario
            st.success(f"Bienvenido, {usuario}")
            st.rerun()  # Recarga la aplicación para continuar
        else:
            st.error("❌ Credenciales incorrectas")


