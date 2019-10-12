import requests
from django.shortcuts import render
from .models import City
from .form import CityForm

def index(request):
	appid = '5365b6926de23a219f853729e7d56c9a'
	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+appid

	if(request.method == 'POST'):
		form = CityForm(request.POST)
		form.save()
	form = CityForm()

	cities = City.objects.all()

	all_cities = []

	for city in cities:

		res = requests.get(url.format(city.name)).json()

		city_info = {
			'city': city.name,
			'temp': res["main"]["temp"],
			'icon': res["weather"][0]["icon"]
		}
		all_cities.append(city_info)
	
	context = {'all_info':all_cities, 'form':form}

	return render(request, 'weather/index.html', context)