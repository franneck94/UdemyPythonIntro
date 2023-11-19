num_rows = 3
num_cols = 2

matrix = [
    [(i * num_cols + j) + 1 for j in range(num_cols)] for i in range(num_rows)
]

print(matrix)

matrix2 = [[0 for j in range(num_cols)] for i in range(num_rows)]

print(matrix2)

matrix2[0][0] = 1

print(matrix2)
