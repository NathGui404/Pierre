import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import requests


st.title('Ceci est un magnifique LiveCoding fourni par Pierre Mur!')
st.write("PS : c'est un super formateur de la Wild Code School")

df = pd.read_csv("velib.csv")

# Quasiment tous les éléments streamlit peuvent être affichés dans la "sidebar"
st.sidebar.image('pierre_mur[1].jpg', width=300)
st.sidebar.title("Cette Sidebar est inutile mais rien ne vaut une photo de Pierre Mur pour égayer votre journée de Novembre !")
st.sidebar.write("Pierre Mur , formateur EMERITUS de la Wild CODE SCHOOL. Tous droits à l'image réservés tout ça !")

        
option_velo = st.sidebar.selectbox(
	    'Quel type de vélo ?',
	    ('mechanical', 'ebike'))

# On peut créer plusieurs "colonnes" pour afficher des éléments côte à côte
# La liste qui suit contient 2 éléments, il y aura donc 2 colonnes
# La première colonne a un poids de "2", elle sera donc 2 fois plus large
col1, col2 = st.columns([2, 1])

# Les éléments à afficher dans chaque colonne :
with col1:
	fig, ax = plt.subplots()
	ax = sns.boxplot(df[option_velo])
	st.pyplot(fig)
with col2:
	fig, ax = plt.subplots()
	ax = sns.boxplot(df[option_velo])
	st.pyplot(fig)
# Ici, nous repartons en centré pleine page, sans les colonnes
link_station = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"
r_stations = requests.get(link_station)
df_stations = pd.json_normalize(r_stations.json()['data']['stations'])
df_merge = pd.merge(left = df,
         right = df_stations,
         on = "station_id")

fig_heatmap = px.density_mapbox(df_merge,
                        lat='lat',
                        lon='lon',
                        z=option_velo,
                        radius=20,
                        center=dict(lat=48.865983, lon=2.275725	),
                        zoom=10,
                        mapbox_style="stamen-terrain")
st.plotly_chart(fig_heatmap)
