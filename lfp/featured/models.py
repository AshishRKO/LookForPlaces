from django.db import models

# Create your models here.

class Feature(models.Model):
	name=models.CharField(max_length=200)
	description=models.TextField(max_length=5000)

	def __unicode__(self): #__str__ in python3
		return self.name

class DetailFeature(models.Model):
	name=models.CharField(max_length=200)
	description=models.TextField(max_length=5000)
	route=models.CharField(max_length=500)

	def __unicode__(self): #__str__ in python3
		return self.name

