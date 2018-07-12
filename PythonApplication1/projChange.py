# -*-coding:utf-8 -*-
import io
import os
import sys
import re
import arcpy
print os.getcwd() 
def readTxt(filename):
    lines = []
    print os.path.exists(filename)
    with open(filename,'r') as f:
       lines = f.readlines()
    for i in range(0,len(lines)):
        arr = re.split(',|\n',lines[i])   
        if re.match(r'^[0-9]*\.[0-9]*$',arr[0]) and re.match(r'^[0-9]*\.[0-9]*$',arr[1]):
            geo = creatPoint(arr[0],arr[1],4490)
            geo2 = pojConver(geo,4523)
            print geo2.WKT
            lines[i] = arr[0] + "," + arr[1] + "," + str(geo2.firstPoint.X) + "," + str(geo2.firstPoint.Y) + "\n"
    with open(filename,'w') as f:
        f.writelines(lines)
def creatPoint(x,y,wkid):
    point = arcpy.Point(x,y)
    sr = arcpy.SpatialReference(wkid)
    ptGeometry = arcpy.PointGeometry(point,sr)
    return ptGeometry   
def pojConver(geo,wkid):
    sr = arcpy.SpatialReference(wkid)
    return geo.projectAs(sr)
for root,dirs,files in os.walk(os.getcwd()):
    for file in files:
        if os.path.splitext(file)[1] == '.txt':
            print "start" + file
            readTxt(file) 
