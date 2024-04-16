import numpy as np
from scipy.linalg import sinm

A = np.array([
    [0, -4, 5, -4],
    [6, 10, -7, 2],
    [4, 4, 0, 5],
    [0, 0, 0, -5],
   ])

# Применяем функцию 2cos(x) + sqrt(x) к Af
Af_modified = sinm(A)

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
    [3, -1, 1, 1, 0],
    [3, 5, 1, -2, -1],
    [2, 2, 3, -2, -1],
    [3, 0, 2, 2, 0],
    [3, 2, 1, -2, 2]
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
-807393/125000,	-275011/250000,	-825033/250000,	 275011/250000,
 825033/125000,	-239731/250000	, 825033/250000,	-275011/125000,
  275011/62500,	 275011/125000,	 292651/125000,	             0,
 -825033/62500	  ,           0	,-825033/125000	, 860313/250000
]
a = [s(l) for l in x]

print(*a, sep=',')