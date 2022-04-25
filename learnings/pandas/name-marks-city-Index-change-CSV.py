import pandas as pd
import numpy as ny
abhinav = pd.read_csv('employees.csv')
print (abhinav)
print ("\nModifying a INDEX now")
abhinav.index = ['first', 'second', 'third', 'fourth', 'fifth', 'six']
print (abhinav)
