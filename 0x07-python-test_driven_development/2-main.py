#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

try:
    print(matrix_divided([], 5))
except Exception as e:
    print(e)
try:
    print(matrix_divided([], 0))
except Exception as e:
    print(e)
try:
    print(matrix_divided([[1, 2 , 3], [1, 2]], 5))
except Exception as e:
    print(e)
try:
    print(matrix_divided(None, 4))
except Exception as e:
    print(e)
try:
    print(matrix_divided([], None))
except Exception as e:
    print(e)
try:
    print(matrix_divided([["hola"], ["Como"]], 6))
except Exception as e:
    print(e)
