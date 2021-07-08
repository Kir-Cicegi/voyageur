from django import forms
from django.forms import ModelForm

from .models import *


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = '__all__'

class AttractionForm(ModelForm):
  class Meta:
    model = Attractions
    fields = ['date', 'attraction']

class AirlineForm(ModelForm):
  class Meta:
    model = Airline
    fields = '__all__'