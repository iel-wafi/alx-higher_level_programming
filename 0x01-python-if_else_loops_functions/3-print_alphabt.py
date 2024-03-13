#!/usr/bin/python3

for x in range(ord("a"), ord("z") + 1):
    if chr(x) not in ("e", "q"):
        print("{}".format(chr(x)), end="")
