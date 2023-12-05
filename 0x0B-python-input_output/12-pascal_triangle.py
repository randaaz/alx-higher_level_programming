#!/usr/bin/python3
"""Pascal’s triangle"""


def pascal_triangle(n):
    """Pascal’s triangle"""
    if n <= 0:
        return []
    Pascal_triangle = [[1]]
    while (len(Pascal_triangle) != n):
        last = Pascal_triangle[-1]
        current = [1]
        for i in range(len(last) - 1):
            current.append(last[i] + last[i + 1])
        current.append(1)
        Pascal_triangle.append(current)
    return Pascal_triangle
