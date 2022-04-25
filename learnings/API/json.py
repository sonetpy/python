import json
import requests
base_url = "http://api.exchangeratesapi.io/v1/latest?access_key=cc92cae75d84545486db97056e6e128f"
response = requests.get(base_url)
print(json.dumps(response.json(), indent = 4))


