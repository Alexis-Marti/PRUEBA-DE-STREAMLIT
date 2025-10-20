import streamlit as st
from modulos.config.conexion import obtener_conexion

# Función para verificar usuario y contraseña
def verificar_usuario(usuario, contrasena):
    con = obtener_conexion()
    if not con:
        st.error("⚠️ No se pudo conectar a la base de datos.")
        return None

    try:
        cursor = con.cursor()
        # Mostrar la consulta y parámetros para depuración
        query = "SELECT usuario, contrasena FROM empleado WHERE usuario = %s AND contrasena = %s"
        st.write(f"Ejecutando consulta: {query} con parámetros: ({usuario}, {contrasena})")
        cursor.execute(query, (usuario, contrasena))
        result = cursor.fetchone()
        return result  # Retorna el registro si existe
    except mysql.connector.Error as e:
        st.error(f"❌ Error al ejecutar la consulta: {e}")
        return None
    finally:
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

# Llamar la función login para ejecutarlo
if __name__ == "__main__":
    login()

