# seiva
Seija and Eva Big Data Practical

WHAT WE HAVE DONE
  1. set up a github repository
  2. each set up a clone in our Pearcey home drive
  3. learnt how to access the raw data and associated files on Bowen storage

 RAW DATA AND METADATA
  to get to Bowen
        in gitbash type ssh zin005@pearcey.hpc.csiro.au then answer yes to 'are you sure you want to continue connecting?'
        enter network password
        cd /OSM
        cd CBR
        cd AF_DATASCHOOL
        cd input
        cd 2019-04-12_Transcritome
        
        raw data files end in fastq.gz
          All raw data is in fastq format, an international standard for storing DNA sequence information.
          The 'headers' of each sequence read also contain metadata eg the sequencing 'lane'
        
        Metadata
	  Samples for sequencing were sent to the Garvan Institute.
          
	  R_161128_SHADIL_LIB2500-M002.csv - information for each sample submitted to the sequencing centre at the time of sequencing
		
		Origin:		Other
		Reference:	Egrandis
		Application:	Submitted Library Standard Depth PE Sequencing (HiSeq 2500) v4.0
		Progress:	Library preparation and QC validation complete
	        
          Common to each fastq.gz output file
		Manifest Name:                          R_161128_SHADIL_LIB2500_M002
                Machine:                                HWI-D00119
                Run ID:                                 220
                Flowcell ID:                            CA73YANXX
                Flowcell lane:                          8
                Tile number within flowcell lane:       1101
                Is the read filtered?:                  No
                Are there control bits on?:             No        
    
ALL OTHER FILES
  to get to Pearcey personal home drive
      in gitbash type ssh zin005@pearcey.hpc.csiro.au then answer yes to 'are you sure you want to continue connecting?'
        enter network password 
    
    Read Me File
      readme_date_initials_number
    Scripts
      scriptname_date_initials_number      
    Results
      resultname_date_initials_number
     
  
