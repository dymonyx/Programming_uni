import numpy as np
# Вводим вектора
v1 = np.array([-1,-1,0,1,4])
v2 = np.array([1,-1,1,-4,-6])
v3 = np.array([0,1,-1,1,-2])
v4 = np.array([-1,-2,0,0,3])

# Вводим матрицу Грама
gram_matrix = np.array([[1, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0],
                        [0, 0, 1, 0, 0],
                        [0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 1]])

def orthogonalize(v, u, gram_matrix):
    numerator = np.dot(np.dot(v.T, gram_matrix), u)
    denominator = np.dot(np.dot(u.T, gram_matrix), u)
    if denominator == 0:
        return v
    coefficient = numerator / denominator
    print(f"Коэффициент для подстановки: {coefficient:.4f}")
    return v - coefficient * u

def find_orthogonal_vectors(vectors, gram_matrix):
    ortho_vectors = []
    for v in vectors:
        for u in ortho_vectors:
            v = orthogonalize(v, u, gram_matrix)
        ortho_vectors.append(v)
    return ortho_vectors

# Получаем ортогональные вектора
orthogonal_vectors = find_orthogonal_vectors([v1, v2, v3, v4], gram_matrix)

# Функция для форматирования вывода векторов
def format_vector(v):
    return ", ".join(map(str, v))

# Выводим ортогональные вектора в удобном формате
print("Ортогональные вектора:")
for i, v in enumerate(orthogonal_vectors, start=1):
    if np.all(v == 0):
        print(f"Ортогональный вектор {i}: [ахтунг! нулевой вектор, не включается в базис]")
    else:
        print(f"Ортогональный вектор {i}: [{format_vector(v)}]")

def gram_schmidt(vectors, gram_matrix):
    ortho_vectors = []
    norms = []
    for v in vectors:
        for u in ortho_vectors:
            v = orthogonalize(v, u, gram_matrix)
        norm = np.sqrt(np.dot(np.dot(v.T, gram_matrix), v))
        if norm == 0:
            ortho_vectors.append(v)
            norms.append(0)
            print(f"Предупреждение: нулевой вектор найден, он не входит в базис.")
        else:
            ortho_vectors.append(v / norm)
            norms.append(norm)
    return ortho_vectors, norms

# Получаем ортонормированные вектора и их длины
orthonormal_vectors, norms = gram_schmidt([v1, v2, v3, v4], gram_matrix)

# Выводим ортонормированные вектора в удобном формате и их длины
print("\nОртонормированные вектора и их длины:")
for i, (v, norm) in enumerate(zip(orthonormal_vectors, norms), start=1):
    if np.all(orthogonal_vectors[i-1] == 0):
        print(f"Ортонормированный вектор {i}: [нулевой вектор, не включается в базис]")
        print(f"Длина вектора {i}: 0.0000\n")
    else:
        print(f"Ортонормированный вектор {i}: [{format_vector(v)}]")
        print(f"Длина вектора {i}: {norm:.4f}\n")
