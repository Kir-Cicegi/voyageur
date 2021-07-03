from django.db import models

# Create your models here.
class City:
  def __init__(self, name, country, fav_spot, fav_local_food, days_spent):
    self.name = name
    self.country = country
    self.fav_spot = fav_spot
    self.fav_local_food = fav_local_food
    self.days_spent = days_spent


cities = [
  City('Tuscany', 'Italy','Antinori winery', 'burrata', 15),
  City('Galway', 'Ireland','Busker Brownes', 'soda bread', 7),
  City('New York', 'USA', 'Stone Street', 'pretzel', 15)
]