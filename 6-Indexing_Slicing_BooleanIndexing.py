import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8]])
print(a)

b = a[0,1]  # indexing (row 0, coloumn 1)
print(b)

b = a[0,1:3] # slicing 1 to 3 (3 excluded)
print(b)

###

c = np.array([[1,2],[3,4],[5,6]])
print(c)

bool_idx = c > 2  # boolean indexing
print(bool_idx)

print(c[c>2])  # getting elements

d = np.where(c>2, c, -1)  # where is not true inserts -1
print(d)

###

e = np.array([10,19,30,41,50,61])
print(e)
f = [1,3,5]  # fancy indexing
print(e[f])

even = np.argwhere(a%2==0).flatten()  # finding even numbers
print(e[even])
