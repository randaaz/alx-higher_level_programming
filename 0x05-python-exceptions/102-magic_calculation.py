#!/usr/bin/python3
def magic_calculation(a, b):
    r = 0
    for j in range(1, 3):
        try:
            if j > a:
                raise Exception('Too far')
            r += a ** b / j
        except Exception:
            r = b + a
            break
        return r
