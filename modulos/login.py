import streamlit as st
from modulos.config.conexion import obtener_conexion
import mysql.connector

def verificar_usuario(Usuario, Contra):
    con = obtener_conexion()
    if not con:
        st.error("⚠️ No se pudo conectar a la base de datos.")
        return None

    try:
        cursor = con.cursor()
        # Cambié la tabla a Empleados y las columnas a Usuario y Contra
        query = "SELECT Id_Empleado, Contra FROM Empleados WHERE Usuario = %s"
        cursor.execute(query, (Usuario,))
        result = cursor.fetchone()

        # Si la contraseña está cifrada, necesitarás compararla con un hash
        if result:
            # Si la contraseña no está cifrada, solo comparas directamente
            if result[1] == Contra:  # Aquí deberías usar una función de hash si es necesario
                return result[0]
            else:
                st.error("⚠️ Contraseña incorrecta.")
                return None
        else:
            st.error("⚠️ Usuario no encontrado.")
            return None
    except mysql.connector.Error as err:
        st.error(f"⚠️ Error al ejecutar la consulta: {err}")
        return None
    finally:
        cursor.close()
        con.close()

def login():
    st.title("Inicio de sesión")
    Usuario = st.text_input("Usuario", key="usuario_input")
    Contra = st.text_input("Contraseña", type="password", key="contrasena_input")

    if st.button("Iniciar sesión"):
        id_empleado = verificar_usuario(Usuario, Contra)
        if id_empleado:
            st.session_state["usuario"] = Usuario
            st.session_state["id_empleado"] = id_empleado
            st.success(f"Bienvenido {Usuario}")
            st.rerun()
        else:
            st.error("Credenciales incorrectas")

            st.error("Credenciales incorrectas")

