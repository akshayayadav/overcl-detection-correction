### Container for tree-based over-clustering detecting and correction of gene families

This container contains the tool for analysing and scoring gene families for over-clustering. Each given family fasta is search against a database of outgroup sequences to find the closest outgroup sequences. The family sequences along with the closest sequences is used to build a Maximum-Likelihood (ML) phylogeny and rooted using the monophyletic outgroup clade or the closest outgroup. The family phylogenies are then scored using the proportion of ingroup sequence pairs that appear to diverge after one or more outgroup sequences. Finally, monophyletic ingroup clades are extracted from the family phylogenies based on predefined species representation cutoff.

 1. ##### Downloading the container
  ```
  docker pull akshayayadav/overcl-detection-correction 
  ```

 2. #### Preparing the data
  Create a directory *<my\_directory>* containing directory named *family_fasta*, a fasta file named *outgroup-sequences.fa* containing all the outgroup sequences and species label file named *species.profile* containing species labels for the ingroup and outgroup species. The *species.profile* contains 2 columns: first column contains the names of all ingroup and outgroup species and second column containing '1' or '0' labels for ingroup and outgroup names. The names in the *species.profile* file **MUST** be present as prefixes of sequence headers in the family fasta files and the *outgroup-sequences.fa* fasta. Also, the sequence of outgroup names in the *species.profile* file should be same as the relative distance from the ingroup species. For example, if outgroup1 is closer to ingroups than outgroup2 that outgroup1 should be mentioned before outgroup2 in the *species.profile* file.

 3. #### Running the analysis
  ```
  docker run -v <absolute_path_to_data_directory>:/data akshayayadav/overcl-detection-correction run_analysis.sh
  ``` 
