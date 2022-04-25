import numpy as np
print ("vstack () is for Vertical Stack")
n1 = np.array([10,20,30])
n2 = np.array([40,50,60])
print (np.vstack((n1,n2)))
print ("Horizontal Stack using hstack()")
print (np.hstack((n1,n2)))
print ("column_stack() this time")
print(np.column_stack((n1,n2)))


