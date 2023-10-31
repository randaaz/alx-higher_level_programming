#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    for i, v in enumerate(str):
        if (i != n):
            new = (new + v)
    return (new)
