'''
Created on Apr 15, 2018

@author: Scott
'''

# Import libraries
import pandas as pd
import folium   #---------------IF YOU WANT TO TRY YOURSELF MAKE SURE TO DOWNLOAD FOLIUM AND-------->
import os  
import json                #----------------JSON---------------->
import geopandas                  #--------------GEOPANDAS--------->
from branca.colormap import linear #--------------BRANCA COLORMAP-------->
import branca.colormap as cm

us_states = os.path.join('US_State.txt')
geo_json_data = json.load(open(us_states))
us_unemployment = os.path.join('US_Unemployment.csv')
unemployment = pd.read_csv(us_unemployment)

df = pd.read_csv('US_Capitals.csv')


m = folium.Map([43, -100], zoom_start=4)             #--------------CREATES the MAP---------->

def color(number):
    if number >= 6:
        col = 'darkblue'
    elif number >= 5:
        col = 'blue'
    elif number >= 4:
        col = 'lightblue'
    elif number >= 3:
        col = 'purple'
    else:
        col = 'pink'
    return col

for lat,lon,name,number in zip(df['latitude'], df['longitude'], df['description'], unemployment['Unemployment']):             #------------SELECTS THE COLUMN NAMES IN THE FILE US_CAPITALS--------->
    folium.Marker(location=[lat,lon], popup= name + '  ' + str(number) + '%', icon = folium.Icon(color = color(number), icon = 'dot')).add_to(m)

m.choropleth(
    geo_data=us_states,
    data=unemployment,
    columns=['State', 'Unemployment'],
    key_on='feature.id',
    fill_color='PuBu',
    highlight=True
)


m.save(os.path.join('test.html'))        #-----------SAVES TO FILE TEST.HTML, OPEN TEST.HTML TO VIEW THE MAP---------->

m


