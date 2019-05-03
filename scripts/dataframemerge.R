# load tidyverse
library(tidyverse)

## merge the output of tidymetadata.R(tidyR_161128_SHADIL_LIB2500_M002.csv) and pythongfastq.gz(fastqfileinfoframe.csv) 
## into "//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/mergedframes.csv"



# assign the tidyR_161128_SHADIL_LIB2500_M002.csv to a variable tidymetadata
tidymetadata <- read_csv("//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/tidyR_161128_SHADIL_LIB2500_M002.csv")

# assign thefastqfileinfoframe.csv to a variable fastqinfo
fastqinfo <- read_csv("//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/fastqfileinfoframe.csv")

# merge the two frames into one called mergedframes
mergedframes <- merge(tidymetadata, fastqinfo, by.x = "Sample", by.y = "Sample")

# write merged frames to mergedframes.csv
write_csv(mergedframes, "//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/mergedframes.csv")

read.csv("//osm-27-cdc.it.csiro.au//OSM_CBR_AF_DATASCHOOL_output/seiva/data/mergedframes.csv")
