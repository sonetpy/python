import argparse
import csv
import sys
parser = argparse.ArgumentParser(description="Script is to find OneDrive Percentage Usage from Weekly Checklist")
parser.add_argument('--file', help='You need to pass an argument as the filename example <onedrive.csv> OR you can enter any other filename by which you have saved the onedrive CSV file in your computer', type=str)
args = parser.parse_args()
with open(args.file, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    next(reader)

    for row in reader:
        if float(row[-1]) > 75.0: 
            print(row[0], row[-1])

# python.exe c:/Users/kumar/Documents/python/learnings/Json-CSV/onedrive_argpass.py --file iglooonedrive.csv 