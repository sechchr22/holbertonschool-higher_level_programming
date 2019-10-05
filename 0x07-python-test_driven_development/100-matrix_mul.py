#!/usr/bin/python3
def matrix_mul(m_a, m_b):

    # check if they are lists
    if type(m_a) != list:
        raise TypeError('m_a must be a list')
    elif type(m_b) != list:
        raise TypeError('m_b must be a list')

    # check if they are a list of lists
    for i in range(len(m_a)):
        if type(m_a[i]) != list:
            raise TypeError('m_a must be a list of lists')
    for j in range(len(m_b)):
        if type(m_b[j]) != list:
            raise TypeError('m_b must be a list of lists')

    # check if the list of list is empty
    if len(m_a) == 0:
        raise ValueError('m_a can\'t be empty')
    if len(m_b) == 0:
        raise ValueError('m_b can\'t be empty')

    # check if there is a list inside that is empty
    for i in range(len(m_a)):
        if len(m_a[i]) == 0:
            raise ValueError('m_a can\'t be empty')
    for j in range(len(m_b)):
        if len(m_b[j]) == 0:
            raise ValueError('m_b can\'t be empty')

    # check if there is no integer or float inside
    for i in range(len(m_a)):
        for k in range(len(m_a[i])):
            if type(m_a[i][k]) != int or type(m_a[i][k]) != float:
                raise TypeError('m_a should contain only integers or floats')
    for j in range(len(m_b)):
        for l in range(len(m_b[j])):
            if type(m_b[j][l]) != int or type(m_a[j][l]) != float:
                raise TypeError('m_b should contain only integers or floats')

    # check if they are rectangle matrix
    len_row_a = 0
    for i in range(len(m_a)):
        if i > 0 and len_row_a != len(m_a[i]):
            raise TypeError('each row of m_a must be of the same size')
        len_row_a = len(m_a[i])
    len_row_b = 0
    for j in range(len(m_b)):
        if j > 0 and len_row_b != len(m_b[j]):
            raise TypeError('each row of m_b must be of the same size')
        len_row_b = len(m_b[j])

    # check if the product is posible
    columns_a = len(m_a[0])
    rows_b = len(m_b)
    if columns_a != rows_b:
        raise ValueError('m_a and m_b can\'t be multiplied')

    # if m_a and m_b passed all the checks
    rows_a = len(m_a)
    colums_b = len(m_b[0])
    result_matrix = []
