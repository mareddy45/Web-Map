import folium
import pandas

data= pandas.read_csv("volcanoes.txt")
lat= list(data["LAT"])
lon= list(data["LON"])

map=folium.Map(location=[17.385,78.486], zoom_start=6, tiles="Stamen Terrain")
map.add_child(folium.Marker(location=[17.385,78.486], popup="Birth Place", icon=folium.Icon(color="red")))

fg = folium.FeatureGroup(name="Map")

for lt, ln in zip(lat,lon):
    fg.add_child(folium.Marker(location=[lt,ln], popup="volcanoes", icon=folium.Icon(color="red")))

map.add_child(fg)

map.save("Map.html")
