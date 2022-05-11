import requests
response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/states")
print(response.status_code)