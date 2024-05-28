import numpy as np

A = np.array([
    [-3, -2, 3, -4, 0, -3, -2, 4, 0],
    [-4, 1, -4, -1, 1, -1, -2, 1, 0],
    [-3, 1, -1, 0, 1, 2, 2, 0, 1]
])

B = np.array([
    [-2, -4, 4, -4, -1, -3, -2, -1, 2],
    [3, 0, 3, -4, 2, -3, 4, 2, -2],
    [-3, 1, 4, 3, -3, 2, 1, 0, -1]
])

# Multiply elements of A by -4 and elements of B by 4
A_mult = -4 * A
B_mult = 4 * B

# Perform the element-wise addition
result_corrected = A_mult + B_mult

print(result_corrected)