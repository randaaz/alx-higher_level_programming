#!/usr/bin/python3
def magic_calculation(a, b):
    res = 0
    for j in range(1, 3):
        try:
            if j > a:
                raise Exception("Too far")
                res += a ** b / j
        except Exception:
            res = a + b
            break
        return res
