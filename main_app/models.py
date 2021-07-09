from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


RATE = (
    ('A', '$'),
    ('B', '$$'),
    ('C', '$$$'),
    ('D', '$$$$'),
    ('E', '$$$$$')
)

#fix how the rating shows up
class Airline(models.Model):
    airline = models.CharField(max_length= 50)
    rating = models.CharField(
        max_length=1,
        choices=RATE,
        default=RATE[0][0]
    )

    def __str__(self):
        return f"{self.airline} ~ (Rating:{self.get_rating_display()})"

    def get_absolute_url(self):
        return reverse('city_detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['-rating']


class City(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    fav_spot = models.CharField(max_length=200)
    fav_local_food = models.CharField(max_length=200)
    days_spent = models.IntegerField(max_length=200)
    airlines = models.ManyToManyField(Airline)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'city_id': self.id})


class Attractions(models.Model):
  date = models.DateField()
  attraction = models.CharField(max_length=200)

  city = models.ForeignKey(City, on_delete=models.CASCADE)

  def __str__(self):
    return f"Visited {self.attraction} on {self.date}"