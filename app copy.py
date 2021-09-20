from flask import Flask
from flask import request
from flask import render_template
import pandas as pd
import os

import csv
import json
import folium
from folium.plugins import HeatMap

app = Flask(__name__)

@app.route('/drawMap')
def draw_map():
    map_data = pd.read_csv("/Users/ryan/Desktop/Project3_challenge/UFO_Sightings_scrubbedfinal.csv")

    lat = map_data["latitude"].mean()
    lon = map_data["longitude"].mean()
    startingLocation = [lat, lon]

    hmap = folium.Map(location=startingLocation, zoom_start=15)

    hm_wide = HeatMap(list(zip(map_data.latitude.values, map_data.longitude.values, map_data.shape.values)),
                        min_opacity=0.2,
                        radius=17, blur=15,
                        max_zoom=1
                    
                    )

    hmap.add_child(hm_wide)
    hmap.save(os.path.join('heatmap.html'))

    return render_template('heatmap.html')