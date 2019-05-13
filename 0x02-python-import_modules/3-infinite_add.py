#!/usr/bin/python3

if __name__ == '__main__':

    import sys

    args_length = len(sys.argv)
    addition = 0

    if args_length > 1:
        for i in range((args_length - 1)):
            addition += int(sys.argv[i + 1])
        print('{:d}'.format(addition))
    else:
        print('{:d}'.format(addition))
