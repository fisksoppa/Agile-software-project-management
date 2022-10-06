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



#For creating the list of df which show all results.
#Located in the URL: ../test
def df_list(request):
    df1 = df.to_html()
    return HttpResponse(df1)


#Makes the grid view fot the map and also create the location pins
def folium_map(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('search')
    else:
        form = SearchForm()

    #Centers the map on Guthenburg
    map = folium.Map(location=[57.708870, 11.974560], zoom_start = 11)

    #For making the pin for either Bus or Clinic and shows oppening hrs
    for index, loc_info in df.iterrows():
        if loc_info['Clinic or Bus'] == 'Bus':
            folium.Marker([loc_info["Latitude"],loc_info["Longitude"]],popup= folium.Popup(loc_info["Opening Hours"], max_width=170), icon = folium.Icon(color = 'red', icon = 'ambulance', prefix = 'fa'), tooltip = loc_info['Place']).add_to(map)
        else:
            folium.Marker([loc_info["Latitude"],loc_info["Longitude"]],popup= folium.Popup(loc_info["Opening Hours"], max_width=170), icon = folium.Icon(color = 'red', icon = 'home', prefix = 'fa'),  tooltip = loc_info['Place']).add_to(map)

    
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
    
    index_sorted = distance_sorted[0:5]
    index_sorted = sorted(index_sorted, key=operator.itemgetter(0))
    

    #sorted by distance in array with index, distance
    
    test = [item[0] for item in distance_sorted]
    testdistance = [item[1] for item in index_sorted]
    testdistance1 = testdistance[0:5]
    #just the indexes
    

    test_take = test[0:5]
    #closest 5 indexes
    

    df_2 = df.iloc[df.index.isin(test_take)]
    #new df with info from original df of the 5 closest places
  
    df_3 = df_2.drop(['Latitude','Longitude'],axis=1)
    df_3['Distance (km)']=testdistance1
    df_3 = df_3.sort_values('Distance (km)')
    
    #convert df to html so i can show it on the webpage
    df_3html = df_3.to_html(index=False)
   
    #Centers the map on Guthenburg
    map = folium.Map(location=[57.708870, 11.974560], zoom_start = 11)

    #For making the pin for either Bus or Clinic and shows oppening hrs
    for index, loc_info in df.iterrows():
        if loc_info['Clinic or Bus'] == 'Bus':
            folium.Marker([loc_info["Latitude"],loc_info["Longitude"]],popup= folium.Popup(loc_info["Opening Hours"], max_width=170), icon = folium.Icon(color = 'red', icon = 'ambulance', prefix = 'fa'), tooltip = loc_info['Place']).add_to(map)
        else:
            folium.Marker([loc_info["Latitude"],loc_info["Longitude"]],popup= folium.Popup(loc_info["Opening Hours"], max_width=170), icon = folium.Icon(color = 'red', icon = 'home', prefix = 'fa'),  tooltip = loc_info['Place']).add_to(map)

    folium.Marker([lat, lng], tooltip='Click for more', popup=location.address).add_to(map)
    
        
    # Get HTML Representation of Map Object
    map = map._repr_html_()
    context = {
        'map': map,
        'form': form,
        'list': df_3html,
    }
    return render(request, 'DBApp/search.html', context)