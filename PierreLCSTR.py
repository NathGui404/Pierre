
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import requests

# Ici, nous repartons en centré pleine page, sans les colonnes
link_station = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"
r_stations = requests.get(link_station)
df_stations = pd.json_normalize(r_stations.json()['data']['stations'])

fig_heatmap = px.density_mapbox(df_stations, 
                        lat='lat', 
                        lon='lon', 
                        radius=20,
                        center=dict(lat=48.865983, lon=2.275725	), 
                        zoom=10,
                        mapbox_style="stamen-terrain")
st.plotly_chart(fig_heatmap)