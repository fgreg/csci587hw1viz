import os
import pathlib

import folium
import geopandas
import pandas as pd
import pyproj.crs
from folium.plugins import FastMarkerCluster

checkins_df = pd.read_csv('https://drive.google.com/uc?export=download&id=1JhMvpBI1GoRhICImQjQrZvp6PMBpvAHJ',
                          delim_whitespace=True, header=None,
                          names=['userid', 'locationid', 'hours_since_epoch', 'lat', 'lon'])

checkins_gdf = geopandas.GeoDataFrame(
    checkins_df, geometry=geopandas.points_from_xy(checkins_df.lon, checkins_df.lat),
    crs=pyproj.CRS.from_epsg(4326))

# print(checkins_gdf.sample(1000))


m = folium.Map([35.55, 139.49], zoom_start=10, tiles='cartodbpositron')

popups, locations = [], []
for idx, row in checkins_gdf.iterrows():
    locations.append([row['geometry'].y, row['geometry'].x])
    popups.append(folium.Popup(checkins_gdf.iloc[idx, :]))

FastMarkerCluster(locations, popups=popups).add_to(m)

# folium.GeoJson(checkins_gdf).add_to(m)
pathlib.Path("./results").mkdir(parents=True, exist_ok=True)
with open(os.path.join('results', 'geopandas_0.html'), 'wb') as outfile:
    m.save(outfile)
