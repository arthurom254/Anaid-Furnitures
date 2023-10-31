
from administrator.models import City, Station, Country
from  django.http import JsonResponse
from django.contrib import messages
def get_city(request, id):
    city=City.objects.filter(country=Country(id=id)).values('id', 'name')
    city=list(city)
    return JsonResponse(city, safe=False)

def get_station(request, id):
    station=Station.objects.filter(city=City(id=id)).values('id', 'name')
    station=list(station)
    return JsonResponse(station, safe=False)