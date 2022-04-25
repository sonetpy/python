#This will modify 1 data of the CSV
import pandas as pd
import numpy as np
abhinav = pd.read_csv('employees.csv')
print("\nBefore any changes in abhinav['Salary'][5]")
print (abhinav)
abhinav['Salary'][5] = 999
print("\nAfter the change abhinav['Salary'][5] = 999")
print(abhinav)
# If you want to save changes to CSV then abhinav.to_csv('employees.csv')
abhinav.to_csv('employees.csv')


