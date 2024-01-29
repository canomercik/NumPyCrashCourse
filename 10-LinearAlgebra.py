import numpy as np

a = np.array([[1,2],[3,4]])
eigenvalues, eigenvectors = np.linalg.eig(a)

print(eigenvalues)
print(eigenvectors)  # column vector

# e_vec * e_val = A * e_vec

b = eigenvectors[:,0] * eigenvalues[0]
print(b)

c = a @ eigenvectors[:,0]
print(c)

# print(b==c) # gives error
print(np.allclose(b,c))  #  comparing if its equal

### Solving linear systems

"""
x1 + x2 = 2200
(1.5)x1 + (4.0)x2 = 5050
"""

A = np.array([[1,1], [1.5,4.0]])
b = np.array([2200,5050])

x = np.linalg.inv(A).dot(b) # inverse slow and can cause problems
print(x)

x = np.linalg.solve(A, b)  # Preffered way
print(x)

### Loading CSV Files

# np.loadtxt()
data = np.genfromtxt('hw_200.csv', delimiter=" ", dtype=np.float32)
print(data.shape)
