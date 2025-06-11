from django.http import JsonResponse

from .models import MesonetStations, WeatherConditions, BatteryData, SoilData
from decimal import Decimal
import json, os, datetime

station_limit = int(os.getenv("STATION_NUMBERS", "11"))

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
    'message': 'Limit should be within 1 and 2016, inclusive.',
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
    
def _validate_codes(code, limit, available_codes, interval=5):
    if interval and interval < 5 or not interval % 5 == 0:
        return JsonResponse(invalid_code_message, status=404)

    if limit <= 0 or limit > 2016:        
        return JsonResponse(out_of_search_limit_message, status=404)
    
    if len(code) > 1:
        print(code)
        for single_code in code:
            if not single_code in available_codes:
                return JsonResponse(invalid_code_message, status=404)
    elif code[0] != "all" and code[0] not in available_codes:
        return JsonResponse(invalid_code_message, status=404)
    else:
        return "VALID"
    
def _generate_response(object_model, code, limit, station_number, interval=5):
    if code[0] == "all":
        all_data = list(object_model.objects.filter(station_num=station_number).order_by("-timestamp").values())[:limit]
    else:
        all_data = list(object_model.objects.filter(station_num=station_number).order_by("-timestamp").values(*code))[:limit]

    result_data = []
    for index, data in enumerate(all_data):
        index_interval = interval / 5
        # print(all_data)
        if index % index_interval == 0:
            result_object = {}
            for key, value in data.items():
                result_object[key] = _convert_types(value)
            result_data.append(result_object)
    # print(result_data)
    return JsonResponse(result_data, safe=False, status=200)

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
                    "rv_tot_pre_accu", "rv_avg_pre_int_max", "rv_max_pre_int_max", "t109_30ft_f_avg", "t109_10ft_f_avg", "absbaro_inhg_avg", "sealvlbaro_inhg_avg", 
                    "heatindxtmpf_avg", "windchilltmpf_avg"}
    object_model = WeatherConditions

    # code and limit validation
    code = request.GET.get("code", "all").strip(",").split(",")
    limit = int(request.GET.get("limit", "1"))
    interval = int(request.GET.get("interval", "5")) # must be a multiple of 5; minimum 0
    response = _validate_codes(code, limit, available_codes, interval)
    if isinstance(response, JsonResponse):
        return response

    # actual response
    return _generate_response(object_model, code, limit, station_number, interval)
    
def get_battery_data(request, station_number):
    available_codes = {"station_num", "timestamp", "batteryvoltage", "batterycurrent", "loadcurrent", "chargeinputvoltage", "chargeinputcurrent", "chargetemp", 
                       "chg_state", "chg_source", "ck_batt"}
    object_model = BatteryData

    # code and limit validation
    code = request.GET.get("code", "all").strip(",").split(",")
    limit = int(request.GET.get("limit", "1"))
    interval = int(request.GET.get("interval", "5"))
    response = _validate_codes(code, limit, available_codes, interval)
    if isinstance(response, JsonResponse):
        return response
    
    # actual response
    return _generate_response(object_model, code, limit, station_number, interval)

def get_one_data_for_all_station(request, code):
    available_codes = {"airtf_avg", "max_airtf_avg", "min_airtf_avg","ws_30ft_mph_avg", "max_ws_30ft_mph_max", "dewptf", "rainsincemidnight"}
    # if code in available_codes:
    data = [0] * station_limit
    if code.split("_")[0] in ["max", "min"]:
        min_or_max = code.split("_")[0]
        code = "_".join(code.split("_")[1:])
        for i in range(0, station_limit):
            unclean_data = list(WeatherConditions.objects.filter(station_num=(i+1)).order_by("-timestamp").values(code, "station_num", "timestamp"))[:288]
            data[i] = [min(unclean_data, key=lambda x: x[code]) if min_or_max == "min" else max(unclean_data, key=lambda x: x[code])]
    else:
        for i in range(0, station_limit):
            data[i] = list(WeatherConditions.objects.filter(station_num=(i+1)).order_by("-timestamp").values(code, "station_num", "timestamp"))[:1]
    return JsonResponse(data, safe=False, status=200)

def get_soil_data(request, station_number):
    available_codes = {"station_num", "timestamp", "vwc_5cm_avg", "ka_5cm_avg", "soiltmpf_5cm_avg", "bulkec_5cm_avg", "vwc_10cm_avg", "ka_10cm_avg", "soiltmpf_10cm_avg", 
                       "bulkec_10cm_avg", "vwc_20cm_avg", "ka_20cm_avg", "soiltmpf_20cm_avg", "bulkec_20cm_avg", "vwc_30cm_avg", "ka_30cm_avg", "soiltmpf_30cm_avg", 
                       "bulkec_30cm_avg", "vwc_40cm_avg", "ka_40cm_avg", "soiltmpf_40cm_avg", "bulkec_40cm_avg", "vwc_50cm_avg", "ka_50cm_avg", "soiltmpf_50cm_avg", 
                       "bulkec_50cm_avg", "vwc_60cm_avg", "ka_60cm_avg", "soiltmpf_60cm_avg", "bulkec_60cm_avg", "vwc_75cm_avg", "ka_75cm_avg", "soiltmpf_75cm_avg", 
                       "bulkec_75cm_avg", "vwc_100cm_avg", "ka_100cm_avg", "soiltmpf_100cm_avg", "bulkec_100cm_avg"}
    object_model = SoilData

    # code and limit validation
    code = request.GET.get("code", "all").strip(",").split(",")
    limit = int(request.GET.get("limit", "1"))
    interval = int(request.GET.get("interval", "5"))
    response = _validate_codes(code, limit, available_codes, interval)
    if isinstance(response, JsonResponse):
        return response
    
    # actual response
    return _generate_response(object_model, code, limit, station_number, interval)

    available_codes = {"station_num", "timestamp", }
    object_model = TemperaturePressure

    # code and limit validation
    code = request.GET.get("code", "all").strip(",").split(",")
    limit = int(request.GET.get("limit", "1"))
    interval = int(request.GET.get("interval", "5"))
    response = _validate_codes(code, limit, available_codes, interval)
    if isinstance(response, JsonResponse):
        return response
    
    # actual response
    return _generate_response(object_model, code, limit, station_number, interval)
    
    # # validating api name
    # available_api = {"get_weather_condition", "get_battery_data"}
    # if api_name not in available_api:
    #     return JsonResponse(api_not_available_message, status=404)

    # # setting available codes and object model
    # available_codes = None
    # object_model = None
    # if api_name == "get_weather_condition":
    #     available_codes = {"station_num", "timestamp", "record", "battv_avg", "ws_30ft_mph_avg", "ws_30ft_mph_max", "winddir_30ft_d1_wvt", "winddir_30ft_sd1_wvt", 
    #                 "ws_10ft_mph_avg", "ws_10ft_mph_max", "winddir_10ft_d1_wvt", "winddir_10ft_sd1_wvt", "ws_sonic_mph_avg", "ws_sonic_mph_max", "winddir_sonic_d1_wvt", 
    #                 "winddir_sonic_sd1_wvt", "airtf_avg", "rh_avg", "slrw_avg", "slrmj_tot", "dewptf", "rainsincemidnight", "rv_pre_accu_tot", "rv_tips_tot", 
    #                 "rv_tot_pre_accu", "rv_avg_pre_int_max", "rv_max_pre_int_max"}
    #     object_model = WeatherConditions
    # elif api_name == "get_battery_data":
    #     available_codes = {"station_num", "timestamp", "batteryvoltage", "batterycurrent", "loadcurrent", "chargeinputvoltage", "chargeinputcurrent", "chargetemp", 
    #                     "chg_state", "chg_source", "ck_batt"}
    #     object_model = BatteryData
    
    # # code and limit validation
    # code = request.GET.get("code", "all")
    # limit = int(request.GET.get("limit", "1"))
    # response = _validate_codes(code, limit, available_codes)
    # if isinstance(response, JsonResponse):
    #     return response
    
    # # actual response
    # if code == "all":
    #     all_data = list(object_model.objects.filter(station_num=station_number).order_by("timestamp").values())[:limit]
    # else:
    #     all_data = list(object_model.objects.filter(station_num=station_number).order_by("timestamp").values())[:limit]
    # for data in all_data:
    #     for key, value in data.items():
    #         data[key] = _convert_types(value)
    # return JsonResponse(all_data, safe=False, status=200)




