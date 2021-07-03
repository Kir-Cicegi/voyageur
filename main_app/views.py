from django.shortcuts import render, redirect

from .models import *
from .forms import *
# Create your views here.

def home (request):
    return render(request, 'index.html', {'cities': cities})

def about(request):
    return render(request, 'about.html')



def city_list(request):
    return render(request, 'cities/index.html', { 'cities': cities })