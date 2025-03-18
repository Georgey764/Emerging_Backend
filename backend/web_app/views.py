from django.http import JsonResponse

from .models import MesonetStations, WeatherConditions, BatteryData
from decimal import Decimal
import json, os, datetime

station_limit = int(os.getenv("STATION_NUMBERS", "9"))

invalid_code_message = {
    "message": "Invalid code",
    "status": "404"
}
station_not_found_message = {
    "message":"Station doesn't exist",
    "status": "Not Found."
}
not_found_message = {
    "message":"404 not found",
    "status": "Not Found."
}
out_of_search_limit_message = {
    'message': 'Limit should be within 1 and 100, inclusive.',
    'status': 'Not found'
}
api_not_available_message = {
    'message': 'Api not available.',
    'status': 'Not found'
}

def _convert_types(data):
    if isinstance(data, Decimal):
        return float(data)
    if isinstance(data, datetime.date):
        return data.strftime("%Y-%m-%d %H:%M:%S")
    else:
        return data
    
def _validate_codes(code, limit, available_codes):
    if limit <= 0 or limit > 100:        
        return JsonResponse(out_of_search_limit_message, status=404)
    if "," in code:
        code = tuple(code.split(","))
        for single_code in code:
            if not single_code in available_codes:
                return JsonResponse(invalid_code_message, status=404)
    elif code != "all" and code not in available_codes:
        return JsonResponse(invalid_code_message, status=404)
    else:
        return "VALID"
    
def _generate_response(object_model, code, limit, station_number):
    if code == "all":
        all_data = list(object_model.objects.filter(station_num=station_number).order_by("timestamp").values())[:limit]
    else:
        all_data = list(object_model.objects.filter(station_num=station_number).order_by("timestamp").values())[:limit]
    for data in all_data:
        for key, value in data.items():
            data[key] = _convert_types(value)
    return JsonResponse(all_data, safe=False, status=200)

def get_stations_data(request):
    station_number_str = request.GET.get('station_number', 'all')

    if station_number_str == "all":
        stations_list = MesonetStations.objects.all().values()
        for station in stations_list:
            for key, value in station.items():
                station[key] = _convert_types(value)
        return JsonResponse(list(stations_list), safe=False, status=200)
    
    station_number = int(station_number_str)
    # validating limit
    if station_number <= 0 or station_number > station_limit:
        return JsonResponse(station_not_found_message, status=404)
    # response for individual stations
    station_data = list(MesonetStations.objects.filter(station_number=station_number).values())[0]
    for key, value in station_data.items():
        station_data[key] = _convert_types(value)
    return JsonResponse(station_data, safe=False, status=200)

def get_weather_condition(request, station_number):
    available_codes = {"station_num", "timestamp", "record", "battv_avg", "ws_30ft_mph_avg", "ws_30ft_mph_max", "winddir_30ft_d1_wvt", "winddir_30ft_sd1_wvt", 
                    "ws_10ft_mph_avg", "ws_10ft_mph_max", "winddir_10ft_d1_wvt", "winddir_10ft_sd1_wvt", "ws_sonic_mph_avg", "ws_sonic_mph_max", "winddir_sonic_d1_wvt", 
                    "winddir_sonic_sd1_wvt", "airtf_avg", "rh_avg", "slrw_avg", "slrmj_tot", "dewptf", "rainsincemidnight", "rv_pre_accu_tot", "rv_tips_tot", 
                    "rv_tot_pre_accu", "rv_avg_pre_int_max", "rv_max_pre_int_max"}
    object_model = WeatherConditions

    # code and limit validation
    code = request.GET.get("code", "all")
    limit = int(request.GET.get("limit", "1"))
    response = _validate_codes(code, limit, available_codes)
    if isinstance(response, JsonResponse):
        return response

    # actual response
    return _generate_response(object_model, code, limit, station_number)
    
def get_battery_data(request, station_number):
    available_codes = {"station_num", "timestamp", "batteryvoltage", "batterycurrent", "loadcurrent", "chargeinputvoltage", "chargeinputcurrent", "chargetemp", 
                       "chg_state", "chg_source", "ck_batt"}
    object_model = BatteryData

    # code and limit validation
    code = request.GET.get("code", "all")
    limit = int(request.GET.get("limit", "1"))
    response = _validate_codes(code, limit, available_codes)
    if isinstance(response, JsonResponse):
        return response
    
    # actual response
    return _generate_response(object_model, code, limit, station_number)
    # validating api name
    available_api = {"get_weather_condition", "get_battery_data"}
    if api_name not in available_api:
        return JsonResponse(api_not_available_message, status=404)

    # setting available codes and object model
    available_codes = None
    object_model = None
    if api_name == "get_weather_condition":
        available_codes = {"station_num", "timestamp", "record", "battv_avg", "ws_30ft_mph_avg", "ws_30ft_mph_max", "winddir_30ft_d1_wvt", "winddir_30ft_sd1_wvt", 
                    "ws_10ft_mph_avg", "ws_10ft_mph_max", "winddir_10ft_d1_wvt", "winddir_10ft_sd1_wvt", "ws_sonic_mph_avg", "ws_sonic_mph_max", "winddir_sonic_d1_wvt", 
                    "winddir_sonic_sd1_wvt", "airtf_avg", "rh_avg", "slrw_avg", "slrmj_tot", "dewptf", "rainsincemidnight", "rv_pre_accu_tot", "rv_tips_tot", 
                    "rv_tot_pre_accu", "rv_avg_pre_int_max", "rv_max_pre_int_max"}
        object_model = WeatherConditions
    elif api_name == "get_battery_data":
        available_codes = {"station_num", "timestamp", "batteryvoltage", "batterycurrent", "loadcurrent", "chargeinputvoltage", "chargeinputcurrent", "chargetemp", 
                        "chg_state", "chg_source", "ck_batt"}
        object_model = BatteryData
    
    # code and limit validation
    code = request.GET.get("code", "all")
    limit = int(request.GET.get("limit", "1"))
    response = _validate_codes(code, limit, available_codes)
    if isinstance(response, JsonResponse):
        return response
    
    # actual response
    if code == "all":
        all_data = list(object_model.objects.filter(station_num=station_number).order_by("timestamp").values())[:limit]
    else:
        all_data = list(object_model.objects.filter(station_num=station_number).order_by("timestamp").values())[:limit]
    for data in all_data:
        for key, value in data.items():
            data[key] = _convert_types(value)
    return JsonResponse(all_data, safe=False, status=200)




