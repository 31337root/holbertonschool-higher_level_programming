#!/usr/bin/python3
def uppercase(str):
    for string in str:
        if (ord(string) > 96) and (ord(string) < 123):
            print('{:c}'.format(ord(string) - 32), end='')
        else:
            print('{:c}'.format(ord(string)), end='')
    print()
