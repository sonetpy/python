# https://api.sunrise-sunset.org/json.
"""
API documentation
Ours is a very simple REST api, you only have to do a GET request to https://api.sunrise-sunset.org/json.

Parameters
lat (float): Latitude in decimal degrees. Required.
lng (float): Longitude in decimal degrees. Required.
date (string): Date in YYYY-MM-DD format. Also accepts other date formats and even relative date formats. If not present, date defaults to current date. Optional.
callback (string): Callback function name for JSON response. Optional.
formatted (integer): 0 or 1 (1 is default). Time values in response will be expressed following ISO 8601 and day_length will be expressed in seconds. Optional.
"""
import json
from datetime import datetime

import requests

# Taking Longitude and latitude of London using below URL
# https://latlong.net/

MY_LAT=51.507351
MY_LNG=-0.127758
DATE=datetime.now()
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
print(response.json())
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print("Sunrise:", sunrise)
print("Sunset:", sunset)
print("Sunrise:", sunrise.split("T")[1].strip("+"), "\n")
print("Sunset:", sunset.split("T")[1].split(":")[0], "\n")
pretty_data = json.dumps(response.json(), indent=4)
pretty_data = json.dumps(data, indent=4)
print(pretty_data)