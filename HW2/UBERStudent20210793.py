#!/usr/bin/python3
import sys
from datetime import datetime

inputFile = sys.argv[1]
outputFile = sys.argv[2]

fr = open(inputFile, "rt")
fw = open(outputFile, "wt")
result = []
week = ["MON", "TUE", "WEB", "THU", "FRI", "SAT", "SUN"]
while True:
    row = fr.readline()
    if not row: break
    rowSplit = row.split(",")
    date = rowSplit[1]
    dateSplit = date.split("/")
    week_num = datetime(int(dateSplit[2]),int(dateSplit[0]), int(dateSplit[1])).weekday()
    rowSplit[1] = str(week_num)

    s = []
    for i in range(len(rowSplit)):
        rowSplit[i] = rowSplit[i].replace("\n", "")
        s.append(rowSplit[i])
        if i == 0 or i == 2:
            s.append(",")
        if i == 1:
            s.append(" ")
    result.append(s)

result.sort(key=lambda x: [x[0],x[2]])
fr.close()    

for r in result:
    for i in range(len(r)):
        if i == 2:
            fw.write(week[int(r[i])])
        else:
            fw.write(r[i])
    fw.write("\n")
fw.close()

    


