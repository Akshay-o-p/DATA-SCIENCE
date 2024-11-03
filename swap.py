import numpy as np


matrix = np.random.randint(1, 100, size=(4, 4))
print("Original 4×4 Matrix:")
print(matrix)


matrix[[0, -1]] = matrix[[-1, 0]]

print("\nMatrix after swapping the first and last rows:")
print(matrix)