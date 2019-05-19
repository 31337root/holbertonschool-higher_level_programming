#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    if matrix:
        for i in matrix:
            idx = 0
            for j in i:
                print("{:d}".format(j), end="")
                if idx < (len(i) - 1):
                    print(" ", end="")
                idx += 1
            print()
    else:
        print()
