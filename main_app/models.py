from django.db import models

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

# cities = [
#   City('Tuscany', 'Italy','Antinori winery', 'burrata', 15),
#   City('Galway', 'Ireland','Busker Brownes', 'soda bread', 7),
#   City('New York', 'USA', 'Stone Street', 'pretzel', 15)
# ]

   # def __init__(self, name, country, fav_spot, fav_local_food, days_spent):
    #     self.name = name
    #     self.country = country
    #     self.fav_spot = fav_spot
    #     self.fav_local_food = fav_local_food
    #     self.days_spent = days_spent