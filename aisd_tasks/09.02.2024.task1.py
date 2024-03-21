import numpy as np
matrix = np.random.randint (0, 10, (5, 5))
for row in matrix:
    print(row)
print()

def svd(A):
    # Вычисляем матрицу A^T A
    ATA = np.dot(A.T, A)

    # Находим собственные значения и собственные векторы матрицы ATA
    eigenvalues, eigenvectors = np.linalg.eig(ATA)

    # Сортируем собственные значения по убыванию
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    # Вычисляем сингулярные значения
    singular_values = np.sqrt(eigenvalues)

    # Строим матрицу Sigma
    sigma = np.diag(singular_values)

    # Матрица V состоит из собственных векторов матрицы A^T A
    V = eigenvectors

    # Вычисляем матрицу U
    U = np.dot(A, V) / singular_values.reshape(-1, 1)

    return U, sigma, V

U, sigma, Vt = svd(matrix)

print("Матрица U:\n", U)
print("Матрица Sigma:\n", sigma)
print("Матрица V^T:\n", Vt)

rank = 0

for i in range(len(sigma)):
    for j in range(len(sigma)):
        if i == j:
            if sigma[i][j] != 0:
                rank+=1
print(f"ранг равен {rank}")