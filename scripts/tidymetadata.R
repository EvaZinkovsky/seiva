# load tidyverse
library(tidyverse)

# read in the metadata.csv file which is the renamed R_161128_SHADIL_LIB2500-M002.csv
read_csv("metadata.csv")

# remove the first 14 rows
metadataless <- read_csv("metadata", skip = 14)

# select columns called Sample/Name, Index and External ID
mtdtlesscolloess <- select(metadataless, "Sample/Name" , "Index" , "External ID")

# rename the columns to remove "/" from the first column and " " from the third column
names(mtdtlesscolless) <- c("SampleName" , "Index" , "ExternalID")

# split the first column into three at the underscore and the double dash
mtdtlesscollesssplit <- mtdtlesscolless %>%
  separate(SampleName, into = c("Number" , "Name" , "Sample"))

# select the Sample, Index and ExternalID columns
mtdtlesscollesssplitnonumbername <- select(mtdtlesscollesssplit, "Sample" , "Index" , "ExternalID")

# split the Index column into six: Index1, Index2, Index3, Index4, LeadSeq, TailSeq
mtdtlesscollesssplit2 <- mtdtlesscollesssplitnonumbername %>%
  separate(Index, into = c("Index1" , "Index2" , "Index3" , "Index4" , "LeadSeq" , "TailSeq"))

# select the columns with variable values and discard the columns which have the same thing in each cell
mtdtlesscollesssplit2select <- mtdtlesscollesssplit2, "Sample" , "Index3" , "Index4" , "LeadSeq" , "TailSeq")