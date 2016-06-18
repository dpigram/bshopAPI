from django.contrib.auth.models import User, Group
from baseAPI.models import Shops, Styles, Appointments
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class ShopSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Shops
		field = ('name', 'address')

class StylesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Styles
		field = ('name')

class AppointmentsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Appointments
		field = ('date', 'customer', 'style')


