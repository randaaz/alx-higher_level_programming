#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    element1_tuple_a = tuple_a[0] if len(tuple_a) > 0 else 0
    element2_tuple_a = tuple_a[1] if len(tuple_a) > 1 else 0
    element1_tuple_b = tuple_b[0] if len(tuple_b) > 0 else 0
    element2_tuple_b = tuple_b[1] if len(tuple_b) > 1 else 0
    return (element1_tuple_a + element1_tuple_b, element2_tuple_a + element2_tuple_b)
