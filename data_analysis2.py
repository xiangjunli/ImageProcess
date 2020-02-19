# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
import numpy as np
from pandas import DataFrame
import cv2
import re

#extract name and line information and save to a new file.
gz_file=open("/home/schnable/Documents/V3Analysis/file_select.txt")
file_name=open("file_name.txt",'w')
for line in gz_file.read().splitlines():
        x = line.split('\t')        
        y = re.split('.', x[0])
        n = re.split(' |_|-|/', x[1])
        print(x[0], n[10], n[20])
        ImgID = x[0]
        line_name = n[10]
        degree = n[20]
        file_name.write(ImgID + ',' + line_name + ',' + degree + '\n')

gz_file.close()
file_name.close()

# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
a = pd.read_csv("/home/schnable/Documents/V3Analysis/file_name.txt") 
b = pd.read_csv("/home/schnable/Documents/V3Analysis/area_height.csv")
b = b.dropna(axis=1)
# Preview the first 5 lines of the loaded data 
print(a.head())
print(b.head())

#merge file_name and area to form a new file.
merged = a.merge(b, on='ImgID')
merged.to_csv("output.csv", index=False)
del merged['ImgID']
merged.head