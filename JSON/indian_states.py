import json
import requests
response = requests.get("http://vocab.nic.in/rest.php/states/json")
data = response.json()
print("Entire JSON response")
print(data)
print("\n")
print(data["states"][0]["state"])
print("\n")
print("Print each key-value pair from JSON response \n")
for key, value in data.items():
    print(key, ":", value)
print("\n")
for i in range(len(data["states"])):
    print(data["states"][i]["state"])
    print("\n")
    print(data["states"][i]["state"]["state_name"])
    print("\n")
