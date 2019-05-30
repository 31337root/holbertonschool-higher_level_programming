#!/usr/bin/python3

'''Define a private field called size raising some exeptions
   based in the conditions (is not int, less than 0).'''


class Square:

    def __init__(self, size=0):
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
