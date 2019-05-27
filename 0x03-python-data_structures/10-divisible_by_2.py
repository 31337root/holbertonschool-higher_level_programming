#!/usr/bin/python3


def divisible_by_2(my_list=[]):

    is_multiple = []
    i = 0
    for i in my_list:
        if (i % 2) == 0:
            is_multiple.append(True)
        else:
            is_multiple.append(False)
    return is_multiple
