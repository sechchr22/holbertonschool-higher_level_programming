#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(0, len(matrix)):
        square = list(map(lambda x: x**2, matrix[i]))
        new_matrix.append(square)
    return(new_matrix)
