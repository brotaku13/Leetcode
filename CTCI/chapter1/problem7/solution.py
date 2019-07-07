"""
Rotate  matrix 90 degrees
Given an NXN matrx, rotate it 90 degrees in place
"""

def rotate(matrix):
    matrix_len = len(matrix)
    for layer in range(matrix_len // 2):
        # go by layer, like an onion
        first = layer
        last = matrix_len - 1 - layer

        for i in range(first, last):
            offset = i - first
            top = matrix[first][i] # save the top
            matrix[first][i] = matrix[last - offset][first] # copy left to top
            matrix[last - offset][first] = matrix[last][last - offset] # copy bottom to left
            matrix[last][last - offset] = matrix[i][last] # copy right to bottom
            matrix[i][last] = top # copy top to right

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
           print(matrix[i][j], end=' ')
        print()

def main():
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    # rotate(m)
    print_matrix(m)
    rotate(m)
    print()
    print_matrix(m)

main()