import urllib.request  # Built-in module for making requests
import json


url = "http://api.open-notify.org/iss-now.json"
response = urllib.request.urlopen(url)

data = response.read().decode('utf-8')  # Decode response as text
data_json = json.loads(data)  # Load JSON data

# Extract longitude and latitude
longitude = data_json['iss_position']['longitude']
latitude = data_json['iss_position']['latitude']
iss_position = (longitude, latitude)

print(data_json)
print(longitude)
print(latitude)
print(iss_position)

# Access other response information
print(response.getcode(), "\n")  # Equivalent to response.status_code
print(data, "\n")  # Equivalent to response.text
print(response.read(), "\n")  # Equivalent to response.content
print(data_json)  # JSON data already parsed
print(data_json.keys())
