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
	# price = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=True);

	def __str__(self):
		return self.name


class Appointments(models.Model):
	date = models.DateTimeField()
	customer = models.ForeignKey(User, related_name="customer_appointment")
	style = models.OneToOneField('Styles')
	barber = models.ForeignKey(User, related_name="barber_appointment")

class Profile(models.Model):
	firstName = models.CharField(max_length=100, default=None)
	lastName = models.CharField(max_length=100, default=None)
	middleName = models.CharField(max_length=100, default=None, null=True)
	nickName = models.CharField(max_length=100, default=None, null=True)
	bio = models.TextField(max_length=100, default=None, null=True)
	owner = models.ForeignKey(User)

class Photos(models.Model):
	caption = models.TextField(default=None)
	owner = models.ForeignKey(User)
	daps = models.IntegerField(default=0)

class Comments(models.Model):
	text = models.TextField(default=None)
	timeStamp = models.DateTimeField(auto_now_add=True)
	daps = models.IntegerField(default=0)
	owner = models.ForeignKey(User)

class Albums(models.Model):
	title = models.TextField(max_length=100, default="Unknown Album")
	timeStamp = models.DateTimeField(auto_now_add=True)
	daps = models.IntegerField(default=0)










