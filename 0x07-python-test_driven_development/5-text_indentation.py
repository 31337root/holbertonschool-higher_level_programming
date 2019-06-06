#!/usr/bin/python3


def text_indentation(text):

    i = 0

    if text:
        if type(text) is str:
            for char in text:
                if char is '.' or char is '?' or char is ':':
                    print(char)
                    print()
                    i = 1
                    continue
                if i is 1 and char is ' ':
                    i = 0
                    continue
                print(char, end="")
        else:
            raise TypeError("text must be a string")
    else:
        pass
