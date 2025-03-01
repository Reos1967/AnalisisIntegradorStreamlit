import streamlit as st
import utilidades as util

#pagina de presentacion o index
st.set_page_config(
    page_title="Analisis del CO2 y el PIB",
    initial_sidebar_state="expanded",
    layout="wide",
    page_icon="🌎"
)

#Lamamos la funcion de archivo utilidad
with st.sidebar:
        col1, col2 = st.columns(2)
        with col1: 
            st.page_link("app.py", label="Home", icon="🏚️")
            st.page_link("pages\informe.py", label="infor", icon="📝")
        with col2:
            st.header("Analisis del CO2 y el PIB")


#Estructura de presentación
left_col, center_col, right_col =st.columns([1,6,1],
                                    vertical_alignment="center")

#edito la columna central 
with center_col:
    st.title("Transición Energética - Analisis del CO2 y el PIB")
    st.write("""
    Relación entre las emisiones de CO₂ y el PIB en Colombia para identificar sectores 
    industriales clave y apoyar la formulación de normativas para reducir sus emisiones.
