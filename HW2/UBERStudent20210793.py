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
    result.append(s)

fr.close()    

resultDic = {}
for r in result:
    
    key = r[0]+","+r[1]
    vehicle = int(r[2])
    trip = int(r[3])
    
    if key in resultDic:
        val = resultDic[key].split(',')
        resultDic[key] = str(vehicle+ int(val[0]))+","+ str(trip+ int(val[1]))
    
    else:
        resultDic[key] = str(vehicle)+","+str(trip)


result_list = []
for key, value in resultDic.items():
    val1 = key.split(",")
    val2 = value.split(',')
    result_list.append([val1[0], val1[1], val2[0], val2[1]])

result_list.sort(key=lambda x: [x[0], x[1]])

for r in result_list:
    s = r[0] + "," + week[int(r[1])] + " " + r[2] + "," + r[3] + "\n"
    fw.write(s)

fw.close()