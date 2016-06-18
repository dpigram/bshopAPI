from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Shops(models.Model):
	name = models.CharField(max_length=100, default=None)
	address = models.CharField(max_length=100, default=None)
	owner = models.ForeignKey(User)

class Styles(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Appointments(models.Model):
	date = models.DateTimeField()
	customer = models.ForeignKey(User, related_name="customer_appointment")
	style = models.OneToOneField('Styles')
	barber = models.ForeignKey(User, related_name="barber_appointment")




