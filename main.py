# First install the folium package and create a virtual environment

# Folium for plotting maps
import folium


# Create a map instance
m = folium.Map(location=[-0.15386345206107715, 34.86414568574279],
               zoom_start=12,
               control_scale=True,
               prefer_canvas=True)

# Adding the Kisumu County Ward Boundaries
folium.GeoJson('facilities.geojson', name='Facilities').add_to(m)


# Adding the tile control layer for the different tiles in Kisumu County
folium.TileLayer('openstreetmap').add_to(m)
folium.TileLayer('cartodbdark_matter').add_to(m)
folium.LayerControl().add_to(m)

# Add marker
# Run: help(folium.Icon) for more info about icons

folium.Marker(
    location=[-0.08250945647176255, 34.7275401708176],
    popup='Kisumu International AirPort',
    icon=folium.Icon(color='green', icon='ok-sign'),
).add_to(m)

m.save('index.html')
