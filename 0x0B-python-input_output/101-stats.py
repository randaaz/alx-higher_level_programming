#!/usr/bin/python3
"""reads stdin line"""


from sys import stdin

sc = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
    }

ts = j = 0


def p():
    """Print file statistics based on input from stdin."""
    print(f'File size: {ts}')
    for k, v in sorted(sc.items()):
        if v > 0:
            print('{:s}: {:d}'.format(k, v))


try:
    for li in stdin:
        split_l = li.split()
        if len(split_l) >= 2:
            s = split_l[-2]
            ts += int(split_l[-1])
            if s in sc:
                sc[s] += 1
        j += 1

        if j % 10 == 0:
            p()
    p()
except KeyboardInterrupt as e:
    p()
