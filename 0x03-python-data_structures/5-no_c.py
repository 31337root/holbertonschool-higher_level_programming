#!/usr/bin/python3


def no_c(my_string):

    if (my_string) and (my_string[0]):
        my_string = list(my_string)
        for i in my_string:
            if (i == 'c'):
                my_string.remove('c')
            if (i == 'C'):
                my_string.remove('C')
        my_string = "".join(my_string)
        return my_string
    else:
        pass
