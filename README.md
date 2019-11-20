## Container for tree-based over-clustering detecting and correction of gene families

This container contains the tool for analysing and scoring gene families for over-clustering. Each given family fasta is search against a database of outgroup sequences to find the closest outgroup sequences. The family sequences along with the closest sequences is used to build a Maximum-Likelihood (ML) phylogeny and rooted using the monophyletic outgroup clade or the closest outgroup. The family phylogenies are then scored using the proportion of ingroup sequence pairs that appear to diverge after one or more outgroup sequences. Finally, monophyletic ingroup clades are extracted from the family phylogenies based on predefined species representation cutoff.

 1. ### Downloading the container
 ```
docker pull akshayayadav/overcl-detection-correction 
 ```   
