import numpy as np
matrix = np.random.randint(-10, 10, (5, 5))
for row in matrix:
    print(row)
print()

def gaussian_elimination(matrix):
# приведение к ступенчатому виду
    rows, cols = len(matrix), len(matrix[0])
    lead = 0
    for r in range(rows):
        if lead >= cols:
            return
        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == rows:
                i = r
                lead += 1
                if cols == lead:
                    return
        matrix[i], matrix[r] = matrix[r], matrix[i]
        lv = matrix[r][lead]
        matrix[r] = [mrx / float(lv) for mrx in matrix[r]]
        for i in range(rows):
            if i != r:
                lv = matrix[i][lead]
                for j in range(cols):
                    print(lv)
                    print(matrix[i])
                    matrix[i][j] -= lv * matrix[r][j]
                    print(matrix[i])
        lead += 1
        for row in matrix:
            print(row)
        print()


def matrix_rank(matrix):
#вычисление ранга
    gaussian_elimination(matrix)
    rank = sum([1 for row in matrix if any(row)])
    return rank


print("ранг матрицы:", matrix_rank(matrix))

#оценить сложность
