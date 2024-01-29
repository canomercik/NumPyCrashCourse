import numpy as np

a = np.arange(1,7)  # from 1 to 6
print(a)
print(a.shape)

b = a.reshape((3,2))  # do it with 3 rows and 2 coloumns
print(b)

c = a[:, np.newaxis]  # new col for every element
print(c)
