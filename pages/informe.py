import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


#Configuramos encabezado de pagina
st.set_page_config(
    page_title="Analisis del CO2 y el PIB",
    initial_sidebar_state="expanded",
    layout="centered",
    page_icon="🌎"
)

#Visualización
st.title("Evolución Global del CO₂ y el PIB (2000-2023): Análisis y Relevancia para las Políticas Públicas en Colombia")
ruta = "Data/tabla.csv"
df = pd.read_csv(ruta)
tex = "Este estudio presenta un análisis de los datos relevantes sobre la generación de CO₂ y el PIB a nivel mundial desde el año 2000 hasta 2023. Se examina la correlación y variabilidad de estos indicadores en el contexto de su evolución global. El objetivo es comprender estos cambios para orientar el diseño y evaluación de políticas públicas en Colombia, con un enfoque en los distintos sectores industriales."
st.write(df, tex)

with st.sidebar:
        col1, col2 = st.columns(2)
        with col1: 
            st.page_link("app.py", label="Home", icon="🏚️")
            st.page_link("pages\informe.py", label="infor", icon="📝")
        with col2:
            st.header("Analisis del CO2 y el PIB")
            
#selector de gráficos
st.header('Visualizador de Gráficos') 
tipo = st.selectbox('Seleccione el tipo de gráfico', ["Emisiones de CO₂ en relación con el PIB", "Tendencia de Emisiones de CO2 por Sector Industrial", "Evolución del Cambio de Temperatura Global Atribuido al CO2", "Emisiones totales de CO2 vs Año", "Relación entre PIB y Emisiones de CO₂ per cápita"] )
#selector de variables a comparar
#variable = st.selectbox('Seleccione la variable a comparar', df.columns[1:].values)

if tipo == 'Emisiones de CO₂ en relación con el PIB':    
     # Mostrar un texto antes del gráfico
    st.write("### Relación entre el PIB y las emisiones totales de CO₂ en 2022")
    st.write("Se muestra la relación entre el Producto Interno Bruto (PIB) y las emisiones totales de CO₂ para el año 2022. Se puede observar cómo las economías más grandes tienden a tener mayores emisiones.")

    # Filtrar datos del año 2022
    df_GDP_2022 = df[df['year'] == 2022]  

    # Estilo de la gráfica
    sns.set_style('darkgrid')

    # Crear la figura y los ejes
    fig, ax = plt.subplots(figsize=(9, 5))

    # Graficar diagrama de dispersión
    ax.scatter(df_GDP_2022['gdp'], df_GDP_2022['co2'], color='r', marker='o')

    # Personalizar la gráfica
    ax.set_title('PIB vs Emisiones totales de CO2 en 2022')
    ax.set_xlabel('PIB')
    ax.set_ylabel('Emisiones totales de CO2')

    # Mostrar la figura en Streamlit
    st.pyplot(fig)
    
elif tipo == 'Tendencia de Emisiones de CO2 por Sector Industrial':
    # Agregar texto introductorio
    st.write("### Tendencia de Emisiones de CO₂ por Sector Industrial")
    st.write("Se muestra cómo han evolucionado las emisiones de CO₂ en distintos sectores industriales a lo largo del tiempo. Se pueden identificar tendencias clave y analizar qué sectores han contribuido más a las emisiones.")

    # Emisiones de CO₂ por sector industrial.
    # Filtrar solo las columnas necesarias
    columns_to_plot = ["year", "cement_co2", "coal_co2", "flaring_co2", "gas_co2", "oil_co2", "other_industry_co2"]
    df_filtered = df[columns_to_plot]

    # Agrupar por año y sumar emisiones de cada sector
    df_grouped = df_filtered.groupby("year").sum()

    # Crear la figura y los ejes
    fig, ax = plt.subplots(figsize=(12, 6))

    # Graficar las emisiones por sector
    for column in columns_to_plot[1:]:  # Excluir "year"
        ax.plot(df_grouped.index, df_grouped[column], label=column.replace("_co2", "").capitalize())

    # Personalizar la gráfica
    ax.set_title("Tendencia de Emisiones de CO2 por Sector Industrial")
    ax.set_xlabel("Año")
    ax.set_ylabel("Emisiones de CO₂ (toneladas)")
    ax.legend()
    ax.grid(True)

    # Mostrar la figura en Streamlit
    st.pyplot(fig) 

elif tipo == 'Evolución del Cambio de Temperatura Global Atribuido al CO2': 
    # Agregar texto introductorio
    st.write("### Evolución del Cambio de Temperatura Global Atribuido al CO₂")
    st.write(
        "Se muestra cómo ha evolucionado el cambio de temperatura global "
        "atribuido a las emisiones de CO₂ a lo largo de los años. "
        "El incremento en la temperatura es un indicador clave del impacto del CO₂ "
        "en el cambio climático.")
    
    # Agrupar por año y calcular el promedio del cambio de temperatura atribuido al CO₂
    df_temp_trend = df.groupby("year")["temperature_change_from_co2"].mean()

    # Crear la figura y los ejes
    fig, ax = plt.subplots(figsize=(12, 6))

    # Graficar la evolución del cambio de temperatura
    ax.plot(df_temp_trend.index, df_temp_trend.values, marker="o", linestyle="-", color="r")

    # Personalizar la gráfica
    ax.set_title("Evolución del Cambio de Temperatura Global Atribuido al CO2")
    ax.set_xlabel("Año")
    ax.set_ylabel("Cambio de Temperatura (°C)")
    ax.grid(True, linestyle="--", alpha=0.5)

    # Mostrar la figura en Streamlit
    st.pyplot(fig)  

elif tipo == 'Emisiones totales de CO2 vs Año':
      # Agregar texto introductorio
    st.write("### Emisiones Totales de CO₂ vs Año")
    st.write(
        "Se muestra la evolución de las emisiones totales de CO₂ en Brasil, "
        "México, Argentina y Colombia a lo largo del tiempo. "
        "El análisis de estas tendencias nos permite entender cómo han cambiado las emisiones "
        "en cada país y cómo pueden estar relacionadas con el crecimiento económico y las políticas ambientales.")
    
    # Filtrar datos por país
    data_Brazil = df[df['country'] == 'Brazil']
    data_Mexico = df[df['country'] == 'Mexico']
    data_Argentina = df[df['country'] == 'Argentina']
    data_Colombia = df[df['country'] == 'Colombia']

    # Crear la figura y los ejes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Graficar evolución de emisiones de CO₂
    ax.plot(data_Brazil['year'], data_Brazil['co2'], '-', color='#FF0000', linewidth=3, label='Brazil')
    ax.plot(data_Mexico['year'], data_Mexico['co2'], '-', color='#0000FF', linewidth=3, label='Mexico')
    ax.plot(data_Argentina['year'], data_Argentina['co2'], '-', color='#FFA500', linewidth=3, label='Argentina')
    ax.plot(data_Colombia['year'], data_Colombia['co2'], '-', color='#8E44AD', linewidth=3, label='Colombia')

    # Personalizar la gráfica
    ax.set_xlabel('Año')
    ax.set_ylabel('Emisiones totales de CO2 (millones de toneladas)')
    ax.set_title('Emisiones totales de CO2 vs Año')
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.5)

    # Mostrar la figura en Streamlit
    st.pyplot(fig)

else:
    # Agregar texto introductorio
    st.write("### Relación entre PIB y Emisiones de CO₂ per cápita")
    st.write(
        "Se muestra la cantidad de CO₂ emitido por persona en los 10 países con mayor PIB. "
        "Se comparan las emisiones derivadas de diferentes fuentes de energía: carbón, petróleo y gas. "
        "Analizar estos datos permite identificar qué economías tienen una mayor dependencia de combustibles fósiles "
        "y cómo esto impacta en sus emisiones per cápita.")

    # Filtrar los 10 países con mayor PIB
    df_gdp_top10 = df.groupby("country", as_index=False).agg({
    "gdp": "max",  # Seleccionar el mayor PIB registrado por país
    "coal_co2_per_capita": "mean",  # Promedio de emisiones por carbón
    "oil_co2_per_capita": "mean",  # Promedio de emisiones por petróleo
    "gas_co2_per_capita": "mean"  # Promedio de emisiones por gas
    }).nlargest(10, "gdp")  # Seleccionar los 10 países con mayor PIB

    # Definir ancho de las barras
    w = 0.25  

    # Convertir datos a numpy arrays
    x = np.asarray(df_gdp_top10["country"])  # Usar nombres de países
    y_carbon = np.asarray(df_gdp_top10["coal_co2_per_capita"])
    y_petroleo = np.asarray(df_gdp_top10["oil_co2_per_capita"])
    y_gas = np.asarray(df_gdp_top10["gas_co2_per_capita"])

    # Definir posiciones de las barras
    bar1 = np.arange(len(x))  
    bar2 = bar1 + w  
    bar3 = bar2 + w  

    # Crear la figura y los ejes
    fig, ax = plt.subplots(figsize=(12, 6))

    # Graficar las barras correctamente alineadas
    ax.bar(bar1, y_carbon, w, label="Carbón", color="red")
    ax.bar(bar2, y_petroleo, w, label="Petróleo", color="blue")
    ax.bar(bar3, y_gas, w, label="Gas", color="green")

    # Personalizar la gráfica
    ax.set_xlabel("PAÍSES")
    ax.set_ylabel("CO2 PER CÁPITA")
    ax.set_title("RELACIÓN ENTRE PIB Y EMISIONES DE CO2 PER CÁPITA")

    # Ajustar etiquetas del eje X
    ax.set_xticks(bar1 + w)  
    ax.set_xticklabels(x, rotation=45)  

    # Agregar leyenda y cuadrícula
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    # Mostrar la figura
    st.pyplot(fig)    
