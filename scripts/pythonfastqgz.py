#!/usr/bin/env python
# coding: utf-8

# In[3]:


### Program to iterate through the all gz files in a directory picking information from the file name 
### and the first line from each file to create a dataframe
### to create 

## final code all in one cell
## import glob, os, pandas as pd, gzip

import glob
import os
import pandas as pd
import gzip

## iterate through the 2019-04-12 fastq.gz files and create a variable globoutput
globoutput = glob.glob('//osm-27-cdc.it.csiro.au/OSM_CBR_AF_DATASCHOOL_input/2019-04-12_Transcritome/*.fastq.gz')

## iterate through globoutput and create textfile fastqfiles.txt as outfile
## put each entry on a new line
with open('//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/fastqfiles.txt','w') as outfile: 
    for entry in globoutput:
        outfile.write(entry)
        outfile.write('\n')
        
## use fastqfiles.txt as readfile1
## use fastqheadersmachine.txt as outfile
## use fastqfileinfoframe.csv as outfile1 as the dataframe

## create a header line with machine, run, flowcell, lane, sample, rep as the column names 
## add to outfile1 as the first line and then go to a new line

## read the first 170 characters of the filename in readfile1 and use this as a variable to open file with gzip
## read the header line
## use the string of the characters from index 2:13 of the header line to create the machine variable
## create a variable path_file with sections from the name of the file (entry from globoutput variable)
## write the machine and path_file variables to outfile. they will be written on the same line
## write a new line
## assign outfile to a variable fastqinfo and print the result

with open('//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/fastqfiles.txt', 'r') as readfile1:
    with open('//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/fastqheadersmachine.txt','w') as outfile1:
        with open('//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/fastqfileinfoframe.csv','w') as outfile: 
            headerline = "Machine" + ',' + "Run" + ',' + "Flowcell" + ',' + "Lane" + ',' + "Sample" + ',' + "Rep"
            outfile.write(headerline)
            outfile.write('\n')
            for line in readfile1:
                lines = line[0:169]
                f = gzip.open(lines, 'rb')
                header = f.readline()
                machine = (str(header)[2:13]) + ','
            for entry in globoutput:
                path_file = entry[92:95] + ','+ entry[77:86] + ',' + entry[87] + ',' + entry[101:104] + ',' + entry[158:160]
       # print(header)
                outfile.write(machine)
                outfile.write(path_file)
                outfile.write('\n')
## assign 
fastqinfo = pd.read_csv('//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/fastqfileinfoframe.csv', sep = '_', header = 0)

print (fastqinfo)


# In[ ]:




