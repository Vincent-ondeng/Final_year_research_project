# Final_year_research_project
## Folium Choropleth Map for Total Confirmed Malaria Cases in Kisumu 
This code generates an interactive choropleth map of Kisumu county that
displays the total confirmed malaria cases in each ward. The map was
created using the folium library and the data was read from a CSV file
(wards.csv). 
The choropleth map is a type of map that displays data as
colored polyggon regions. The color intensity of each region corresponds
to the value of a particular data attribute, in this case the total
confirmed malaria cases.

## Required Libraries To run this code, the following libraries need to be installed:

Folium 
Pandas 
Input Data The input data for this code is a CSV file
named "wards.csv". This file contains information about the total
confirmed malaria cases in each ward in Kisumu county.

## Features of the Map Choropleth map: 
This map displays the total confirmed malaria cases in each ward as a colored polygon region. 
The color intensity of each region corresponds to the value of the total confirmed malaria cases.

## Tile Layers: The code allows the user to choose from three different
tile layers (Openstreetmap, Cartodbdark\_matter, and Stamen terrain) to
display the underlying map. The user can also switch between the tile
layers using the Layer Control feature.

## Geojson Tooltips: The map includes Geojson tooltips that display
detailed information about each ward when the user hovers over a
particular region. The tooltips display the following fields:

## Ward Code Ward Name Total Confirmed cases in all age groups Confirmed
cases in children under age 5 Confirmed cases greater under the age of 5
Confirmed cases in pregnant women Marker: The code also includes a
marker that represents the location of Kisumu International Airport.

## Output 
The code generates an HTML file named "index.html". 
This file can be opened in a web browser to view the interactive choropleth map.

How to Run the Code Clone the repository containing the code. Install
the required libraries using the following command: pip install folium
pandas Run the code using the following command: python
folium\_choropleth\_map.py Open the generated HTML file "index.html" in
a web browser to view the map.
