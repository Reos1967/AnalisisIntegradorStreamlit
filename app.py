import streamlit as st
import pandas as pd
from PIL import Image
from matplotlib import pyplot as plt 
import seaborn as sns
import plotly.express as px
import utilidades as util

#pagina de presentacion o index
st.set_page_config(
    page_title="Analisis del CO2 y el PIB",
    initial_sidebar_state="expanded",
    layout="wide",
    page_icon="🌎"
)

#Lamamos la funcion de archivo utilidad
util.generarMenu()


#Estructura de presentación
left_col, center_col, right_col =st.columns([1,6,1],
                                    vertical_alignment="center")

#edito la columna central 
with center_col:
    st.title("Transición Energética - Analisis del CO2 y el PIB")
    st.write("""
    Relación entre las emisiones de CO₂ y el PIB en Colombia para identificar sectores 
    industriales clave y apoyar la formulación de normativas para reducir sus emisiones.

    En la pagina informes se puede observar los datos y su analisis""")
    
    imagen2 = Image.open("Media\equilibrio.png")
    st.image(imagen2, use_container_width=True, width=500,
             caption="Imagen tomada de la web.")
    
with center_col:
    st.title("RESUMEN EJECUTIVO")
    st.write("""
INTRODUCCIÓN:
        El impacto ambiental de los sectores industriales representa un desafío clave en la transición hacia un modelo económico sostenible. Este informe identifica los sectores con mayor contribución a las emisiones de CO₂ a nivel mundial, con el fin de establecer un marco comparativo para el caso de Colombia. Además, se evalúan estrategias para reducir estas emisiones sin comprometer el crecimiento económico del país.
        A través del análisis de datos sectoriales y políticas ambientales, se busca proponer soluciones que equilibren la competitividad industrial con el cumplimiento de los compromisos climáticos nacionales. Asimismo, se analiza cómo una mayor adopción de concretos, incluyendo la apertura a nuevos mercados que exigen el cumplimiento de normativas ambientales.

OBJETIVO: 
        Identificar los sectores industriales con mayor impacto ambiental en términos de emisiones de CO₂ y evaluar estrategias que permitan la reducción de emisiones sin comprometer el crecimiento económico del país.
    3. ALCANCE DEL PROYECTO
Alcances
    •	Recopilación y análisis de datos sobre emisiones de CO₂ y Producto Interno Bruto (PIB) a nivel mundial y regional.
    •	Identificación de los sectores industriales con mayor impacto ambiental en términos de emisiones de CO₂.
    •	Evaluación de la relación entre el crecimiento económico y las emisiones de CO₂.
    •	Propuesta de principios fundamentales para la implementación o mejora de políticas ambientales en Colombia.
    •	Análisis de los beneficios que la adopción de estas políticas puede generar en los sectores industriales, incluyendo oportunidades en nuevos mercados y ventajas competitivas.
Límites
    •	El estudio se basará en fuentes de datos oficiales y bases de datos públicas o de acceso permitido.
    •	El análisis se centrará en las emisiones de CO₂ como principal indicador de impacto ambiental, sin incluir otros contaminantes.
    •	La evaluación de estrategias estará enfocada en sectores industriales previamente identificados como los mayores generadores de emisiones.
    •	Las recomendaciones estarán orientadas a la viabilidad dentro del contexto económico y regulatorio de Colombia.
Exclusiones
    •	No se realizarán estudios experimentales o mediciones directas de emisiones.
    •	No se abordarán impactos ambientales distintos a las emisiones de CO₂, como contaminación del agua o deforestación.
    •	No se desarrollarán normativas o políticas específicas, sino principios y recomendaciones generales para su formulación.
    •	No se usarán datos nacionales debido a la falta de información que pueda ser contrastada con las bases de datos mundiales, ya que la muestra para Colombia es relativamente baja y limitada
4. METODOLOGÍA
    Enfoque
    El estudio adopta un enfoque cuantitativo basado en el análisis de datos para evaluar la relación entre las emisiones de CO₂ y el crecimiento económico. Se emplea una metodología descriptiva y exploratoria, permitiendo la identificación de tendencias y patrones en los sectores industriales de alto impacto ambiental.
    Técnicas Utilizadas
1.	Recopilación de Datos
    •	Identificación y descarga de bases de datos sobre emisiones de CO₂ y Producto Interno Bruto (PIB) desde fuentes oficiales.
    •	Filtrado de registros específicos para Colombia y los sectores industriales relevantes.
2.	Procesamiento y Depuración
    •	Eliminación de datos inconsistentes o incompletos.
    •	Normalización de datos para garantizar uniformidad en el análisis.
3.	Análisis Estadístico y Visualización
    •	Uso de estadística descriptiva para identificar tendencias y patrones en las emisiones de CO₂ y el PIB.
    •	Generación de gráficos comparativos para visualizar relaciones clave, como:
        1- Emisiones de CO₂ en relación con el PIB
        2- Tendencia de Emisiones de CO2 por Sector Industrial
        3- Evolución del Cambio de Temperatura Global Atribuido al CO2
        4- Emisiones totales de CO2 vs Año
        5- Relación entre PIB y Emisiones de CO₂ per cápita
4.	Interpretación y Evaluación
    •	Análisis de la calidad de los datos obtenidos.
    •	Evaluación de los hallazgos para extraer conclusiones y recomendaciones sobre la implementación de políticas ambientales.
Herramientas y Tecnologías Empleadas
    •	Bases de Datos: Data URL y repositorios abiertos con información global sobre emisiones de CO₂ y PIB.
    •	Lenguajes de Programación y Entornos:
    •	Python: Para procesamiento y análisis de datos.
    •	Google Colab: Para ejecución de scripts y limpieza de datos.
    •	Bibliotecas y Frameworks:
    •	Pandas: Para manipulación y depuración de datos.
    •	Matplotlib y Seaborn: Para visualización de datos mediante gráficos.
    •	NumPy: Para cálculos numéricos y análisis estadístico.
    •	Formatos de Datos: CSV, para facilitar la interoperabilidad de los datos entre herramientas.

5. PLANIFICACIÓN Y CRONOGRAMA
             
Fases del ProyectoS
    1.	Adquisición de Datos (Semana 1)
        •	Identificación y descarga de fuentes de datos confiables sobre emisiones de CO₂ y PIB.
        •	Verificación de la integridad y cobertura de la información recopilada.
    2.	Limpieza y Extracción (Semana 1-2)
        •	Filtrado de datos relevantes para Colombia y sectores industriales clave.
        •	Eliminación de datos inconsistentes y normalización de la información.
    3.	Análisis de los Datos (Semana 2-3)
        •	Aplicación de técnicas de estadística descriptiva para identificar tendencias y patrones.
        •	Evaluación de la relación entre emisiones de CO₂ y PIB.
    4.	Visualización y Despliegue (Semana 3-4)
        •	Creación de gráficos y representaciones visuales con Matplotlib y Seaborn.
        •	Comparación de datos entre sectores industriales y países.
    5.	Informe Ejecutivo (Semana 4)
        •	Redacción del informe con hallazgos clave y recomendaciones.
        •	Revisión final y ajustes antes de la entrega.


RESULTADOS ESPERADOS 
    Objetivos Esperados
    1.	Identificar los sectores industriales con mayor impacto ambiental en términos de emisiones de CO₂ a nivel global y su relación con Colombia.
    2.	Analizar la relación entre el crecimiento económico y las emisiones de CO₂ mediante el estudio del PIB y los datos de emisiones.
    3.	Evaluar estrategias para la reducción de emisiones sin comprometer el desarrollo económico de los sectores industriales.
    4.	Proponer principios fundamentales para la formulación de políticas ambientales en Colombia, basados en análisis de datos y tendencias globales.
    5.	Presentar información clara y visualmente accesible mediante gráficos y análisis estadísticos que permitan una interpretación efectiva de los datos.

 Beneficios del Proyecto
    1.	Toma de decisiones basada en datos: Proporciona información fundamentada para el diseño de políticas ambientales eficaces.
    2.	Optimización de estrategias de reducción de CO₂: Permite a los sectores industriales conocer su impacto ambiental y adoptar medidas adecuadas.
    3.	Oportunidades en nuevos mercados: Facilita la identificación de ventajas competitivas para empresas que adopten estándares ambientales internacionales.
    4.	Fortalecimiento de la competitividad industrial: Equilibra el cumplimiento de normativas ambientales con el crecimiento económico del país.
    5.	Mayor comprensión del impacto de las emisiones: Aporta evidencia visual y estadística sobre las tendencias de emisiones en relación con el PIB.
    Entregables del Proyecto
    1.	Base de datos procesada con información sobre emisiones de CO₂ y PIB, filtrada y estructurada para su análisis.
    2.	Gráficos y visualizaciones que representen de manera clara la relación entre emisiones de CO₂, sectores industriales y PIB.
    3.	Análisis estadístico detallado con tendencias, patrones y correlaciones identificadas.
    4.	Informe Ejecutivo Final, que incluya:
        •	Resumen de hallazgos clave.
        •	Evaluación de estrategias y propuestas de principios para políticas ambientales.
        •	Conclusiones y recomendaciones basadas en el análisis de datos.
 Indicadores de Éxito
    1.	Precisión de los datos: Depuración y validación del 100% de los registros utilizados en el análisis.
    2.	Visualización efectiva: Creación de al menos 5 gráficos clave que representen las tendencias más relevantes.
    3.	Calidad del informe final: Documento estructurado con análisis fundamentado, revisado y validado según estándares académicos o empresariales.
    4.	Relevancia de las recomendaciones: Propuestas alineadas con tendencias globales en políticas ambientales y aplicables al contexto colombiano.
    5.	Cumplimiento del cronograma: Finalización de cada fase dentro de las 4 semanas establecidas.""")