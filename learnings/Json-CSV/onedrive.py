import csv
with open('onedrive.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    next(reader)

    for row in reader:
        if float(row[-1]) > 75.0: 
            print(row[0], row[-1])



