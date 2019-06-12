#!/usr/bin/python3


def number_of_lines(filename=""):

    n = 0

    with open(filename) as ofile:
        for l in ofile:
            n += 1
        return n
