#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):

    n = 0

    with open(filename) as ofile:
        for l in ofile:
            n += 1

        if nb_lines < n and nb_lines > 0:
            ofile.seek(0)
            l_ofile = ofile.readlines()
            for i in range(nb_lines):
                print(l_ofile[i], end='')
        else:
            ofile.seek(0)
            print(ofile.read(), end='')
