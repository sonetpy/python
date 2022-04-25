import pandas as pd
s1=pd.Series([1,2,3,4,5,6])
print (s1)
s2=pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])
print (s2)
dic1 = {'a':10,'b':20,'c':30,'d':'40'}
print("\ndictionary:")
print(pd.Series(dic1))
print("\n chnage index position")
s3=pd.Series([1,2,3,4,5,6],index=['d','c','b','a','e','f'])
print(s3)