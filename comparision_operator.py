import numpy as np


array1 = np.array([1, 5, 3, 7])
array2 = np.array([2, 5, 1, 8])

greater_than = np.greater(array1, array2)
less_than = np.less(array1, array2)
equal_to = np.equal(array1, array2)

print("Greater than comparison:", greater_than)
print("Less than comparison:", less_than)
print("equal to comparison:", equal_to)
