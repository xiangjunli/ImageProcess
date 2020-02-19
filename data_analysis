# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
a = pd.read_csv("file_name.csv") 
b = pd.read_csv("area.csv")
b = b.dropna(axis=1)
# Preview the first 5 lines of the loaded data 
print(a.head())
print(b.head())

#merge file_name and area to form a new file.
merged = a.merge(b, on='ImgID')
merged.to_csv("output.csv", index=False)
del merged['ImgID']
merged.head

# check duplicated rows
duplicateRowsDF = merged[merged.duplicated(['Line', 'Degree'])]
print("Duplicate Rows based on 2 columns are:", duplicateRowsDF, sep='\n')

#code to keep only last duplicated record
test=merged.sort_values('Line').drop_duplicates(subset=['Line', 'Degree'], keep='last')
test.loc[test['Line']=='52-217-059']

merged['area_idx'] = 'Area_' + merged.Degree.astype(str)
merged['height_idx'] = 'Height_' + merged.Degree.astype(str)
area = merged.pivot_table(index = 'Line', columns = 'area_idx', values = 'Area')
height = merged.pivot_table(index = 'Line', columns = 'height_idx', values = 'Height')
long=area.merge(height, on='Line')
long=long.reset_index()
long
#long.columns

