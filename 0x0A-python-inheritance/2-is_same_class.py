#!/usr/bin/python3


def is_same_class(obj, a_class):

    """Returns True if the object is exactly an instance
    of the specified class ; otherwise False."""
    if obj is not None and a_class is not None:
        if type(obj) is a_class:
            return True
    return False
