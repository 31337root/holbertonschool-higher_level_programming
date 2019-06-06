#!/usr/bin/python3


def print_square(size):

    if size:
        if type(size) is int and type(size) is not float:
            if size < 0:
                raise ValueError("size must be >= 0")
            for i in range(size):
                for j in range(size):
                    print('#', end="")
                print()
        else:
            raise TypeError("size must be an integer")
    else:
        pass
