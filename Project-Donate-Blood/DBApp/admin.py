from django.contrib import admin
from .models import *

# Register your models here.

#Makse the ../admin   tab useble, where the search results are stored.
admin.site.register(Search)