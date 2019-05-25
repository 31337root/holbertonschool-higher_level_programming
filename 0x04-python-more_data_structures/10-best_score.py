#!/usr/bin/python3


def best_score(a_dictionary):

    if a_dictionary:
        return max(a_dictionary, key=(lambda value: a_dictionary[value]))
    else:
        return None
