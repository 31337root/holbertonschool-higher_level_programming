#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    length = len(sys.argv)

    if length > 1:
        print('{:d} arguments:'.format(length - 1))
        for i in range((length - 1)):
            print('{:d}: {:s}'.format(i + 1, sys.argv[i + 1]))
    else:
        print('0 arguments.')
