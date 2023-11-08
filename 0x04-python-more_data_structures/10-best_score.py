#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    Kmax = ""
    vmax = 0
    for key, value in a_dictionary.items():
        if value > vmax:
            vmax = value
            Kmax = key
    return Kmax
