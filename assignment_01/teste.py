#!/usr/bin/env python
import re

f = open("trace_result.txt", "r")
keep = []

for line in f:
    words = line.replace(" \n","").split(" ")
    if len(words) > 1:
        # print words
        print words


f.close()
