import numpy as np

a = np.array([[1,2], [3,4]])

print(a)
print(a.shape)  # rows by coloumns

print(a[0,0])  # index (first row first coloumn)
print(a[:,0])  # ":" means all

print(np.linalg.inv(a))  # reverse
print(np.linalg.det(a))  # determinant

print(np.diag(a))  # diagonal (çapraz-köşegen elementler)
c = np.diag(a)
print(np.diag(c))  # only puts that elements
