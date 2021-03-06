from django.db import models

class Category(models.Model):
	name = models.CharField(max_length = 255)

	def __str__(self):
		return self.name

class Event(models.Model):
	name = models.CharField(max_length = 255)
	description = models.CharField(max_length = 500)
	host = models.CharField(max_length = 255)
	date = models.DateTimeField()
	location = models.CharField(max_length = 255)
	address = models.CharField(max_length = 255)
	startTime = models.DateTimeField()
	endTime = models.DateTimeField()
	cost = models.FloatField()
	eventLink = models.CharField(max_length = 255)
	category = models.ForeignKey(
		Category,
		on_delete=models.DO_NOTHING,
	)
	source = models.CharField(max_length = 255)

	def __str__(self):
		return self.name
