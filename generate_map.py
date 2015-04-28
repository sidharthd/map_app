# Generates an HTML file to render the map of India with overlays for states.

import folium
from pandas import read_csv

csv_data = read_csv('static/air_quality_2011_states.csv')

map = folium.Map(location=[25, 83], zoom_start=4, width=553, height=590, tiles='Stamen Terrain')

map.geo_json(geo_path='static/india_states.geojson',
            data=csv_data,
            data_out='static/air_data.json',
            columns=['State', 'SO2 Annual average'],
            key_on='feature.properties.NAME_1',
            threshold_scale=[10,20],
            fill_color='YlOrRd', line_opacity=0.2)

map.create_map(path='templates/map_generated.html')