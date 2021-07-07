from django.shortcuts import render, redirect

from .models import *
from .forms import *
# Create your views here.


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


# class CityCreate(CreateView):
#   model = City
#   fields = '__all__'

class CityUpdate(UpdateView):
  model = City
  fields = ['country','fav_spot', 'fav_local_food', 'days_spent']

class CityDelete(DeleteView):
  model = City
  success_url = '/cities/'


def home (request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')



def city_list(request):
    # City.objects.create(name="Tuscany", country="Italy", fav_spot="Antinori Winery", fav_local_food="Burrata", days_spent=15)
    cities = City.objects.all()
   
   
    return render(request, 'cities/index.html', { 'cities': cities })

def detail(request, city_id):
    city = City.objects.get(id=city_id)
    spots = Attractions.objects.all
    spots_form = AttractionForm()
    return render(request, 'cities/detail.html', { 'city': city, 'spots_form': spots_form, 'spots': spots })



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



def add_spot(request, city_id):
	# create the ModelForm using the data in request.POST
  form = AttractionForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_spot = form.save(commit=False)
    new_spot.city_id = city_id
    new_spot.save()
    
  return redirect('detail', city_id=city_id)