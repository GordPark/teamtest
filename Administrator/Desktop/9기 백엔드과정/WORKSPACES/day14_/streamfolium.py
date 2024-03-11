import folium
import pandas as pd
import json
m = folium.Map(location=[37.5665, 126.9780], zoom_start=10)

folium.Choropleth(
    geo_data='seoul_municipalities_geo.json',
    name='choropleth',
    data=pd.DataFrame({
        'region': ['Seoul', 'Busan'],
        'value': [50, 500]
    }),
    columns=['region', 'value'],
    key_on='feature.properties.name',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Value'
).add_to(m)

m.save('south_korea_choropleth.html')