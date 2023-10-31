#!/usr/bin/python3
for i in range(25, -1, -1):
    char = i + ord('A')
    if (i % 2 == 1):
        char += 32
    print ("{:c}".format(char), end="")
