#!/usr/bin/python3


def pascal_triangle(n):

    big_list = []

    if n <= 0:
        return big_list

    else:
        for i in range(n):
            new_list = []
            new_list.append(1)
            if len(big_list) > 1:
                for k in range(len(big_list[(len(big_list) - 1)])):
                    if k < (len(big_list[(len(big_list) - 1)]) - 1):
                        new_list.append(big_list[len(big_list) - 1][k] +
                                        big_list[len(big_list) - 1][k + 1])
            if len(big_list) > 0:
                new_list.append(1)
            big_list.append(list(new_list))
        return big_list
