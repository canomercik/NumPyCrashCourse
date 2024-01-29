import numpy as np

l = [1,2,3]
a = np.array([1,2,3])

# l.append(4)
# l = l + [4]
l = l * 2  # Writes list twice
print(l)

# a.append(4) # error 
# a = a + np.array([4])  # adds 4 for every element
a = a * 2 # Doubles the elements value
print(a)

a = np.sqrt(a)
print(a)
a = np.log(a)
print(a)
