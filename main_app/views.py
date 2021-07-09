from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
import boto3
import uuid
from .models import *
from .forms import *

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'voyageurbucket'


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


def add_photo(request, city_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
         
            photo = Photo(url=url, city_id=city_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', city_id=city_id)