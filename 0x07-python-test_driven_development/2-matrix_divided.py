#!/usr/bin/python3

"""
matrix_divided module

divides all elements of a matrix of integers/floats
of the same size

returns a new matrix result of the division or an
exception otherwise

"""


def matrix_divided(matrix, div):

    """
    Args:
        matrix: matrix of the same size
        div: integer/float

    Returns: A new matrix result of the division
    """

    len_row = 0
    str = 'matrix must be a matrix (list of lists) of integers/floats'

    for i in range(len(matrix)):
        if i > 0 and len_row != len(matrix[i]):
            raise TypeError('Each row of the matrix must have the same size')
        len_row = len(matrix[i])
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError(str)
    if type(div) != int and type(div) != float:
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = list(map(list, matrix))

    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            result = round((new_matrix[i][j] / div), 2)
            new_matrix[i][j] = result

    return new_matrix
