from django.db import models

# Create your models here.

class Stud(models.Model):
	fname=models.CharField(max_length=30)
	marks=models.IntegerField()

	def __str__(self):
		return (' Name=%s'%(self.fname))