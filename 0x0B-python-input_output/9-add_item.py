#!/usr/bin/python3

import sys
import json
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

"""Script that adds all arguments to a Python list, and then save them to a file."""

with open("add_item.json", 'a') as temp:
    a_list = []
    a_list = load_from_json_file("add_item.json")

    for i in range(len(sys.argv)):
        if i > 0:
            a_list.append(sys.argv[i])

    save_to_json_file(a_list, "add_item.json")
