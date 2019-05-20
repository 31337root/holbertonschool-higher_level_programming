#!/usr/bin/python3


def max_integer(my_list=[]):

    if my_list:
        i = 0
        while i < len(my_list):
            if i + 1 < len(my_list):
                if my_list[i] >= my_list[i + 1]:
                    temp = my_list[i]
                    my_list[i + 1] = temp
            elif my_list[i] > my_list[i - 1]:
                temp = my_list[i]
            i += 1
            if len(my_list) == 1:
                return my_list[0]
        return temp
    else:
        return None
