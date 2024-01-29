import numpy as np

a = np.array([[1,2],[3,4]])
print(a)

b = np.array([[5,6]])

c = np.concatenate((a,b), axis=None)  # appended all elements on b
print(c)

c = np.concatenate((a,b.T), axis=1)
print(c)

###

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
# hstack, vstack
c = np.hstack((a,b))  # horizontally
print(c)
c = np.vstack((a,b))  # vertically
print(c)

### Broadcasting

x = np.array([[1,2,3],[4,5,6],[1,2,3],[4,5,6]])
a = np.array([1,0,1])  
y = x + a  # applies for all rows
print(y)
