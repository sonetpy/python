import os
import sys
import datetime
age=3
path=input("enter a path :")
if not os.path.exists(path):
    print("Provide a vlaid path ")
    sys.exit(1)
if os.path.isfile(path):
    print("Provide dir path ")
    sys.exit(2)
#print(os.listdir(path)) ## This will list all Files and Dir inside the Path
today=datetime.datetime.now()

for each_file in os.listdir(path):
    each_file_path = os.path.join(path,each_file)
    if os.path.isfile(each_file_path):
        #file_creation_date=datetime.datetime.fromtimestamp(os.path.getctime(k))
        print (each_file_path,datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))) ## This will print only the Files and no Dir and it will also print the ctime of the file.
        #print ("\n Difference in days")
        file_creation_date = datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
        print(each_file_path,today - file_creation_date)


