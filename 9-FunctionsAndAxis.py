import numpy as np

a = np.array([[7,8,9,10,11,12,13],[17,18,19,20,21,22,23]])
print(a)
print(a.sum())  # overall
print(a.sum(axis=0))  # sum for each coloumn
print(a.sum(axis=1))  # sum for each row

print(a.mean(axis=None))  # ortalama

# axis=None is default

print(a.var(axis=None))
print(a.std(axis=None))  # standart variation

print(a.min(axis=None))
print(a.max(axis=None))

### Datatypes

x = np.array([1,2], dtype=np.float64)  # forcing datatype
print(x)
print(x.dtype)

### Copying Arrays

a = np.array([1,2,3])
b = a.copy()  #doesnt change a 
b[0] = 42
print(b)
print(a)

### Generating Arrays

a = np.zeros([2,3])  # zeros 2 by 3
print(a)

a = np.ones([2,3])  # ones 2 by 3
print(a)

a = np.full([2,3], 5.0)  # fives 2 by 3
print(a)

a = np.eye(3)  # ones diagonal (I)
print(a)

a = np.arange(20)  # 1 to 19
print(a)

a = np.linspace(0,10,5)  # start stop step
print(a)

### Random Numbers

a = np.random.random((3,2)) # 0-1
print(a)

a = np.random.randn(1000) #normal/Gaussian
print(a.mean(),a.var())

a = np.random.randint(10,size=(3,3))
print(a)

a = np.random.choice(5, size=10)
print(a)

a = np.random.choice([-8,-7,-6], size=10)
print(a)
