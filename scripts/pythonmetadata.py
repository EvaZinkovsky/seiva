#!/usr/bin/env python
# coding: utf-8

# In[1]:


## !usr/bin/env python
#import the pandas library and aliasing as pd
import numpy
import pandas
fastqinfo = pandas.DataFrame(columns=["Instrument","Run","Flowcell","Lane","SampleName","Rep"])
print(fastqinfo)


# In[2]:


## print all of the files from "location"
import glob
location = '//osm-27-cdc.it.csiro.au/OSM_CBR_AF_DATASCHOOL_input/2019-04-12_Transcritome'
print(glob.glob(location + '/*'))


# In[3]:


## print all of the .fastq.gz files from "location"
import glob
print(glob.glob('//osm-27-cdc.it.csiro.au/OSM_CBR_AF_DATASCHOOL_input/2019-04-12_Transcritome/*.fastq.gz'))


# In[4]:


## put all of the .fastq.gz files from "location" into a list variable globoutput
import glob
globoutput = glob.glob('//osm-27-cdc.it.csiro.au/OSM_CBR_AF_DATASCHOOL_input/2019-04-12_Transcritome/*.fastq.gz')

print(globoutput)


# In[5]:


# shows that files is a list (even though it is stored as what looks like a string)
type(globoutput)


# In[6]:


import glob
import os
globoutput = glob.glob('//osm-27-cdc.it.csiro.au/OSM_CBR_AF_DATASCHOOL_input/2019-04-12_Transcritome/*.fastq.gz')

with open('//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/fastqfiles.txt','w') as outfile: 
    for entry in globoutput:
        outfile.write(entry)
        outfile.write('\n')

with open('//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/fastqfiles.txt', 'r') as readfile:
    print(readfile.read())


# In[7]:


# print the desired sections of each file in globoutput name on a new line separated by '_'
import glob
import os
globoutput = glob.glob('//osm-27-cdc.it.csiro.au/OSM_CBR_AF_DATASCHOOL_input/2019-04-12_Transcritome/*.fastq.gz')

with open('//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/fastqfileinfo.txt','w') as outfile: 
    for entry in globoutput:
        #run
        path_file = entry[92:95] + '_'+ entry[77:86] + '_' + entry[87] + '_' + entry[101:104] + '_' + entry[158:160]
        outfile.write(path_file)
        outfile.write('\n')

with open('//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/fastqfileinfo.txt', 'r') as readfile:
    print(readfile.read())
    


# In[8]:


# put the desired information into a dataframe

import pandas as pd

with open('//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/fastqfileinfo.txt','w') as outfile: 
    for entry in globoutput:
        #run
        path_file = entry[92:95] + '_'+ entry[77:86] + '_' + entry[87] + '_' + entry[101:104] + '_' + entry[158:160]
        outfile.write(path_file)
        outfile.write('\n')

fastqinfo = pd.read_csv('//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/fastqfileinfo.txt', sep = '_', header = None)
fastqinfo.columns = ["Run","Flowcell","Lane","SampleName","Rep"]
print (fastqinfo)


# In[9]:


#from Bio import SeqIO
import gzip
file1 = open('//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/fastqfiles.txt', 'rt')
line = file1.readline()
lines = line[0:169]
#print(lines)

with gzip.open(lines, 'rb') as f:
            header = f.readline()
            print(header)
#for line in file:


# In[10]:


#from Bio import SeqIO
import gzip
file1 = open('//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/fastqfiles.txt', 'rt')

#print(line)


with open('//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/fastqheaders.txt','w') as outfile: 
    for line in file1:
        line = file1.readline()
        lines = line[0:169]
        with gzip.open(lines, 'rb') as f:
            header = f.readline()
        
            outfile.write(str(header))
            outfile.write('\n')

with open('//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/fastqheaders.txt', 'r') as readfile:
    print(readfile.read())


# In[11]:


import os
import glob
import gzip
globoutput = glob.glob('//osm-27-cdc.it.csiro.au/OSM_CBR_AF_DATASCHOOL_input/2019-04-12_Transcritome/*.fastq.gz')
file1 = open('//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/fastqfiles.txt', 'rt')

with open('//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/fastqfiles.txt','w') as outfile1:
    with open('//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/fastqfileinfo.txt','w') as outfile2:    
        for entry in globoutput:
            outfile1.write(entry)
            outfile1.write('\n')
            path_file = entry[92:95] + '_'+ entry[77:86] + '_' + entry[87] + '_' + entry[101:104] + '_' + entry[158:160]
       
        with open('//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/fastqfiles.txt','r') as readfile1:

            for line in readfile1:
                    line = readfile1.readline()
                    lines = line[0:169]
                    with gzip.open(lines, 'rb') as f:
                        header = f.readline()
                        machine = (str(header)[2:13]) + '_'
        
                        outfile2.write(machine)
                        outfile2.write(path_file)         
                        outfile2.write('\n')

with open('//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/fastqfileinfo.txt', 'r') as readfile2:
    print(readfile2.read())
    
    fastqinfo = pd.read_csv('//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/fastqfileinfo.txt', sep = '_', header = None)
    fastqinfo.columns = ["Machine","Run","Flowcell","Lane","SampleName","Rep"]
print (fastqinfo)


# In[ ]:





# In[ ]:




