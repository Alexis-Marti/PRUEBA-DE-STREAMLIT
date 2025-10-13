import streamlit as st
import mysql.connector

# Conexión
conn = mysql.connector.connect(
    host="be5bmntqvmjb45dbc68h-mysql.services.clever-cloud.com",
    user="ufrsewvahgrdaghy",
    password="UxDnJbPxibZaLwBC6Xt1",
    database="ufrsewvahgrdaghy",
    port=3306
)
cursor = conn.cursor()

st.title("Agregar Venta")

# Formulario
comprador = st.text_input("Nombre del Comprador")
edad = st.text_input("Edad")
telefono = st.number_input("Teléfono", min_value=0, step=1)

if st.button("Agregar Venta"):
    cursor.execute(
        "INSERT INTO Venta (Comprador, Edad, Telefono) VALUES (%s, %s, %s)",
        (comprador, edad, telefono)
    )
    conn.commit()
    st.success("Venta agregada correctamente!")

# Mostrar tabla actualizada
cursor.execute("SELECT * FROM Venta")
datos = cursor.fetchall()
st.table(datos)

cursor.close()
conn.close()
