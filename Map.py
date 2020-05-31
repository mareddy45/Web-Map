import folium
map=folium.Map(location=[17.385,78.486], zoom_start=6, tiles="Stamen Terrain")
map.add_child(folium.Marker(location=[17.385,78.486], popup="Birth Place", icon=folium.Icon(color="red")))
map.save("Map.html")
