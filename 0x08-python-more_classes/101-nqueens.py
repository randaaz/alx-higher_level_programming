#!/usr/bin/python3
"""N-Queens Solver"""

import sys


def _bord(n):
    """
    Create an empty chessboard of the specified size.

    Args:
        size (int): The size of the chessboard.

    Returns:
        list: A 2D list representing the empty chessboard.
    """
    bord = []
    [bord.append([' ' for j in range(n)]) for j in range(n)]
    return bord


def _copy(bord):
    """
    Create a deep copy of the given chessboard.

    Args:
    chessboard (list): The chessboard to be copied.

    Returns:
    list: A new copy of the chessboard.
    """
    if isinstance(bord, list):
        return list(map(_copy, bord))
    return bord


def p_s(bord):
    """
    Extract the positions of queens on the chessboard.

    Args:
        chessboard (list): The chessboard.

    Returns:
        list: A list of coordinates representing the positions of queens.
    """
    s = []
    for ro in range(len(bord)):
        for co in range(len(bord)):
            if bord[ro][co] == "Q":
                s.append([ro, co])
                break
    return s


def _lout(bord, r, c):
    """
    Mark the attacked positions on the chessboard.

    Args:
        chessboard (list): The chessboard.
        r (int): The row index of the queen.
        c (int): The column index of the queen.
    """
    # x out
    for m in range(c + 1, len(bord)):
        bord[r][m] = "x"
    # x out all
    for m in range(c - 1, -1, -1):
        bord[r][m] = "x"
    # x out
    for y in range(r + 1, len(bord)):
        bord[y][c] = "x"
    # x out
    for y in range(r - 1, -1, -1):
        bord[y][c] = "x"
    # x out
    m = c + 1
    for y in range(r + 1, len(bord)):
        if m >= len(bord):
            break
        bord[y][m] = "x"
        m += 1
    # x out
    m = c - 1
    for y in range(r - 1, -1, -1):
        if m < 0:
            break
        bord[y][m] = "x"
        m -= 1
    # x out
    m = c + 1
    for y in range(r - 1, -1, -1):
        if m >= len(bord):
            break
        bord[y][m] = "x"
        m += 1
    # x out
    m = c - 1
    for y in range(r + 1, len(bord)):
        if m < 0:
            break
        bord[y][m] = "x"
        m -= 1


def _rs(bord, r, q, sol):
    """
    Recursively find all solutions to the N-Queens problem.

    Args:
        chessboard (list): The chessboard.
        current_row (int): The current row being considered.
        queens_placed (int): The number of queens placed so far.
        solutions (list): A list to store solutions.

    Returns:
        list: A list of solutions to the N-Queens problem.
    """
    if q == len(bord):
        sol.append(p_s(bord))
        return sol

    for m in range(len(bord)):
        if bord[r][m] == " ":
            tb = _copy(bord)
            tb[r][m] = "Q"
            _lout(tb, r, m)
            sol = _rs(tb, r + 1, q + 1, sol)
    return sol


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    bord = _bord(int(sys.argv[1]))
    sol = _rs(bord, 0, 0, [])
    for mh in sol:
        print(mh)
