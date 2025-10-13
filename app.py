import streamlit as st
import mysql.connector

st.set_page_config(page_title="Ventas - Clever Cloud", page_icon="💰")
st.title("💰 Registro de Ventas")

try:
    # 🔗 Conexión a la base de datos
    conn = mysql.connector.connect(
        host="be5bmntqvmjb45dbc68h-mysql.services.clever-cloud.com",
        user="ufrsewvahgrdaghy",
        password="UxDnJbPxibZaLwBC6Xt1",
        database="ufrsewvahgrdaghy",  # ⚠️ verifica el nombre exacto de tu base
        port=3306,
        connection_timeout=10
    )
    cursor = conn.cursor()
    st.success("✅ Conectado correctamente a la base de datos Clever Cloud")

    # 🧱 Crear tabla si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Venta (
            id INT AUTO_INCREMENT PRIMARY KEY,
            Comprador VARCHAR(100),
            Edad VARCHAR(10),
            Telefono VARCHAR(20)
        )
    """)
    conn.commit()

    # 🧾 Formulario para agregar venta
    st.subheader("🧾 Agregar nueva venta")
    comprador = st.text_input("Nombre del Comprador")
    edad = st.text_input("Edad")
    telefono = st.number_input("Teléfono", min_value=0, step=1)

    if st.button("Agregar Venta"):
        if comprador and edad and telefono:
            cursor.execute(
                "INSERT INTO Venta (Comprador, Edad, Telefono) VALUES (%s, %s, %s)",
                (comprador, edad, telefono)
            )
            conn.commit()
            st.success("✅ Venta agregada correctamente")
        else:
            st.warning("⚠️ Por favor, completa todos los campos antes de guardar.")

    # 📋 Mostrar tabla de ventas
    st.subheader("📋 Ventas registradas")
    cursor.execute("SELECT * FROM Venta")
    datos = cursor.fetchall()

    if datos:
        st.table(datos)
    else:
        st.info("No hay ventas registradas aún.")

except mysql.connector.Error as e:
    st.error(f"❌ Error al conectar con MySQL: {e}")
    st.info("Verifica que Clever Cloud permita conexiones externas o revisa tus credenciales.")

finally:
    # 🔒 Cerrar conexión y cursor
    try:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()
    except:
        pass


