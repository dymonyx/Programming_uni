''''
import numpy as np
from scipy.linalg import expm

A = np.array([
    [5, 1, 0, 0, 0],
    [0, 5, 0, 0, 0],
    [-1, 1, 6, 1, 0],
    [1, 0, -1, 4, 0],
    [3, 0, -3, -3, 2]
])

Af = expm(0.5 * A)
Af = np.around(Af, 2)

print("[", end='')
for i in range(len(Af)):
    print(*[j for j in Af[i]], sep=", ", end='')
    if i != len(Af) - 1:
        print(";", end=' ')
print("]")
'''
import numpy as np
from scipy.linalg import cosm

A = np.array([
    [5, 0, -1, 0, 1],
    [1, 6, 1, 0, -2],
    [1, 1, 5, 0, -1],
    [0, 0, -1, 4, 0],
    [1, 1, 0, 0, 4]
])

Af = cosm(A)
Af = np.around(Af, 2)

print("[", end='')
for i in range(len(Af)):
    print(*[j for j in Af[i]], sep=", ", end='')
    if i != len(Af) - 1:
        print(";", end=' ')
print("]")