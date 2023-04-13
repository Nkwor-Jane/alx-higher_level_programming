#!/usr/bin/python3
"""script to add all arguments to a Python list and save to a file"""
import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
filename = "add_item.json"
if __name__ = "__main__":
    try:
        my_list = load_from_json(filename)
    with open(filename, 'a+', encoding="utf-8") as f:
        my_list = []
        my_list.append(args[1:])
        save_to_json_file(my_list, filename)
        load_from_json_file(filename)
