#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):

    if len(my_list) > 0:
        idx = len(my_list) - 1

        while idx >= 0:
            print("{:d}".format(my_list[idx]))
            idx -= 1
    else:
        pass
