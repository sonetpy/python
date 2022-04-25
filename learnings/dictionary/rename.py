# rename city to location
#https://pynative.com/python-dictionary-exercise-with-solutions/
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sampleDict['location'] = sampleDict.pop('city')
print (sampleDict)

