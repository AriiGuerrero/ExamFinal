# Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from PIL import Image
from sqlalchemy import create_engine
from matplotlib import ticker
from sqlalchemy import create_engine
#from pandas_profiling import ProfileReport
from matplotlib import ticker
from matplotlib.ticker import AutoMinorLocator
sns.set_style('white')

from collections import namedtuple
from math import radians, acos, asin, cos, sin, atan, degrees, sqrt

# Insert an icon
icon = Image.open("Resources/logo.jpg")

# State the design of the app
st.set_page_config(page_title="EmisionesCo2", page_icon=icon)

# Insert css codes to improve the design of the app
st.markdown(
    """
<style>
h1 {text-align: center;
}
body {background-color: #DCE3D5;
      width: 1400px;
      margin: 15px auto;
}
</style>""",
    unsafe_allow_html=True,
)

# Title of the app
st.title("Emisiones de CO2 de fuentes estacionaria :link:")

st.write("---")

# Add information of the app
st.markdown(
    """ This app is used to visualize dataframe for emisiones CO2, to upload csv files, 
to call data, and to realize graphic.

**Python Libraries:** Streamlit, pandas, plotly, PIL.
"""
)

# Add additional information
expander = st.expander("About")
expander.write("This app is very useful for final exam")

# Insert image
image = Image.open("Resources/contaminacion.png")
st.image(image, width=100, use_column_width=True)

st.caption("La industria del refinado de petróleo desempeña un papel crucial tanto en "
           "la cadena de suministro de energía como en el cambio climático y es el tercer "
           "mayor emisor estacionario de gases de efecto invernadero en el mundo, "
           "contribuyendo con el 6% de todas las emisiones industriales de gases de efecto invernadero. "
           "En concreto, el CO2 representa aproximadamente el 98% de los gases de efecto "
           "invernadero emitidos por las refinerías de petróleo")


# Insert video
st.subheader("**EMISIONES DE CO2 POR FUENTES ESTACIONARIAS**")
st.caption("Así nos encontramos con que los mayores emisores de CO2 que existen actualmente "
           "en el mundo son también las mayores potencias económicas del planeta. "
           "El vertiginoso desarrollo que China ha llevado a cabo durante las últimas dos "
           "décadas ha tenido un evidente impacto en las emisiones de dióxido de carbono, "
           "aunque esta cifra quede más difuminada si consideramos la elevada población "
           "que tiene el país asiático. Le sigue Estados Unidos y otra mezcla de potencias "
           "al alza y consolidadas como India, Rusia, Alemania o Japón, países donde el "
           "sector industrial tiene un peso importante dentro de la economía nacional.")



# Sidebar
Logo = Image.open("Resources/ESPOL.png")
st.sidebar.image(Logo)

# Add title to the sidebar section
st.sidebar.title(":arrow_down: **Navigation**")


# Pages
with st.sidebar:
    options = option_menu(
        menu_title="Menu",
        options=["Home", "Data", "Plots"],
        icons=["house", "tv-fill", "box"],)

def data(dataframe):
    st.header("**Dataframe header**")
    st.write(dataframe.head())
    st.header("**Statistical information**")
    st.write(dataframe.describe())


# Call dataframe

# Call web app sections
if options == "Data":
    engine = create_engine('sqlite:///Data/CO2_EOR(1).db')
    df = pd.read_sql_query("SELECT* FROM R_Shushufindi", engine)
    df.columns

    ter = pd.read_sql_query("SELECT* FROM Datos_termoelectricas", engine)
    ter.head()
    ter_ama = ter[ter['Termoelectrica'] == 'Amazonas']
    ter_ama


elif options == "Plots":
    #refineria
    fig1, ax = plt.subplots(figsize=(14, 8))
    formatter = ticker.EngFormatter()
    ax.bar(df['año'], df['RefinacionBarriles'], color='navy')
    ax.set_xlabel('Year', fontsize=18)
    ax.set_ylabel('Oil refined (MMbbl)', fontsize=20)
    ax.tick_params(axis='x', labelsize=18)
    ax.tick_params(axis='y', labelsize=18)
    ax.yaxis.set_major_formatter(formatter)
    # ax.set_xticks(ax.get_xticks())
    ax.set_title('Oil refined of the refinery Sushufindi',
                 fontname="Times New Roman", size=20, fontweight="bold")
    plt.xticks([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
    plt.show()
    fig6, ax = plt.subplots(figsize=(12, 8))

    fig7, ax = plt.subplots(figsize=(12, 8))

#AMAZONAS
    engine = create_engine('sqlite:///Data/CO2_EOR.db')
    ter = pd.read_sql_query("SELECT* FROM Datos_termoelectricas", engine)
    ter.head()
    ter_ama = ter[ter['Termoelectrica'] == 'Amazonas']
    ter_ama

    ax.bar(ter_ama['año'], ter_ama['EmisionCO2[Ton]'], color='red')
    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel(r'$CO_{2}$ emissions (Ton)', fontsize=14)
    ax.set_title(r'Anual $CO_{2}$ emissions of the thermal plant Amazonas',
                 fontname="Times New Roman", size=20, fontweight="bold")
    plt.show()

    ax.bar(ter_ama['año'], ter_ama['EnergiaBruta(MWH)'], color='seagreen')
    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel('Net energy (MWH)', fontsize=14)
    ax.set_title('Anual energy production of the thermal plant Amazonas',
                 fontname="Times New Roman", size=20, fontweight="bold")
    plt.show()
