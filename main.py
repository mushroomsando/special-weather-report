import requests
import json

"""
In order to inquire about the special report issued in the area based on the special report area code, 
the function of inquiry of branch number, announcement time (date), announcement number (monthly), announcement area code, 
zone name, special report strength, effective time, release time, total cancellation, cancellation time

Power by Korea Meteorological Administration
Copyright (C) 2023 Mushroomsando. All right reserved.
"""
with open('alret_info.json', 'r', encoding='utf-8') as json_file:
    reference_data = json.load(json_file)

def get_raw_data(service_key, areacode, branchCod, warningType = '', fromTime = '', toTime = ''):
    url = 'http://apis.data.go.kr/1360000/WthrWrnInfoService/getPwnCd'
    params ={'serviceKey' : service_key, # Essential, Your API KEY
            'pageNo' : '1', # Essential, Page Number
            'numOfRows' : '10', # Essential, Number of results per page
            'dataType' : 'JSON', # Option, Defalt : XML, Data type (XML or JSON)
            'fromTmFc' : fromTime, # Option, Time (YYYYMMDD), Current date if not entered
            'toTmFc' : toTime, # Option, Time (YYYYMMDD), Current date if not entered
            'areaCode' : areacode, # Option, areaCode
            'warningType' : warningType, # Option, 1-strong wind, 2-rain, 3-cold wave, 4-dry, 5-storm tidal wave, 6-wind, 7-tropical wind, 8-snow, 9-yellow sand, 12-heat wave
            'stnId' : branchCod # Essential, Branch code
            }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if data["response"]["header"]["resultCode"] == "03":
        raise ValueError("해당지역에 내려진 가상특보 데이터가 없습니다.")
    else:
        return data

def extract_weather_info(raw_data):
    data = []

    for item in raw_data["response"]["body"]["items"]["item"]:
        forecast_time = item["tmFc"]
        area_name = item["areaName"]
        warn_value = item["warnVar"]
        warn_stress = item["warnStress"]
        command = item["command"]
        start_time = item["startTime"]
        end_time = item["endTime"]
        is_cancel = item["cancel"]

        warn_var_name = reference_data["warnVar"][str(warn_value)]
        warn_stress_name = reference_data["warnStress"][str(warn_stress)]
        command_name = reference_data["command"][str(command)]
    
        data_item = {
            "forecast_time": forecast_time,
            "area_name": area_name,
            "warn_value": warn_var_name,
            "warn_stress": warn_stress_name,
            "command_name": command_name, 
            "start_time": start_time,
            "end_time": end_time,
            "is_cancel": is_cancel
        }

        data.append(data_item)

    return data

raw = get_raw_data(open("api_key.txt", "r"), "L1080100", "108",fromTime="20230810",toTime="20230813")
print(extract_weather_info(raw))