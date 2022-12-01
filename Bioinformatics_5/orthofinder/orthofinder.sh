#!/usr/bin/bash -l
#SBATCH -p short -N 1 -c 32 -n 1 --out orthofinder.%A.log

module load orthofinder

orthofinder -f cyanobacteria -S diamond_ultra_sens -a 16 -t 32
