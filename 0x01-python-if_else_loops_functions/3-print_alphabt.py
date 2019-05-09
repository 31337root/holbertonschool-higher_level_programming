#!/usr/bin/python3
for ch in range(97, 123):
    if (ch is not ord('q')) and (ch is not ord('e')):
        print('{}'.format(chr(ch)), end='')
