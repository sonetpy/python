import urllib.request  # Built-in module for making requests
import json

print('City Name should be in iata format like Mumbai: BOM, Delhi: DEL')
dep_iata = input('Departure City: ')
arr_iata = input('Arrival City: ')

params = {
    'access_key': 'your_access_key',  # Replace with your actual access key
    'flight_status': 'active',
    'dep_iata': dep_iata,
    'arr_iata': arr_iata
}

url = 'https://app.goflightlabs.com/flights'

# Use urllib.request to make the request
response = urllib.request.urlopen(urllib.request.Request(url, data=urllib.parse.urlencode(params).encode('utf-8')))

data = response.read().decode('utf-8')  # Decode response as text
data_json = json.loads(data)  # Parse JSON data

for flight in data_json:  # Iterate through flights directly
    print(flight['flight']['iata'])
