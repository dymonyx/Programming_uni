import numpy as np
from scipy.linalg import cosm

A = np.array([
    [2, 2, -1, 0, 0],
    [0, 2, 0, 0, 1],
    [-1, 2, 0, 1, 2],
    [-1, 5, -4, 3, 2],
    [-1, 2, -2, 1, 3]
])

# Применяем функцию 2cos(x) + sqrt(x) к Af
Af_modified = cosm(A)

Af_modified = np.around(Af_modified, 2)

print("[", end='')
for i in range(len(Af_modified)):
    print(*[j for j in Af_modified[i]], sep=", ", end='')
    if i != len(Af_modified) - 1:
        print(";", end=' ')
print("]")

import numpy as np
from scipy.linalg import cosm, sqrtm

A = np.array([
    [2, 2, -1, 0, 0],
    [0, 2, 0, 0, 1],
    [-1, 2, 0, 1, 2],
    [-1, 5, -4, 3, 2],
    [-1, 2, -2, 1, 3]
])

Af = cosm(A) * 2 + sqrtm(A)
Af = np.around(Af, 2)

print("[", end='')
for i in range(len(Af)):
    print(*[j for j in Af[i]], sep=", ", end='')
    if i != len(Af) - 1:
        print(";", end=' ')
print("]")

s = lambda x: round(x, 2)
x = [
    4961 / 2000  ,    341 / 125        ,    0 ,- 341 / 250,
    0 ,   4961 / 2000  ,    341 / 250  ,          0,
    0  ,          0 ,   4961 / 2000   ,         0,
    0      ,      0 ,     341 / 250,    4961 / 2000,
]
a = [s(l) for l in x]

print(a, sep=',')