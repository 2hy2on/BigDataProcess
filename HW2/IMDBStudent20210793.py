#!/usr/bin/python3
import sys
inputFile = sys.argv[1]
outputFile = sys.argv[2]

fr = open(inputFile, "rt")
fw = open(outputFile, "wt")

genre = dict()
while True:
    row = fr.readline()
    if not row: break
    rowSplit = row.split("::")
    temp = rowSplit[2]
    gen = temp.split('|')
    for g in gen:
        g = g.replace("\n", "")
        if g not in genre:
            genre[g] = 1
        else:
            genre[g] += 1

fr.close()
for key, value in genre.items():
    fw.write(f'{key} {value}\n')
fw.close()


