from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
import pandas as pd
import folium
import geocoder
from geopy.distance import geodesic
import operator
import numpy as np

#This shows what you want the index page to show.
#This is the "homepage"
def index(request):
    return HttpResponse("Blank Test Page for project!")



#For creating the list of df which show all results.
#Located in the URL: ../test
def test(request):
    df1 = df.to_html()
    
    return HttpResponse(df1)


#Makes the grid view fot the map and also create the location pins
def folium_map(request):
    #Centers the map on Guthenburg
    map = folium.Map(location=[57.708870, 11.974560], zoom_start = 11)

    #For making the pin for either bus or clinic and shows oppening hrs
    for index, loc_info in df.iterrows():
        if loc_info['Clinic or bus'] == 'bus':
            folium.Marker([loc_info["Latitude"],loc_info["Longitude"]],popup= folium.Popup(loc_info["Day and Time"], max_width=170), icon = folium.Icon(color = 'red', icon = 'ambulance', prefix = 'fa'), tooltip = loc_info['Place']).add_to(map)
        else:
            folium.Marker([loc_info["Latitude"],loc_info["Longitude"]],popup= folium.Popup(loc_info["Day and Time"], max_width=170), icon = folium.Icon(color = 'red', icon = 'home', prefix = 'fa'),  tooltip = loc_info['Place']).add_to(map)

    map = map._repr_html_()
    context = {
        'map':  map,
    }
    return render(request, 'DBApp/map.html', context)

#The URL for the mainpage
#The URL is: ../test1
def test1(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('test1')
    else:
        form = SearchForm()
    address = Search.objects.all().last()
    location = geocoder.osm(str(address) + ', ' + 'gothenburg')
    
    lat = location.lat
    lng = location.lng
    coordinates = (lat,lng)

    #Handles invalid long- or latitude input
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('You address input is invalid')

    #Method for appending the long- and latitude
    distance = []
    for i in range(len(df)):
          distance.append([i, geodesic(coordinates, (float(df['Latitude'][i]), float(df['Longitude'][i]))).km])

    distance_sorted = distance
    distance_sorted = sorted(distance_sorted, key=operator.itemgetter(1))

    #sorted by distance in array with index, distance
    print(distance_sorted)
    test = [item[0] for item in distance_sorted]
    #just the indexes
    print(test)

    test_take = test[0:5]
    #closest 5 indexes
    print(test_take)

    df_2 = df.iloc[df.index.isin(test_take)]
    #new df with info from original df of the 5 closest places
    print(df_2)
    #convert df to html so i can show it on the webpage
    df_2html = df_2.to_html()
    # Create Map Object
    map = folium.Map(location=[57.708870, 11.974560], zoom_start = 11)

    #For making the pin for either bus or clinic and shows oppening hrs
    for index, loc_info in df.iterrows():
        if loc_info['Clinic or bus'] == 'bus':
            folium.Marker([loc_info["Latitude"],loc_info["Longitude"]],popup= folium.Popup(loc_info["Day and Time"], max_width=170), icon = folium.Icon(color = 'red', icon = 'ambulance', prefix = 'fa'), tooltip = loc_info['Place']).add_to(map)
        else:
            folium.Marker([loc_info["Latitude"],loc_info["Longitude"]],popup= folium.Popup(loc_info["Day and Time"], max_width=170), icon = folium.Icon(color = 'red', icon = 'home', prefix = 'fa'),  tooltip = loc_info['Place']).add_to(map)


    folium.Marker([lat, lng], tooltip='Click for more', popup=location.address).add_to(map)
    
        
    # Get HTML Representation of Map Object
    map = map._repr_html_()
    context = {
        'map': map,
        'form': form,
        'list': df_2html,
    }
    return render(request, 'DBApp/test.html', context)