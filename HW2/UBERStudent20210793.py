#!/usr/bin/python3
import sys
from datetime import datetime

inputFile = sys.argv[1]
outputFile = sys.argv[2]

fr = open(inputFile, "rt")
fw = open(outputFile, "wt")

week = ["MON", "TUE", "WEB", "THU", "FRI", "SAT", "SUN"]
while True:
    row = fr.readline()
    if not row: break
    rowSplit = row.split(",")
    date = rowSplit[1]
    dateSplit = date.split("/")
    week_num = datetime(int(dateSplit[2]),int(dateSplit[0]), int(dateSplit[1])).weekday()
    rowSplit[1] = week[week_num]

    s = ""
    for i in range(len(rowSplit)):
        s += rowSplit[i]
        if i == 0 or i == 2:
            s += ","
        if i == 1:
            s+=" "
    fw.write(s+"\n")

    


