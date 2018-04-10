from django.db import models

# Create your models here.
class RestaurantLocation(models.Model):
	"""contains the information of the location of each restaurants"""
	name = models.CharField(max_length=120)
	location = models.CharField(max_length=200, blank=True, null=True)

class OrderLocation(models.Model):
	"""to  find the foreign key relationship"""
	addedon = models.DateField(auto_now = True)
	location = models.ForeignKey('RestaurantLocation', on_delete = models.CASCADE)