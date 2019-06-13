#!/usr/bin/python3


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        attributs_dict = self.__dict__
        new_dict = {}

        if attrs is not None:
            for att in attrs:
                if att in attributs_dict:
                    new_dict[att] = attributs_dict[att]
            return new_dict
        return attributs_dict
