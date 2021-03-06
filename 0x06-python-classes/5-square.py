#!/usr/bin/python3


class Square:

    '''Define a private field called size raising some exeptions
    based in the conditions (is not int, less than 0).'''

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        if type(val) == int:
            if val >= 0:
                self.__size = val
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        '''Returns the current square area.'''
        return self.__size ** 2

    def my_print(self):
        '''Prints in stdout the square with the character #.'''
        if self.__size > 0:
            for i in range(self.__size):
                for k in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
