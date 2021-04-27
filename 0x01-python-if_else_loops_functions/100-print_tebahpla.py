#!/usr/bin/python3
for i in range(0, 26):
    c = ord("z") - i
    if i % 2 is 1:
        c = chr(c + ord("A") - ord("a"))
    else:
        c = chr(c)
    print("{}".format(c), end=(""))
