import json
from os import path
filename='C:/Users/kumar/Documents/Python/learnings/Project/flight.json'
with open(filename) as f:
    jet = json.load(f)

#print(jet[1])
for i in range(len(jet)):
    print(jet[i]['flight']['iata'])
