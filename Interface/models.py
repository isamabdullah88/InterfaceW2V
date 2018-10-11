from django.db import models

# Create your models here.
class Word(models.Model):
	words = models.CharField(max_length=150)

	def __str__(self):
		return self.words

class Image(models.Model):
	file_name = models.CharField(max_length=200, default='')
	image = models.CharField(max_length=200, default='')

	def __str__(self):
		return self.image