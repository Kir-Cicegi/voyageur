from django.db import models
from django.urls import reverse



# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    fav_spot = models.CharField(max_length=200)
    fav_local_food = models.CharField(max_length=200)
    days_spent = models.IntegerField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

 

    # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'city_id': self.id})

 

# Tourist Attractions that you visited & when
class Attractions(models.Model):
  date = models.DateField()
  attraction = models.CharField(max_length=200)

  city = models.ForeignKey(City, on_delete=models.CASCADE)

  def __str__(self):
    return f"Visited {self.attraction} on {self.date}"