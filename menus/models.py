from django.db import models

# Create your models here.

class Menu(models.Model):
	restaurant = models.CharField(max_length=200)
	location = models.CharField(max_length=500)
	phone = models.CharField(max_length=20)
	def __unicode__(self):
		return self.restaurant

class MenuItem(models.Model):
	order_id = models.CharField(max_length=10)
	name = models.CharField(max_length=500)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	category = models.CharField(max_length=200)
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(default=0)
	menu = models.ForeignKey(Menu)
	def __unicode__(self):
		return self.name
