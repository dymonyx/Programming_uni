def rank_matrix(matrix):
    n = len(matrix)
    rank = 0
    for i in range(n):
        if not all(elem == 0 for elem in matrix[i]):
            rank += 1
        for j in range(i + 1, n):
            if all(matrix[j][k] == 0 for k in range(n)):
                continue
            ratio = matrix[j][i] / matrix[i][i]
            for k in range(n):
                matrix[j][k] -= ratio * matrix[i][k]
    return rank

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rank_matrix(matrix))
