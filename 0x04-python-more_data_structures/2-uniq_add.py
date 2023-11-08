#!/usr/bin/python3
def uniq_add(my_list=[]):
    x = set()
    res = 0
    for i in my_list:
        if i not in x:
            res += i
            x.add(i)
    return res
