# First install the folium package and create a virtual environment
# Create a map instance
import folium
m = folium.Map(location=[-0.15386345206107715, 34.86414568574279], zoom_start=12,
               control_scale=True, prefer_canvas=True)
# Add marker
# Run: help(folium.Icon) for more info about icons
folium.Marker(
    location=[-0.08250945647176255, 34.7275401708176],
    popup='Kisumu International AirPort',
    icon=folium.Icon(color='green', icon='ok-sign'),
).add_to(m)

m.save('map.html')
