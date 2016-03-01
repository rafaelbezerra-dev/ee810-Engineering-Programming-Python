#!/usr/bin/env python
import os, sys

filename = "/home/pi/Projects/GitHub/ee810/assignment_01/tr.txt"
f = open("tr.txt", "r")
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
        f = open("DelayValues.txt", "a")
        f.write(ms)
        f.close()
        os.remove(filename)
        break
    current_line -= 1
