import folium
import pandas

data= pandas.read_csv("volcanoes.txt")
lat= list(data["LAT"])
lon= list(data["LON"])
elev= list(data["ELEV"])
name= list(data["NAME"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

def color_producer(elevation):
    if elevation < 1000:
        return 'red'
    elif 1000<=elevation<3000:
        return 'blue'
    else:
        return 'orange'

map=folium.Map(location=[34.05,-118.246], zoom_start=5, tiles="Stamen Terrain")
map.add_child(folium.Marker(location=[17.385,78.486], popup="Birth Place", icon=folium.Icon(color="green")))
map.add_child(folium.Marker(location=[34.05,-118.246], popup="Current Place", icon=folium.Icon(color="green")))

fg = folium.FeatureGroup(name="Map")

for lt, ln, el, name in zip(lat,lon,elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius= 6, popup=folium.Popup(iframe), fill_color=color_producer(el), color='grey', fill_opacity=0.7))

map.add_child(fg)

map.save("Map.html")
