#!/usr/bin/python3


def write_file(filename="", text=""):

    with open(filename, 'w') as ofile:
        return ofile.write(text)
