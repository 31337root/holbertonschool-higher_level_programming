#!/usr/bin/python3

import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

a_list = []

try:
    a_list = load_from_json_file("add_item.json")

except:
    pass

    for i in sys.argv[1:]:
        a_list.append(i)

    save_to_json_file(a_list, "add_item.json")
