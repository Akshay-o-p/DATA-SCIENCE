import numpy as np


matrix = np.random.randint(1, 10, size=(5, 5))
print("Matrix:")
print(matrix)


total_sum = np.sum(matrix)
print("\nSum of all elements:", total_sum)


column_sum = np.sum(matrix, axis=0)
print("Sum of each column:", column_sum)


row_sum = np.sum(matrix, axis=1)
print("Sum of each row:", row_sum)