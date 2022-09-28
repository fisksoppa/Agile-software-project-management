from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import *


class SearchForm(forms.ModelForm):
    address = forms.CharField(label='')

    class Meta:
        model = Search
        fields = ['address', ]