from http.client import HTTPResponse
from pydoc import render_doc
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .database import *
import pandas as pd
import folium
import geocoder
from geopy.distance import geodesic
import operator
import matplotlib



#For creating the list of df which show all results.
#Located in the URL: ../test
def df_list(request):
    df1 = df.to_html()
    return HttpResponse(df1)


#Sends request to render about us page.
def about(request):
    return render(request, "about.html")

def pins_on_map(map):
    #For making the pin for either Bus or Clinic and shows oppening hrs, For the homepage URL
    for index, loc_info in df.iterrows():
        if loc_info['Clinic or Bus'] == 'Bus':
            folium.Marker([loc_info["Latitude"],loc_info["Longitude"]],popup= folium.Popup(loc_info["Opening Hours"], max_width=170), icon = folium.Icon(color = 'red', icon = 'ambulance', prefix = 'fa'), tooltip = loc_info['Place']).add_to(map)
        else:
            folium.Marker([loc_info["Latitude"],loc_info["Longitude"]],popup= folium.Popup(loc_info["Opening Hours"], max_width=170), icon = folium.Icon(color = 'red', icon = 'home', prefix = 'fa'),  tooltip = loc_info['Place']).add_to(map)
    return map


#Makes the grid view fot the map and also create the location pins
def folium_map(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('search')
    else:
        form = SearchForm()

    map = folium.Map(location=[57.708870, 11.974560], zoom_start = 11)

    # Creates the pins on the map
    pins_on_map(map)

    map = map._repr_html_()
    context = {
        'map':  map,
        'form': form,
    }
    return render(request, 'DBApp/map.html', context)

#The URL for the mainpage
#The URL is: ../test1
def search_result(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('search')
    else:
        form = SearchForm()

    address = Search.objects.all().last()
    location = geocoder.osm(str(address) + ', ' + 'gothenburg')
    
    lat, lng = location.lat, location.lng
    coordinates = (lat,lng)

    #Handles invalid long- or latitude input
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('You address input is invalid')

    #Method for appending the long- and latitude
    distance = []
    for i in range(len(df)):
          distance.append([i, geodesic(coordinates, (float(df['Latitude'][i]), float(df['Longitude'][i]))).km])

    #Get the [index, distance] for the 5 nearest locations
    Five_closest_location_sorted = sorted(distance, key=operator.itemgetter(1))[0:5]
 
    
    #sorted by distance in array with index, distance
    index = [item[0] for item in Five_closest_location_sorted]
    distance = [item[1] for item in Five_closest_location_sorted]
    

    #new df with info from original df of the 5 closest places
    
    df_2 = df.iloc[index]
    df_3 = df_2.drop(['Latitude','Longitude'],axis=1)
    df_3['Distance (km)']=distance
  

    #Style the dataframe
    df_3 = df_3.style.background_gradient(axis=0, gmap=df_3['Distance (km)'], cmap='Greys').hide(axis='index')
        

    #convert df to html so i can show it on the webpage
    
    df_3html = df_3.to_html(index_names=False)
  
    #Centers the map on Guthenburg
    map = folium.Map(location=[57.708870, 11.974560], zoom_start = 11)

    # Creates the pins on the map
    pins_on_map(map)
  
    folium.Marker([lat, lng], tooltip='Click for more', popup=location.address).add_to(map)
    
        
    # Get HTML Representation of Map Object
    map = map._repr_html_()
    context = {
        'map': map,
        'form': form,
        'list': df_3html,
    }
    return render(request, 'DBApp/search.html', context)
