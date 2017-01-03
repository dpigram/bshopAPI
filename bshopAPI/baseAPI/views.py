from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from baseAPI.serializers import BarberSerializer, AppointmentsSerializer, ProfilesSerializer, StylesSerializer, ShopSerializer, UserSerializer, GroupSerializer, FavoriteShopsSerializer
from baseAPI.models import Barber, Shops, Styles, Appointments, FavoriteShops, Profile
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
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

class FavoriteShopsViewSet(viewsets.ModelViewSet):
	queryset = FavoriteShops.objects.all()
	serializer_class = FavoriteShopsSerializer

class ProfilesViewSet(viewsets.ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfilesSerializer

class BarberViewSet(viewsets.ModelViewSet):
	queryset = Barber.objects.all()
	serializer_class = BarberSerializer

@api_view(['POST'])
def LoginViewSet(request):
	user = authenticate(username=request.POST['username'], password=request.POST['password'])
	serializer_context = {
		'request': request,
	}
	data = UserSerializer(instance=user, context=serializer_context)
	
	if user is not None:
		if user.is_active:
			return Response({'status': 'success', 'data': data.data})
		else:
			return Response({'status' : 'failure', 'message' : 'This account has been disabled'})
	else:
		# the authentication system was unable to verify the username and password
		return JsonResponse({'status': 'failure', 'message': 'The username and password were incorrect'})


@api_view(['POST'])
def barberAppointments(request):
	print(request.POST['barber_id'])
	appointments = Appointments.objects.filter(barber=request.POST['barber_id'])
	print(appointments)
	serializer_context = {
		'request': request,
	}

	data = AppointmentsSerializer(appointments, context=serializer_context, many=True)
	return JsonResponse({'data': data.data})

@api_view(['POST'])
def customerAppointments(request):
	appointments = Appointments.objects.filter(customer=request.POST['customer_id'])
	serializer_context = {'request': request,}
	data = AppointmentsSerializer(appointments, context=serializer_context, many=True)
	return JsonResponse({'data': data.data})



def getUserProfile(request, userid):
	profile = Profile.objects.get(owner=userid)
	serializer_context = {'request': request,}
	data = ProfilesSerializer(profile, context=serializer_context, many=False)
	return JsonResponse({'data': data.data})

@api_view(['POST'])
def getUserFavoriteShops(request, userid):
	favorites = FavoriteShops.objects.filter(owner=userid)
	serializer_context = {'request': request,}
	data = FavoriteShopsSerializer(favorites, context=serializer_context, many=True)

	if data is not None:
		return JsonResponse({'data': data.data})
	else:
		return Response({'data': ''})
	
