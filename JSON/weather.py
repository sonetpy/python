import json
import requests
MY_LAT = 33.44
MY_LON = -94.04
MY_KEY = "3841a915236de71bd0a04b6380b1d45f"
parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": MY_KEY
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
pretty_data = json.dumps(response.json(), indent=4)
print(pretty_data)