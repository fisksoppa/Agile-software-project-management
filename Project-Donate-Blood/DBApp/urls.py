from importlib.resources import path
from django.urls import path
from .import views

# The different URL paths possible
urlpatterns = [
    path('', views.folium_map, name='map1'),
    path('list/', views.df_list, name='list'),
    path('about/', views.about, name='about'),
    path('search/', views.search_result, name='search')

]