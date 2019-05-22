#!/usr/bin/python3


def uniq_add(my_list=[]):

    new_set = set(my_list)
    addition = 0

    for element in new_set:
        addition += element
    return addition
