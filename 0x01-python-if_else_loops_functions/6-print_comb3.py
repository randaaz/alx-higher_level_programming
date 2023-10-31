#!/usr/bin/python3
for tens in range(10):
    for ones in range(10):
        if (tens != ones and tens < ones):
            print("{:d}{:d}".format(tens, ones), end="\n" if tens == 8 else ", ")
