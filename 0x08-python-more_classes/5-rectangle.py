#!/usr/bin/python3


class Rectangle:
    """Store the wigth and height of a Rectangle."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __del__(self):
        print("Bye rectangle...")

    def __str__(self):
        rectangle_str = ""

        if self.__height > 0 and self.__width > 0:
            for h in range(self.__height):
                for w in range(self.__width):
                    rectangle_str += '#'
                if h < (self.__height - 1):
                    rectangle_str += '\n'
        return rectangle_str

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", " \
               + str(self.__height) + ')'

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is int:
            if value > -1:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        if type(value) is int:
            if value > -1:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):

        """Find the rectangle area."""

        return self.__height * self.__width

    def perimeter(self):

        """Find the rectangle perimeter."""

        if self.__height is not 0 and self.__width is not 0:
            return (self.__height * 2) + (self.__width * 2)
        else:
            return 0
