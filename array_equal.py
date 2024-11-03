import numpy as np


array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([1, 2, 3, 4, 5])


are_equal = np.array_equal(array1, array2)

print("Are the two arrays equal element-wise?", are_equal)