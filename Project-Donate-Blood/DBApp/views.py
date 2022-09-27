from django.shortcuts import render
from django.http import HttpResponse
from .models import df
import pandas as pd
import folium

#This shows what you want the index page to show.
def index(request):
    return HttpResponse("Blank Test Page for project!")
# Create your views here.







def folium_map(request):
    map = folium.Map(location=[57.708870, 11.974560], zoom_start = 11)


    for index, loc_info in df.iterrows():
        if loc_info['Clinic or bus'] == 'bus':
            folium.Marker([loc_info["Latitude"],loc_info["Longitude"]],popup= folium.Popup(loc_info["Day and Time"], max_width=170), icon = folium.Icon(color = 'red', icon = 'ambulance', prefix = 'fa'), tooltip = loc_info['Place']).add_to(map)
        else:
            folium.Marker([loc_info["Latitude"],loc_info["Longitude"]],popup= folium.Popup(loc_info["Day and Time"], max_width=170), icon = folium.Icon(color = 'red', icon = 'home', prefix = 'fa'),  tooltip = loc_info['Place']).add_to(map)

    map = map._repr_html_()
    context = {
        'map':  map,
    }
    return render(request, 'DBApp/test.html', context)
    

def lucas(request):
    context = {}
    return render(request, 'DBApp/lucas.html', context)