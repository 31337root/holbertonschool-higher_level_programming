#!/usr/bin/python3


def roman_to_int(roman_string):

    if type(roman_string) is str or roman_string is not None:

        roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                         'D': 500, 'M': 1000}
        temp_list = [roman_numbers[i] for i in roman_string]
        addition = 0

        for i in range(len(temp_list)):
            if i < (len(temp_list) - 1):
                if temp_list[i] < temp_list[i + 1]:
                    addition -= temp_list[i]
                else:
                    addition += temp_list[i]
            else:
                addition += temp_list[i]
        return addition
    else:
        return 0
