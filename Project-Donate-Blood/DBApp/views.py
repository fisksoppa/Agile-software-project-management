from django.shortcuts import render
from django.http import HttpResponse

#This shows what you want the index page to show.
def index(request):
    return HttpResponse("Blank Test Page for project!")
# Create your views here.
