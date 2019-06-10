#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """Inherits from BaseGeometry and initialize two fields."""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

    def area(self):
        return self.__width * self.__height
