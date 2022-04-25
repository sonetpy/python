import numpy as np
import pandas as pd

dict1 = {
                    "name":['harry', 'rohan', 'skillf', 'shubh'],
                                "marks":[92, 45, 56, 78],
                                            "city":['patna', 'raipur', 'delhi', 'patna']
                                                                }
df = pd.DataFrame(dict1)
print(df)

print ("\nwithout numpy and pandas dict1['name'][0] ")
print (dict1['name'][0])
print ("\nwithout numpy and pandas dict1[i][j]")
j = 0
p = {}
for i in dict1:
    j = len(dict1)
    p = dict1[i][j]
    j = j + 1
    print (p)
print("\nwithout numpy and pandas just by using dict1.items()")
p = {}
for i, j in dict1.items():
    print(i, j)

