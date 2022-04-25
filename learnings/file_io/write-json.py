import json
data = {'item': 'Beer', 'cost':'4.00', 'brand': 'corona'}
print ("Print it in JSON format")
print (json.dumps(data))
#z = json.dumps(data, ensure_ascii=False, indent=4))
print ("dump a file in JSON file")
with open("my-josn.json", mode='w') as myjson:
    myjson.write(json.dumps(data, indent=4))