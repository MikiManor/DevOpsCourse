#! /usr/bin/env python3
import sys
high = sys.argv[1]
width = sys.argv[2]

if int(high) <= 0 or int(width) <= 0: 
    print("dimentions cannot be negative or Zero! ")
    exit(2)
else:
    line = ''
    for i in range(int(high)):
        for j in range(int(width)):
            line += "*"
        line += "\n"
    print(str(line))

