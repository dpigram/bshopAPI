from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from baseAPI.serializers import AppointmentsSerializer, StylesSerializer, ShopSerializer, UserSerializer, GroupSerializer
from baseAPI.models import Shops, Styles, Appointments
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class ShopsViewSet(viewsets.ModelViewSet):
	queryset = Shops.objects.all()
	serializer_class = ShopSerializer

class StylesViewSet(viewsets.ModelViewSet):
	queryset = Styles.objects.all()
	serializer_class = StylesSerializer

class AppointmentsViewSet(viewsets.ModelViewSet):
	queryset = Appointments.objects.all()
	serializer_class = AppointmentsSerializer