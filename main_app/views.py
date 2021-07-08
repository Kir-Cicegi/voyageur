from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import *
from .forms import *


def home (request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')



def city_list(request):
    cities = City.objects.all()
    return render(request, 'cities/index.html', { 'cities': cities })

def detail(request, city_id):
    city = City.objects.get(id=city_id)
    spots = city.attractions_set.all()
    spots_form = AttractionForm()
    unpicked_airlines = Airline.objects.exclude(id__in = city.airlines.all().values_list('id'))
    return render(request, 'cities/detail.html', { 'city': city, 'spots_form': spots_form, 'spots': spots, 'airlines':unpicked_airlines })



def new_form (request): 
    if request.method == 'POST':
        print("I have received form data")
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/cities/')
    else: 
        form = CityForm()
        return render(request, 'cities/form.html', {'form': form})

class CityUpdate(UpdateView):
  model = City
  fields = ['country','fav_spot', 'fav_local_food', 'days_spent']

class CityDelete(DeleteView):
  model = City
  success_url = '/cities/'


def add_spot(request, city_id):
  form = AttractionForm(request.POST)
  if form.is_valid():
    new_spot = form.save(commit=False)
    new_spot.city_id = city_id
    new_spot.save()
    
  return redirect('detail', city_id=city_id)


class AirlineList(ListView):
  model = Airline

class AirlineDetail(DetailView):
  model = Airline

class AirlineCreate(CreateView):
  model = Airline
  fields = '__all__'
  success_url = '/airlines/'


def assoc_airline(request, city_id, airline_id):
  City.objects.get(id=city_id).airlines.add(airline_id)
  return redirect('detail', city_id=city_id)

def unassoc_airline(request, city_id, airline_id):
  City.objects.get(id=city_id).airlines.remove(airline_id)
  return redirect('detail', city_id=city_id)

