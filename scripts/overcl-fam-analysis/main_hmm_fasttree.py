#!/usr/bin/python

from family_workflow_for_dir_hmm_fastree import FamilyWorflowFamFastaDir

min_family_size = 2
hmmsearch_evalue_cutoff = "1e-5"
msa_num_threads = 4
clade_species_representation_cutoff = 0.7
non_family_seq_count_cutoff = 10

family_worflow_orthofinder_legumes = FamilyWorflowFamFastaDir(min_family_size)
family_worflow_orthofinder_legumes.execute_workflow_for_family_dir(hmmsearch_evalue_cutoff, msa_num_threads,
                                                                   clade_species_representation_cutoff,
                                                                   non_family_seq_count_cutoff)
