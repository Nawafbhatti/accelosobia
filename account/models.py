from django.db import models

# Create your models here.

class CONTACT(models.Model):

	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	note = models.TextField()

	def __str__(self):
	    return self.name

class CAREER_DATA(models.Model):

	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	note = models.TextField()

	def __str__(self):
	    return self.name