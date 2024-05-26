import numpy as np

# Вектор v
v = np.array([-6, 3, -3, 0], dtype=float)

# Базисные векторы подпространства L
L = np.array([
    [3, 0, 0, 0],
    [-9, 3, 0, 0],
    [-9, -6, 6, 3]
], dtype=float)


# Ортогонализация векторов подпространства L методом Грама-Шмидта
for i in range(1, L.shape[0]):
    for j in range(i):
        L[i] -= (L[i] @ L[j]) / (L[j] @ L[j]) * L[j]

# Нормализация векторов подпространства L
for i in range(L.shape[0]):
    L[i] /= np.sqrt(L[i] @ L[i])

# Вычисление проекции вектора v на подпространство L
proj = sum((v @ l) / (l @ l) * l for l in L)

# Вычисление косинуса угла между v и его проекцией на L
cos_theta = v @ proj / np.sqrt((v @ v) * (proj @ proj))

# Вычисление угла в градусах
theta = np.arccos(cos_theta)

print(f'Угол = {theta} .')
