module load muscle
module load fasttree
muscle -align MET12.hit_seqs.fasta -output MET12.hit_seqs.afa
FastTree -gamma -wag MET12.hit_seqs.afa  > MET12.hit_seqs.FT.tre
