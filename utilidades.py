import pandas as pd
import streamlit as st 
from PIL import Image
from matplotlib import pyplot as plt 
import seaborn as sns
import plotly.express as px

def generarMenuInfo(df):
    with st.sidebar:
        col1, col2 = st.columns(2)
        with col1: 
            imagen = Image.open("Media\co2.png")
            st.image(imagen, use_container_width=False, width=80)
        with col2:
            st.header("Analisis del CO2 y el PIB")
            

        st.page_link("app.py", label="Home", icon="🏚️")
        st.page_link("Pages\informe.py", label="Información", icon="📝")


def generarMenu():
    with st.sidebar:
        col1, col2 = st.columns(2)
        with col1: 
            imagen = Image.open("Media\co2.png")
            st.image(imagen, use_container_width=False, width=80)
        with col2:
            st.header("Analisis del CO2 y el PIB")
            

        st.page_link("app.py", label="Home", icon="🏚️")
        st.page_link("Pages\informe.py", label="infor", icon="📝")