from importlib.resources import path
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.folium_map, name='map'),
    path('lucas/', views.lucas, name='public')
]