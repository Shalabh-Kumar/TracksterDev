from django.db import models

class Post(models.Model):
	highTemp = models.CharField(max_length = 140)
	lowTemp = models.CharField(max_length = 140)
	date =models.DateTimeField()

	def __str__(self):
		return self.highTemp