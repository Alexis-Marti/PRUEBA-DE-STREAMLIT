import streamlit as st
from modulos.login import login  # Importa la función de login
from modulos.venta import mostrar_venta  # Importa la función para mostrar ventas

# Comprobamos si la sesión ya está iniciada
if "sesion_iniciada" in st.session_state and st.session_state["sesion_iniciada"]:
      # Mostrar el menú lateral
    opciones = ["Ventas", "Otra opción"]  # Agrega más opciones si las necesitas
    seleccion = st.sidebar.selectbox("Selecciona una opción", opciones)

    # Según la opción seleccionada, mostramos el contenido correspondiente
    if seleccion == "Ventas":
        mostrar_venta()
    elif seleccion == "Otra opción":
        st.write("Has seleccionado otra opción.")  # Aquí podrías agregar el contenido de otras opciones

else:
    # Si la sesión no está iniciada, mostrar el login
    login()














