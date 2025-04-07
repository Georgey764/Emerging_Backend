from django.urls import path

from . import views

urlpatterns = [
    path("get_stations_data", views.get_stations_data, name="get stations data"),
    path("get_weather_condition/<int:station_number>", views.get_weather_condition, name="get weather condition"),
    path("get_battery_data/<int:station_number>", views.get_battery_data, name="get battery data"),
    path("get_one_data_for_all_station/<str:code>", views.get_one_data_for_all_station, name="get one data for all station")
]