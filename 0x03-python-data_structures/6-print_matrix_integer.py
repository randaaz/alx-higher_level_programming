#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for row in matrix:
        if len(row) == 0:
            print()
        for j in range(len(row)):
            print("{:d}".format(row[j]),
                  end="\n" if j is len(row) - 1 else " ")
