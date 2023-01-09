# First install the folium package and create a virtual environment

# Folium for plotting maps
import folium
import pandas as pd


# Create a map instance
m = folium.Map(location=[-0.15386345206107715, 34.86414568574279],
               zoom_start=10,
               control_scale=True,
               prefer_canvas=True)

# Creating the choropleth map
# Using pandas to read the data from wards.csv
ward_geo = f"wards.geojson"
ward_malaria = f"wards.csv"
ward_data = pd.read_csv(ward_malaria)

folium.Choropleth(
    geo_data=ward_geo,
    name="choropleth",
    data=ward_data,
    columns=['wardcode', 'Total_co'],
    key_on='feature.properties.wardcode',
    fill_color="YlGn",
    fill_opacity=0.5,
    line_opacity=0.2,
    legend_name="Total Confirmed Malaria  Cases in Kisumu",
).add_to(m)

# Adding the tile control layer for the different tiles in Kisumu County
folium.TileLayer('openstreetmap').add_to(m)
folium.TileLayer('cartodbdark_matter').add_to(m)
folium.TileLayer('Stamen terrain').add_to(m)
folium.LayerControl().add_to(m)

# Add customized tooltips to the map
folium.features.GeoJson(
                    data=ward_data,
                    name='Total Confirmed Malaria Cases in Kisumu',
                    smooth_factor=2,
                    style_function=lambda x: {'color': 'black', 'fillColor': 'transparent', 'weight': 0.5
                                              },
                    tooltip=folium.features.GeoJsonTooltip(
                        fields=['wardcode',
                                'ward',
                                'Total_co',
                                'Confirme',
                                'Confirm1'
                                'Malaria_'],
                        aliases=["Ward Code:",
                                 "Ward Name:",
                                 "Total Confirmed cases in all age groups:",
                                 "Confirmed cases in children under age 5):",
                                 "Confirmed cases greater under the age of 5:"
                                 "Confirmed cases in pregnant women:"],
                        localize=True,
                        sticky=False,
                        labels=True,
                        style="""
                            background-color: #F0EFEF;
                            border: 2px solid black;
                            border-radius: 3px;
                            box-shadow: 3px;
                        """,
                        max_width=800,),
                    highlight_function=lambda x: {'weight': 3, 'fillColor': 'grey'},
                        ).add_to(m)
# Add marker
# Run: help(folium.Icon) for more info about icons

folium.Marker(
    location=[-0.08250945647176255, 34.7275401708176],
    popup='Kisumu International AirPort',
    icon=folium.Icon(color='green', icon='ok-sign'),
).add_to(m)

m.save('index.html')
