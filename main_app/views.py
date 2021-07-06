from django.shortcuts import render, redirect

from .models import *
from .forms import *
# Create your views here.


from django.views.generic.edit import CreateView, UpdateView, DeleteView


# class CityCreate(CreateView):
#   model = City
#   fields = '__all__'

class CityUpdate(UpdateView):
  model = City
  fields = ['fav_spot', 'fav_local_food', 'days_spent']

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
    return render(request, 'cities/detail.html', { 'city': city })



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


