#!/usr/bin/python3
import sys
from datetime import datetime

inputFile = sys.argv[1]
outputFile = sys.argv[2]

fr = open(inputFile, "rt")
fw = open(outputFile, "wt")
result = []
week = ["MON", "TUE", "WEB", "THU", "FRI", "SAT", "SUN"]
resultDic = {}

while True:
    row = fr.readline()
    if not row: break
    rowSplit = row.strip().split(",")
    date = rowSplit[1]
    dateSplit = date.split("/")
    week_num = datetime(int(dateSplit[2]),int(dateSplit[0]), int(dateSplit[1])).weekday()
    rowSplit[1] = week_num

    key = rowSplit[0] +","+week[week_num]
    vehicle = int(rowSplit[2])
    trip = int(rowSplit[3])
    
    if key in resultDic:
        val = resultDic[key]
        val[0] = val[0] + vehicle
        val[1] = val[1] + trip
    
    else:
        resultDic[key] = [vehicle, trip]

for key, value in resultDic.items():
    keyVal = key.split(",")
    fw.write(keyVal[0] + ","+keyVal[1]+" "+ str(value[0])+","+str(value[1])+"\n")

fr.close()    
fw.close()