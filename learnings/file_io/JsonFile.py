# json.load(f) : Load JSON data from file (or file-like object).
# json.loads(s): Load JSON data from a string.
# json.dump(j, f): Write JSON object to a file (or file-like object).
# json.dumps(j): Output JSON object as string.

import json
with open ("D:\Scripts\Python\File IO\EmployeeData.json", mode='r') as f:
    json_text = f.read()
apod_dict = json.loads(json_text)
print(apod_dict['explanation'])
print(json.dumps(apod_dict, indent=4))

# Import Python strings to JSON in a file.


