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


WORKFLOW FOR COMPILING TIDY METADATA         

TIDYMETADATA.R
- Write an R Script to take the  R_161128_SHADIL_LIB2500-M002.csv and tidy the data to keep only the columns 
necessary to keep with each file. This required deleting 14 rows of header information and then deleting and 
splitting columns.

PYTHONMETADATA.IPYNB
- Write a python script (pythonmetada - long script) using glob to iterate through fastq.gz files 
2019-04-12_Transcritome/*.fastq.gz and grab information from both the file name and the header line of each file. 
This information is then collected into another csv file - fastqfileinfoframe.csv.
 
PYTHONFASTQGZ.IPYNB 
- gives the same output as PYTHONMETADATA.IPYNB with condensed scripting into one cell.

DATAFRAMEMERGE.R
- An R script to merge the two dataframes tidyR_161128_SHADIL_LIB2500_M002.csv AND fastqfileinfoframe.csv into 
one dataframe mergedframes.csv. 


- Open VCN session to run an interactive session that is not going to kick you off in half an hour. 

- Logging into Pearcey
	$ ssh tuo003pearcey.hpc.csiro.au

- Finding input data on Bowen
	tuo003@pearcey-login:~> cd /OSM/
	tuo003@pearcey-login:/OSM> ls
	CBR  CDC  galaxy
	tuo003@pearcey-login:/OSM> cd CBR
	tuo003@pearcey-login:/OSM/CBR> ls
	AF_DATASCHOOL

	tuo003@pearcey-login:/OSM/CBR> cd AF_DATASCHOOL/
	tuo003@pearcey-login:/OSM/CBR/AF_DATASCHOOL> cd input
	tuo003@pearcey-login:/OSM/CBR/AF_DATASCHOOL/input> ls

- Inside input we find
	2018-04-23_Lmaculans     LukeB           data            kerensa     test.fastq
	2018-05-03_canola        Maddie          fasqc_practise  kim         wat344
	2019-04-12_Transcritome  Pools_metadata  genome          lost+found
	Hiz_Kim                  cla473          jared           ref_genome

- We want 2019-04-12_Transcritome

	tuo003@pearcey-login:/OSM/CBR/AF_DATASCHOOL/input> cd 2019-04-12_Transcritome> ls
	tuo003@pearcey-login:/OSM/CBR/AF_DATASCHOOL/input/2019-04-12_Transcritome> ls

- There are 32 fastqc files + 1 .csv and one .txt file

	CA73YANXX_8_161220_BPO--000_Other_TAAGGCGA-CTCTCTAT_R_161128_SHADIL_LIB2500_M002_R1.fastq.gz
	CA73YANXX_8_161220_BPO--000_Other_TAAGGCGA-CTCTCTAT_R_161128_SHADIL_LIB2500_M002_R2.fastq.gz
	.
	.
	CA73YANXX_8_161220_BPO--031_Other_CGAGGCTG-TCTCTCCG_R_161128_SHADIL_LIB2500_M002_R2.fastq.gz
	R_161128_SHADIL_LIB2500_M002.csv
	samples.txt

- Load fastqc module
	tuo003@pearcey-login:~> module load fastqc
	tuo003@pearcey-login:~> ls -l
	total 32

- Make an output directory (fastqc can't make it and will try to write output to Bowen)
	tuo003@pearcey-login:~> mkdir fastqc_output2
	tuo003@pearcey-login:~> ls -l
	total 36


- For 3.1 run one file on Pearcey and send output to Pearcey home directory (-o means output, $HOME means home directory of where you are now).
	tuo003@pearcey-login:/OSM/CBR/AF_DATASCHOOL/input/2019-04-12_Transcritome> fastqc 
CA73YANXX_8_161220_BPO--031_Other_CGAGGCTG-TCTCTCCG_R_161128_SHADIL_LIB2500_M002_R2.fastq.gz -o $HOME

- Runfastqc on a single file inside a a batch script
	tuo003@pearcey-login:/OSM/CBR/AF_DATASCHOOL/input/2019-04-12_Transcritome> cd $home
	tuo003@pearcey-login:~> sbatch fastqcBatch.q  (sbatch means to submit a batch with file name fastqcBatch.q)

	Submitted batch job 23949452
	tuo003@pearcey-login:~> squeue -u tuo003  (squeue -u tuo003 short usage message, user tuo003) 
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
          23949452        h2   fastqc   tuo003  R       0:09      1 c265

- type sbatch -h (help and tips for running batch, very useful)

- /home/tuo003/testBatch.q is a shell script. Open it and change job name, amount of memory (depends on size of file to be opened and read).

- Batch script to edit
	#!/bin/bash -l
	#SBATCH --job-name=fastqc
	#SBATCH --nodes=1
	#SBATCH --ntasks-per-node=1
	#SBATCH --cpus-per-task=2
	#SBATCH --mem=1gb
	#SBATCH --time=0:10:00

	#SBATCH --mail-type=ALL
	#SBATCH --mail-user=seija.tuomi@csiro.au

- In Pearcey login type 
	module load fastqc
	fastqc '/OSM/CBR/AF_DATASCHOOL/input/2019-04-12_Transcritome/CA73YANXX_8_161220_BPO--030_Other_CGAGGCTG-	
CGTCTAAT_R_161128_SHADIL_LIB2500_M002_R1.fastq.gz' -o '/home/tuo003'

- Email report on job
	SLURM Job_id=23949452 Name=fastqc Began, Queued time 00:00:02
	SLURM Job_id=23949452 Name=fastqc Ended, Run time 00:03:15, COMPLETED, ExitCode 0  
