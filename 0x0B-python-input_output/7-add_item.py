#!/usr/bin/python3
"""
Module 9-add_item
Contains function that adds and saves to Python obj to JSON file; loads objects

"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file

filename = "add_item.json"

contents = load_from_json_file(filename)

save_to_json_file(contents + argv[1:], filename)
