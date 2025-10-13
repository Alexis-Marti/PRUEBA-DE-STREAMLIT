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

# Intentar hacer una consulta en la tabla 'Venta' (mostrar las primeras 10 filas)
cursor.execute("SELECT * FROM Venta LIMIT 10")
resultados = cursor.fetchall()

# Mostrar los resultados en Streamlit
st.write("Resultados de la consulta a la tabla 'Venta':")
st.write(resultados)

# Cerrar la conexión y el cursor
cursor.close()
conn.close()



