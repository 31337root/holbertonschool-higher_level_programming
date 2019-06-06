#!/usr/bin/python3


def matrix_divided(matrix, div):

    new_matrix = [[], []]
    j = 0

    if (type(div) is int or type(div) is float) and div is not 0:
        if matrix:
            for i in range(len(matrix)):
                if i < (len(matrix) - 1):
                    if len(matrix[i]) is not len(matrix[i + 1]):
                        raise TypeError("Each row of the matrix must have the same size")
            for _list in matrix:
                if type(_list) is list:
                    for value in _list:
                        if type(value) is int or type(value) is float:
                            new_matrix[j].append(round(value / div, 2))
                        else:
                            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                    j += 1
                else:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            return new_matrix
        else:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif div is 0:
        raise ZeroDivisionError("division by zero")
    else:
        raise TypeError("div must be a number")
