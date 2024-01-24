matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
print(matrix[0])
print(matrix[0][0])  # first column, second row


for row in matrix:
    print(row)

    for column in row:
        print(column)
    print("-" * 15)
