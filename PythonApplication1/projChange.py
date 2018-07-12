# -*- coding: utf-8 -*-
import io
import os
import sys
import re
import arcpy

def changeTxt(filename):
    lines = []
    with open(filename,'r') as f:
       lines = f.readlines()
    for i in range(0,len(lines)):
        arr = re.split(',|\n',lines[i])   
        if re.match(r'^[0-9]*\.[0-9]*$',arr[0]) and re.match(r'^[0-9]*\.[0-9]*$',arr[1]):
            geo = creatPoint(arr[0],arr[1],wkidF)
            geo2 = pojConver(geo,wkidT)
            lines[i] = arr[0] + "," + arr[1] + "," + str(geo2.firstPoint.X) + "," + str(geo2.firstPoint.Y) + "\n"
    with open(filename,'w') as f:
        f.writelines(lines)
    print "success"

def creatPoint(x,y,wkid):
    wkid=int(wkid)
    point = arcpy.Point(x,y)
    sr = arcpy.SpatialReference(wkid)
    ptGeometry = arcpy.PointGeometry(point,sr)
    return ptGeometry 

def pojConver(geo,wkid):
    wkid=int(wkid)
    sr = arcpy.SpatialReference(wkid)
    return geo.projectAs(sr)

wkidF=raw_input("please input WKID_FROM:")
wkidT=raw_input("please input WKID_TO:")
if wkidF=="":
    wkidF=4490
if wkidT=="":
    wkidT=4523

for root,dirs,files in os.walk(os.getcwd()):
    for file in files:
        if os.path.splitext(file)[1] == '.txt':
            print os.getcwd()+"\\" +file+" is started"
            changeTxt(file) 
