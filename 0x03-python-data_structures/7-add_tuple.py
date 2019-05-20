#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    new_tuple = ()
    length_a = len(tuple_a)
    length_b = len(tuple_b)

    if length_a > 1 and length_b > 1:
        for i in range(2):
            new_tuple += (tuple_a[i] + tuple_b[i],)
        return new_tuple
    elif length_a <= 2 and length_b <= 2:
        if length_a == 0 and length_b == 1:
            new_tuple += (tuple_b[0], 0)
            return new_tuple
        elif length_a == 1 and length_b == 0:
            new_tuple += (tuple_a[0], 0)
            return new_tuple
        elif length_b == 0 and length_a == 0:
            new_tuple += (0, 0)
            return new_tuple
        elif length_b == 1 and length_a == 1:
            new_tuple += (tuple_a[0] + tuple_b[0], 0)
            return new_tuple
        elif length_b == 2 and length_a == 1:
            new_tuple += (tuple_a[0] + tuple_b[0], tuple_b[1])
            return new_tuple
        elif length_b == 1 and length_a == 2:
            new_tuple += (tuple_a[0] + tuple_b[0], tuple_a[1])
            return new_tuple
        elif length_b == 2 and length_a == 0:
            new_tuple += (tuple_b[0], tuple_b[1])
            return new_tuple
        elif length_b == 0 and length_a == 2:
            new_tuple += (tuple_a[0], tuple_a[1])
            return new_tuple
