# load tidyverse
library(tidyverse)

# read in the metadata.csv file which is the renamed R_161128_SHADIL_LIB2500-M002.csv
metadata <- read_csv("//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_input/2019-04-12_Transcritome/R_161128_SHADIL_LIB2500_M002.csv")

# remove the first 14 rows
metadataless <- filter(metadata, skip = 14)

#metadataless.csv <- read_csv("data/metadata.csv", skip = 14)

# select columns called Sample/Name, Index and External ID
mtdtlesscolless <- select(metadataless, "Sample/Name" , "Index" , "External ID")

# rename the columns to remove "/" from the first column and " " from the third column
names(mtdtlesscolless) <- c("SampleName" , "Index" , "ExternalID")

# split the first column into three at the underscore and the double dash
mtdtlesscollesssplit <- mtdtlesscolless %>%
  separate(SampleName, into = c("Number" , "Name" , "Sample"))

# select the Sample, Index and ExternalID columns
mtdtlesscollesssplitnonumbername <- select(mtdtlesscollesssplit, "Sample" , "Index" , "ExternalID")

# separate the ExternalID column into DayLength and ID
mtdtlesscollesssplitnonumbername2 <- mtdtlesscollesssplitnonumbername %>%
  separate(ExternalID, into = c("DayLength" , "ID"), sep = 1)

# split the Index column into six: Index1, Index2, Index3, Index4, LeadSeq, TailSeq
mtdtlesscollesssplit2 <- mtdtlesscollesssplitnonumbername2 %>%
  separate(Index, into = c("Index1" , "Index2" , "Index3" , "Index4" , "LeadSeq" , "TailSeq"))

# select the columns with variable values and discard the columns which have the same thing in each cell
mtdtlesscollesssplit2select <- select(mtdtlesscollesssplit2, "Sample" , "Index3" , "Index4" , "LeadSeq" , "TailSeq" , "DayLength","ID")

view(mtdtlesscollesssplit2select)
 

write_csv(mtdtlesscollesssplit2select, "//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/tidyR_161128_SHADIL_LIB2500_M002.csv")
