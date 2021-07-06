from django import forms
from django.forms import ModelForm

from .models import *



class CityForm(ModelForm):
    # name= forms.CharField(max_length=80, widget= forms.TextInput(attrs={'placeholder':'Name of the City'}))
    # country= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Name of the Country'}))
    # fav_spot= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Your favourite spot there'}))
    # fav_local_food= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Favourite local food you tried there'}))
    # days_spent= forms.IntegerField(widget= forms.NumberInput(attrs={'placeholder':'How many days you spent there?'}))
    class Meta:
        model = City
        fields = '__all__'