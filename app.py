import mysql.connector
import os
import streamlit as st

# Obtener las credenciales de las variables de entorno (seguridad)
host = os.getenv("DB_HOST", "be5bmntqvmjb45dbc68h-mysql.services.clever-cloud.com")
user = os.getenv("DB_USER", "ufrsewvahgrdaghy")
password = os.getenv("DB_PASSWORD", "UxDnJbPxibZaLwBC6Xt1")
database = os.getenv("DB_NAME", "be5bmntqvmjb45dbc68h")

# Crear la conexión con la base de datos
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Título en Streamlit
st.title("Formulario de Ingreso de Datos para la Tabla Venta")

# Crear un formulario para ingresar los datos
comprador = st.text_input("Comprador")
edad = st.text_input("Edad")
telefono = st.text_input("Telefono")

# Botón para insertar los datos en la base de datos
if st.button("Guardar Datos"):
    if comprador and edad and telefono:
        try:
            # Preparar la consulta SQL para insertar los datos en la tabla 'Venta'
            query = "INSERT INTO Venta (Comprador, Edad, Telefono) VALUES (%s, %s, %s)"
            cursor.execute(query, (comprador, edad, telefono))
            conn.commit()  # Confirmar la inserción

            # Mostrar un mensaje de éxito
            st.success(f"Los datos de {comprador} han sido guardados exitosamente.")
        except mysql.connector.Error as err:
            st.error(f"Error al guardar los datos: {err}")
    else:
        st.error("Por favor, ingresa todos los datos.")

# Realizar una consulta para mostrar los datos de la tabla Venta
cursor.execute("SELECT * FROM Venta LIMIT 10")
resultados = cursor.fetchall()

# Mostrar los resultados en Streamlit
st.write("Resultados de la tabla 'Venta':")
st.write(resultados)

# Cerrar la conexión y el cursor
cursor.close()
conn.close()




