#This code will read CSV
# This code will just read and print one column of CSV
import numpy as np
import pandas as pd
print("\nHow to read a CSV file using pd.read_csv('harry.csv')")
abhinav = pd.read_csv('employees.csv')
print (abhinav)
print ("\n\nJust print 1 column abhinav['Salary']") 
print(abhinav['Salary'])


