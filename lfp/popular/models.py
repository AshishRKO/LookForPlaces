from django.db import models

# Create your models here.

class Places(models.Model):
	name=models.CharField(max_length=200)
	description=models.TextField(max_length=5000)

	def __unicode__(self): #__str__ in python3
		return self.name

class DetailPlaces(models.Model):
	
	name=models.CharField(max_length=200)
	description=models.TextField(max_length=5000)
	image1=models.ImageField(upload_to = 'detailplaces',default='none')
	image2=models.ImageField(upload_to = 'detailplaces',default='none')
	image3=models.ImageField(upload_to = 'detailplaces',default='none')
	image4=models.ImageField(upload_to = 'detailplaces',default='none')
	image5=models.ImageField(upload_to = 'detailplaces',default='none')
	image6=models.ImageField(upload_to = 'detailplaces',default='none')
	image7=models.ImageField(upload_to = 'detailplaces',default='none')
	image8=models.ImageField(upload_to = 'detailplaces',default='none')
	route=models.CharField(max_length=500)

	def __unicode__(self): #__str__ in python3
		return self.name

		