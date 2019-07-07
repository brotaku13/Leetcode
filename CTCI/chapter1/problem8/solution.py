"""
0 matrix

given an MxN matrix, if any element is 0, then make that elements whole row and column 0
"""
import random

def zero_matrix(matrix):
    rows = [1] * len(matrix)
    cols = [1] * len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows[i] = 0
                cols[j] = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if rows[i] == 0 or cols[j] == 0:
                matrix[i][j] = 0

def zero_matrix_bv(matrix):
    rows = 0
    cols = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows = rows | 1 << i
                cols = cols | 1 << j
    
    print(bin(cols))
    print(bin(rows))
    def check(vector, ind):
        return (vector >> ind) & 1 == 1

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if check(rows, i) or check(cols, j):
                matrix[i][j] = 0

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
           print(matrix[i][j], end=' ')
        print()



def main():
    rows = 5
    cols = 5
    m = [[random.randint(0, 9) for x in range(cols)] for i in range(rows)]
    print_matrix(m)
    print()
    zero_matrix_bv(m)
    print_matrix(m)

main()