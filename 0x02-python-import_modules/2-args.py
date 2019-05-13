#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    if len(sys.argv) > 1:
        for i in range((len(sys.argv) - 1)):
            print('{:d}: {:s}'.format(i + 1, sys.argv[i + 1]))
    else:
        print('0 arguments.')
