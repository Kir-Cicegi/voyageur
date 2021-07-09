from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
import boto3
from .models import *
from .forms import *


def home (request):
    return render(request, 'index.html')

@login_required
def profile(request):
    cities = request.user.city_set.all()
    name = request.user.username
    return render(request, 'profile.html', { 'cities': cities, 'name':name })


@login_required
def city_list(request):
    cities = City.objects.all()
    
    return render(request, 'cities/index.html', { 'cities': cities })

@login_required
def detail(request, city_id):
    city = City.objects.get(id=city_id)
    spots = city.attractions_set.all()
    spots_form = AttractionForm()
    unpicked_airlines = Airline.objects.exclude(id__in = city.airlines.all().values_list('id'))
    return render(request, 'cities/detail.html', { 'city': city, 'spots_form': spots_form, 'spots': spots, 'airlines':unpicked_airlines })


# new city does not get generated!
@login_required
def new_form (request): 
    if request.method == 'POST':
        print("I have received form data")
        form = CityForm(request.POST)
        print(request.POST)
        if form.is_valid():
            # user=form.cleaned_data['user']
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            print(instance)
        return redirect('/cities/')
    else: 
        form = CityForm()
        return render(request, 'cities/form.html', {'form': form})

class CityUpdate(LoginRequiredMixin, UpdateView):
  model = City
  fields = ['country','fav_spot', 'fav_local_food', 'days_spent']

class CityDelete(LoginRequiredMixin, DeleteView):
  model = City
  success_url = '/cities/'


def add_spot(request, city_id):
  form = AttractionForm(request.POST)
  if form.is_valid():
    new_spot = form.save(commit=False)
    new_spot.city_id = city_id
    new_spot.save()
    
  return redirect('detail', city_id=city_id)


class AirlineList(LoginRequiredMixin, ListView):
  model = Airline


class AirlineDetail(LoginRequiredMixin, DetailView):
  model = Airline


class AirlineCreate(LoginRequiredMixin, CreateView):
  model = Airline
  fields = '__all__'
  success_url = '/airlines/'


def assoc_airline(request, city_id, airline_id):
  City.objects.get(id=city_id).airlines.add(airline_id)
  return redirect('detail', city_id=city_id)

def unassoc_airline(request, city_id, airline_id):
  City.objects.get(id=city_id).airlines.remove(airline_id)
  return redirect('detail', city_id=city_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)