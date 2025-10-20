import streamlit as st
from modulos.config.conexion import obtener_conexion
import mysql.connector

def verificar_usuario(Usuario, Contra):
    con = obtener_conexion()  # Obtén la conexión a la base de datos
    if not con:
        st.error("⚠️ No se pudo conectar a la base de datos.")
        return None

    try:
        cursor = con.cursor()
        query = "SELECT * FROM Empleados WHERE Usuario = %s AND Contra = %s"
        cursor.execute(query, (Usuario, Contra))
        result = cursor.fetchone()  # Obtener la primera fila de resultados
        
        if result:  # Si encontramos un resultado
            return result  # Retornar toda la fila de datos del usuario
        else:
            return None  # No se encontraron coincidencias

    except mysql.connector.Error as err:
        st.error(f"Error al ejecutar la consulta: {err}")
        return None
    finally:
        con.close()  # Asegurarse de cerrar la conexión después de la consulta

def login():
    st.title("Inicio de sesión")
    
    # Campos de entrada para el usuario y la contraseña
    Usuario = st.text_input("Usuario", key="usuario_input")
    Contra = st.text_input("Contraseña", type="password", key="contrasena_input")

    if st.button("Iniciar sesión"):
        # Verificar el usuario y contraseña
        usuario_data = verificar_usuario(Usuario, Contra)
        
        if usuario_data:
            # Extraemos el Id_Empleado (primer campo de la fila)
            Id_Empleado = usuario_data[0]  # Asumimos que el Id_Empleado es el primer campo
            st.session_state["usuario"] = Usuario
            st.session_state["Id_Empleado"] = Id_Empleado
            st.success(f"Bienvenido, {Usuario} (ID: {Id_Empleado})")
        else:
            st.error("Credenciales incorrectas")

if __name__ == "__main__":
    login()

