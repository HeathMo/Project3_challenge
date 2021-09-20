import numpy as np
import pandas as pd
import gmaps
import gmaps.datasets
import folium

map_data = pd.read_csv("/Users/ryan/Desktop/Project3_challenge/UFO_Sightings_scrubbedfinal.csv")

m = folium.Map(location=[45.5236, -122.6750])

m