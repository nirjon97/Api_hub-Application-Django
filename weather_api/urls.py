from django import views
from django.urls import path
from .views import CityWeatherView,City_delete

urlpatterns = [
        path('weather_view/', CityWeatherView,name='city_weather'),
        path('remove/<city_name>/',City_delete, name='city_remove')

    ]