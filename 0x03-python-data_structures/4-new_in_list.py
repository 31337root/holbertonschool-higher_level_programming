#!/usr/bin/python3


def new_in_list(my_list, idx, element):

    if my_list:
        new_list = []
        for j in my_list:
            new_list.append(j)
        if (idx < len(my_list)) and (idx >= 0):
            new_list[idx] = element
            return new_list
        else:
            return new_list
    else:
        pass
