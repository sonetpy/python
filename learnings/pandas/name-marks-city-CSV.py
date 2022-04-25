import numpy as np
import pandas as pd

dict1 = {
        "name":['harry', 'rohan', 'skillf', 'shubh'],
        "marks":[92, 45, 56, 78],
        "city":['patna', 'raipur', 'delhi', 'patna']}
df = pd.DataFrame(dict1)
print(df)
print ("\nTop 2 lines") 
print(df.head(2))
print("\nLast 2 lines") 
print(df.tail(2))
print("\nDescribe the numerical column")
print(df.describe())
print("\nConverting it to CSV")
df.to_csv('friends.csv')
df.to_csv('friends-index-false.csv', index=False)
