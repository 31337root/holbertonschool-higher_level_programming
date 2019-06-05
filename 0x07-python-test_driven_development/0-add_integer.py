#!/usr/bin/python3


def add_integer(a, b=98):

    """Function to add two integers."""

    if ((type(a) is int or type(a) is float) and
       (type(b) is int or type(b) is float)):
        return int(a) + int(b)
    elif a is None or (type(a) is not int and type(a) is not float):
        raise TypeError('a must be an integer')
    elif a is None or (type(b) is not int and type(b) is not float):
        raise TypeError('b must be an integer')
