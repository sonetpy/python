import json
import requests
# Trent Bridge Weather report
"""
MY_LAT = 52.716129
MY_LON = -1.345700
MY_KEY = "3841a915236de71bd0a04b6380b1d45f"
"""
# Patna Weather report

MY_LAT = 25.594095
MY_LON = 85.137566
MY_KEY = "3841a915236de71bd0a04b6380b1d45f"

# https://openweathermap.org/api/one-call-api
parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": MY_KEY,
    "exclude": "current,minutely,daily" # I have added this as per API doc because I want to exclude some data.
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status() # Raise a response if we get an error
#pretty_data = json.dumps(response.json(), indent=4)
#print(pretty_data)
# print(response.json())
# hourly.rain from API doc
#weather_data = response.json()['hourly'][5]['weather'][0] # Got data only for hourly so that I can run FOR loop
#print(json.dumps(weather_data, indent=4))

index = 0
for i in range(0, 23):
    id = response.json()['hourly'][i]['weather'][0]['id']
    # Full list of weather code like snow, rain, thunderstor .. etc
    # https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
    if id < 700:
        print ("High chance of Rain in next {}Hrs at Latitude {} and Longitude {}, better take an umbrella".format(i, MY_LAT, MY_LON))
        weather_data = response.json()['hourly'][i]['weather'][0]  # Got data only for hourly so that I can run FOR loop
        print(json.dumps(weather_data, indent=4))
        break

else:
    print("Sky is clear it will not rain in next 24 Hrs")




