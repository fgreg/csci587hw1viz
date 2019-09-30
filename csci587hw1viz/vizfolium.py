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

print(checkins_gdf.head())


m = folium.Map([35.55, 139.49], zoom_start=10, tiles='cartodbpositron')

popups, locations = [], []
for idx, row in checkins_gdf.iterrows():
    locations.append([row['geometry'].y, row['geometry'].x, row['userid'], idx])

callback = """
function (row) {
    var icon = L.AwesomeMarkers.icon();
    var marker = L.marker(new L.LatLng(row[0], row[1]));
    marker.setIcon(icon);
    var popup = L.popup({maxWidth: '300'});
    const display_text = {text: 'userid='+row[2]+', checkin#='+row[3]};
    var mytext = $(`<span>${display_text.text}</span>`)[0];
    popup.setContent(mytext);
    marker.bindPopup(popup);
    return marker;
};"""

FastMarkerCluster(locations, callback=callback).add_to(m)

# folium.GeoJson(checkins_gdf).add_to(m)
pathlib.Path("./results").mkdir(parents=True, exist_ok=True)
with open(os.path.join('results', 'geopandas_0.html'), 'wb') as outfile:
    m.save(outfile)
