#!/usr/bin/python3


def inherits_from(obj, a_class):

    """Function that returns True if the object is an instance
    of a class that inherited (directly or indirectly) from the
    specified class ; otherwise False."""

    if a_class is not None:
        if type(obj) is not a_class:
            return issubclass(type(obj), a_class)
    return False
