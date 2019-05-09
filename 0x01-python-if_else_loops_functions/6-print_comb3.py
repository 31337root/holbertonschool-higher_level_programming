#!/usr/bin/python3
for num in range(1, 90):
    if num is 89:
        print('{:02d}'.format(num))
        break
    if (num % 10) > (num / 10):
            print('{:02d}'.format(num), end=', ')
