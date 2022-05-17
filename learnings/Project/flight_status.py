import requests
import json
import urllib
#city=input('Enter a City name: ')
#extra=input('Enter URL cities/route/flights')
print('City Name should be in iata format like Mumbai: BOM, Delhi: DEL')
dep_iata=input('Departure City: ')
arr_iata=input('Arrival City: ')
params = {
    'access_key': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiM2Q4NzEyNzU4YjM1YTk2NjQyMDE4YjY0Y2YxMDdlMTNkZWQxYjQwNzIyNGVmMGM2MTE2Y2JkZGIwODQxY2NmNjRiYzM4ZGViNzM1MmFmNmIiLCJpYXQiOjE2NTI2MTUxNTAsIm5iZiI6MTY1MjYxNTE1MCwiZXhwIjoxNjg0MTUxMTUwLCJzdWIiOiI0NjE0Iiwic2NvcGVzIjpbXX0.FkmGff6gCWf-9wKa5OOyppzdu238I9x8XH_Y3CG1HGorU-WW4QSevHf1kHGVVUt9izDFH8xK_uaO9OxMozT0Tg'
    ,'flight_status': 'active'
    ,'dep_iata': dep_iata
    ,'arr_iata': arr_iata
}
api_result = requests.get('https://app.goflightlabs.com/flights',params)

data = api_result.json()
print(json.dumps(data, indent=4))
json_str = json.dumps(data)