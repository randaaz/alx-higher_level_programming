#!/usr/bin/python3
"""append after line"""


def append_after(filename="", search_string="", new_string=""):
    """append after line"""
    with open(filename, "r", encoding='utf-8') as file:
        new_l = []
        while True:
            r_line = file.readline()
            if r_line == "":
                break
            new_l.append(r_line)
            if search_string in r_line:
                new_l.append(new_string)
    with open(filename, "w", encoding='utf-8') as file:
        file.writelines(new_l)
