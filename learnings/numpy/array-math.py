import numpy as np
n1=np.array([10,20])
n2=np.array([30,40])
print("Sum of 2 array: ",np.sum([n1,n2]))
print("Sum of 2 array: ",np.sum([n1,n2],axis=0))
print ("Sum of 2 array: ",np.sum([n1,n2],axis=1))
n3=np.array([10,20,30])
n3=n3+1
print("sum of array :",n3)
n3=n3-1
print("sub of array :",n3)
n3=n3*2
print("multiplication of array :",n3)
n4=n3/2
print("division of array :",n4)
