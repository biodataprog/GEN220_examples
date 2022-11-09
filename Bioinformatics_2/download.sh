#!/usr/bin/bash
#SBATCH -p batch -N 1 -n 3 
module unload perl
module load sratoolkit
module load aspera
parallel -j 3 fastq-dump --gzip --split-3 {} ::: $(cat acc.txt)
