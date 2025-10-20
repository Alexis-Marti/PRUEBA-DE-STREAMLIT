import streamlit as st
import mysql.connector
from modulos.config.conexion import obtener_conexion

def verificar_usuario(Usuario, Contra):
    # Intentar obtener la conexión a la base de datos
    con = obtener_conexion()  
    if not con:
        st.error("⚠️ No se pudo conectar a la base de datos.")
        return None

    try:
        # Crear un cursor para ejecutar la consulta SQL
        cursor = con.cursor()
        # Actualizamos la consulta para usar las columnas "usuario" y "contrasena"
        query = "SELECT * FROM empleado WHERE usuario = %s AND contrasena = %s"
        cursor.execute(query, (Usuario, Contra))  # Ejecutar la consulta con los parámetros de entrada
        result = cursor.fetchone()  # Obtener el primer resultado (si existe)
        
        # Si encontramos un resultado, lo devolvemos
        if result:
            return result  # Retorna toda la fila (contiene id_empleado, usuario, contrasena, etc.)
        else:
            return None  # Si no encontramos nada, devolvemos None

    except mysql.connector.Error as err:
        # Mostrar el error detallado en caso de fallos
        st.error(f"Error al ejecutar la consulta: {err}")
        st.error(f"Consulta SQL: {query}")
        return None
    finally:
        # Asegurarse de cerrar la conexión después de realizar la consulta
        con.close()

def login():
    st.title("Inicio de sesión")
    
    # Crear los campos de entrada para el nombre de usuario y la contraseña
    Usuario = st.text_input("Usuario", key="usuario_input")
    Contra = st.text_input("Contraseña", type="password", key="contrasena_input")

    # Verificar cuando el usuario presiona el botón de "Iniciar sesión"
    if st.button("Iniciar sesión"):
        # Verificar el usuario y la contraseña
        usuario_data = verificar_usuario(Usuario, Contra)
        
        if usuario_data:
            # Extraemos el id_empleado (que se encuentra en la primera columna de la tabla)
            Id_Empleado = usuario_data[0]  # Asumimos que el id_empleado es la primera columna en la tabla
            # Guardamos los datos del usuario en el estado de la sesión
            st.session_state["usuario"] = Usuario
            st.session_state["id_empleado"] = Id_Empleado
            st.success(f"Bienvenido, {Usuario} (ID: {Id_Empleado})")
        else:
            # Si no encontramos el usuario, mostramos un error
            st.error("Credenciales incorrectas")

if __name__ == "__main__":
    # Ejecutamos la función login cuando se corre el archivo
    login()

