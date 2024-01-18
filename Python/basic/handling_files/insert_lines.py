#!/bin/python3
import sys

#file = 'sample_1.txt'
file = f"{sys.argv[1]}"
out_file = 'output.txt'

with open(file, encoding='UTF-8') as f:
    lines = f.readlines()


insert_lines = lines[1:3]

for iter in range(3):
    for i, insert_line in enumerate(insert_lines):
        lines.insert(5+i, insert_line)


print(lines)
with open(out_file, encoding="UTF-8", mode="w") as f:
    f.writelines(lines)