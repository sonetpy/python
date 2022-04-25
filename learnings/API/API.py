import requests
# noinspection PyInterpreter
import json
base_url = "http://api.exchangeratesapi.io/v1/latest?access_key=cc92cae75d84545486db97056e6e128f"

response = requests.get(base_url)
print(response.ok, "\n")
print(response.status_code, "\n")
print(response.text, "\n")
print(response.content, "\n")
print(response.json())
print(json.dumps(response.json(), indent = 4))
print(response.json().keys())