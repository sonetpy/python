import requests
import json
import urllib
print('City Name should be in iata format like Mumbai: BOM, Delhi: DEL')
dep_iata=input('Departure City: ')
arr_iata=input('Arrival City: ')
ele=[]
params = {
    'access_key': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiY2IyMDA5ODBlNTlmOTVmNTA4YzU0MzM5NDYwZTdjZjJiNjM1ODZkYWNlZDAxYzFmOTJhY2U3YmVlZmFhMmJiMTliYmVjNjc3YTQzY2Y1MzciLCJpYXQiOjE2NTMyODQyNDQsIm5iZiI6MTY1MzI4NDI0NCwiZXhwIjoxNjg0ODIwMjQ0LCJzdWIiOiI0OTg0Iiwic2NvcGVzIjpbXX0.AjQorLAsINjaeozE9XNlf6FdCqqhpQ3i5hRVZBAtG__2v1cpRXa8IMzdDXUOh0S_hUyidq2J7165Awxn82RlUQ'
    ,'flight_status': 'active'
    ,'dep_iata': dep_iata
    ,'arr_iata': arr_iata
}
response = requests.get('https://app.goflightlabs.com/flights',params)
json_response = response.json()
#jet = json.loads(json_response)
#json.loads take a string as input and returns a dictionary as output.
#json.dumps take a dictionary as input and returns a string as output.
data = json.dumps(response.json())
data_loads = json.loads(data)

for i in range(len(data_loads)):
    print(data_loads[i]['flight']['iata'])
