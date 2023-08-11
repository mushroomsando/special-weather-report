import requests

"""
In order to inquire about the special report issued in the area based on the special report area code, 
the function of inquiry of branch number, announcement time (date), announcement number (monthly), announcement area code, 
zone name, special report strength, effective time, release time, total cancellation, cancellation time

Power by Korea Meteorological Administration
Copyright (C) 2023 Mushroomsando. All right reserved.
"""

# basics
key = open("api_key.txt", "r")

url = 'http://apis.data.go.kr/1360000/WthrWrnInfoService/getPwnCd'
params ={'serviceKey' : key.read(), # Essential, Your API KEY
         'pageNo' : '1', # Essential, Page Number
         'numOfRows' : '10', # Essential, Number of results per page
         'dataType' : 'JSON', # Option, Defalt : XML, Data type (XML or JSON)
         'fromTmFc' : '', # Option, Time (YYYYMMDD), Current date if not entered
         'toTmFc' : '', # Option, Time (YYYYMMDD), Current date if not entered
         'areaCode' : 'L1080100', # Option, areaCode
         'warningType' : '', # Option, 1-strong wind, 2-rain, 3-cold wave, 4-dry, 5-storm tidal wave, 6-wind, 7-tropical wind, 8-snow, 9-yellow sand, 12-heat wave
         'stnId' : '108' # Essential, Branch code
         }

response = requests.get(url, params=params)
print(response.content)