import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos


st.header('Aplicación para obtener info sobre los vehiculos')

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig_hist = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Se agrega la construcción del gráfico de dispersión

disp_button = st.button('Construir gráfico de dispersión') # crear un botón
        
if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
    # crear un gráfico de dispersión
    fig_disp = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_disp, use_container_width=True)

# Se agregan con casillas

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

    # crear un histograma
    fig_hist = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# crear una casilla de verificación
build_disp = st.checkbox('Construir un gráfico de dispersión')

if build_disp: # si la casilla de verificación está seleccionada
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig_disp = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_disp, use_container_width=True)