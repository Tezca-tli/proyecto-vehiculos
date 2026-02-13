import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
# Asegúrate de que el nombre del archivo coincida
car_data = pd.read_csv('vehicles_us.csv')

# Título de la app
st.header('Análisis de Vehículos Usados')

# Botón 1: Construir histograma
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Botón 2: Construir gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión precio vs. odómetro')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
