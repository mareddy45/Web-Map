import folium
import pandas

data= pandas.read_csv("volcanoes.txt")
lat= list(data["LAT"])
lon= list(data["LON"])
elev= list(data["ELEV"])

map=folium.Map(location=[34.05,-118.246], zoom_start=3, tiles="Stamen Terrain")
map.add_child(folium.Marker(location=[17.385,78.486], popup="Birth Place", icon=folium.Icon(color="green")))
map.add_child(folium.Marker(location=[34.05,-118.246], popup="Current Place", icon=folium.Icon(color="green")))

fg = folium.FeatureGroup(name="Map")

for lt, ln, el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln], popup= str(el)+ " m", icon=folium.Icon(color="red")))

map.add_child(fg)

map.save("Map.html")
