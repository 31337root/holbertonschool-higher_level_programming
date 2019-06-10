#!/usr/bin/python3


class BaseGeometry:

    """Instance method: def area(self): that raises an Exception.
    Instance method: integer_validator(self) that validates value."""

    def area(self):

    """Instance method: def area(self): that raises an Exception."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name=None, value=None):
        if name is not None and value is not None:
            if type(value) is not int:
                raise TypeError(name + " must be an integer")
            if value < 1:
                raise ValueError(name + " must be greater than 0")
