#!/usr/bin/python3
"""Pascal triangle module"""


def pascal_triangle(n):
    """
    to print pascal triangle

    Args:
       n: int
    """
    matrix = []
    vector = []
    for i in range(n):
        vector.append(1)
        vector_copy = vector.copy()
        matrix.append(vector_copy)

    for i in range(2, len(matrix)):
        for j in range(1, (len(matrix[i]) - 1)):
            matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j]

    return matrix
