from django.contrib.auth.models import User, Group
from baseAPI.models import Barber, Profile, Shops, Styles, Appointments, FavoriteShops
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('url','id', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class ShopSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Shops
		fields = ('name', 'address', 'owner')

class StylesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Styles
		fields = ('name',)

class AppointmentsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Appointments
		fields = ('date', 'customer', 'style', 'barber')

class FavoriteShopsSerializer(serializers.ModelSerializer):
	class Meta:
		model = FavoriteShops
		fields = ('url', 'owner', 'shop', )

class ProfilesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ('url', 'firstName', 'lastName', 'middleName', 'nickName', 'bio', 'owner', 'favoriteShops')
		
class BarberSerializer(serializers.ModelSerializer):
	class Meta:
		model = Barber
		fields = ('url', 'firstName', 'lastName', 'middleName', 'nickName', 'user')

