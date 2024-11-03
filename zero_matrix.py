import numpy as np


matrix = np.zeros((5, 5))
np.fill_diagonal(matrix, 1)

print("5×5 Matrix with ones on the main diagonal:")
print(matrix)