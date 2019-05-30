#!/usr/bin/python3


class Square:

    '''Define a private field called size raising some exeptions
    based in the conditions (is not int, less than 0).'''

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, val):
        if type(val) == int:
            if val >= 0:
                self.__size = val
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, val):
        if (len(val) == 2 and
        (map(lambda x: True if type(x) == int and x >= 0 else False), val)):
            self.__position = val
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        '''Returns the current square area.'''
        return self.__size ** 2

    def my_print(self):
        '''Prints in stdout the square with the character #.'''
        if self.__size > 0:
            for i in range(self.__size):
                if self.__position[1] < 2:
                    for spaces in range(self.__position[0]):
                        print(' ', end='')
                for k in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
