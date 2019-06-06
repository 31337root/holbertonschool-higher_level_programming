#!/usr/bin/python3


def say_my_name(first_name, last_name=""):

    if first_name:
        if type(first_name) is str:
            if type(last_name) is str:
                print("My name is {:s} {:s}".format(first_name, last_name))
            else:
                raise TypeError("last_name must be a string")
        else:
            raise TypeError("first_name must be a string")
    pass
