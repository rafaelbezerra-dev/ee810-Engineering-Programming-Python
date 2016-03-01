#!/usr/bin/env python
import os, sys

source = "tr.txt"
dest = "DelayValues.txt"
f = open(source, "r")
lines = f.readlines()
f.close()

current_line = len(lines) - 1;

while current_line >= 1:
    if "* * *" in lines[current_line]:
        current_line -= 1
        continue

    words = lines[current_line].split("  ");
    if "ms" in words[len(words) - 1]:
        ms = words[len(words) - 1].replace(" ms", "")
        # float_ms = float(ms)
        f = open(dest, "a")
        f.write(ms)
        f.close()
        os.remove(source)
        break
    current_line -= 1
