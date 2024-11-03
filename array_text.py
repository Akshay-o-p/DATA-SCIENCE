import numpy as np


array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


np.savetxt('array.txt', array)

print("Array saved to 'array.txt'.")


loaded_array = np.loadtxt('array.txt')

print("Loaded array from 'array.txt':")
print(loaded_array)