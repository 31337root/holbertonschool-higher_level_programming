#!/usr/bin/python3


def number_keys(a_dictionary):

    keys_list = list(a_dictionary.keys())
    n_keys = 0

    for i in keys_list:
        n_keys += 1
    return n_keys
