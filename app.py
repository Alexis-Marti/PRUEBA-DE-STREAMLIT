import streamlit as st

# Título de la aplicación
st.title('¡Bienvenido a mi aplicación Streamlit!')

# Texto de bienvenida
st.write('Este es un ejemplo básico de cómo usar Streamlit con Python.')

# Crear un slider para seleccionar edad
edad = st.slider('Selecciona tu edad', 0, 100, 25)
st.write(f'Tu edad es {edad} años.')