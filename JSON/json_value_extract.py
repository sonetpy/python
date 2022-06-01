import json
import requests
response = requests.get("https://jsonplaceholder.typicode.com/todos")
# json to python
todos = json.loads(response.text)
#print(todos)
#print(json.dumps(response.json(), indent = 4))
data = json.dumps(response.json(), indent = 4)
#print(data)
print(todos)

