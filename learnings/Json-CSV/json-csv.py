import json
import csv
with open("city.json", mode="r") as cityfile:
    readcity = cityfile.read()
# Now parse the file
jsonobj = json.loads(readcity)
print (json.dumps(jsonobj, indent=4))
print ("Just print the name of the first person", json.dumps(jsonobj[0], indent=4))
print ("Print the details of the first person name", (jsonobj[0]['Name']))
## Convert JSON into CSV
#data_file = open("data_file.csv", 'w')
# # now we will open a file for writing 
data_file = open("city.csv", 'w')
# create the csv writer object
csv_writer = csv.writer(data_file)
# Counter variable used for writing
# headers to the CSV file
count=0
for i in jsonobj:
    if count == 0:
        #Writing headers of CSV file
        header = i.keys()
        csv_writer.writerow(header)
        count += 1
    #Writing data of CSV file
    csv_writer.writerow(i.values())
data_file.close()
