#!/usr/bin/python3
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

l_args = list(sys.argv[1:])
try:
    add_args = load_from_json_file("add_item.json")
except Exception:
    add_args = []
add_args.extend(l_args)
save_to_json_file(add_args, 'add_item.json')
