from family_workflow_for_dir_hmm import FamilyWorflowFamFastaDir

min_family_size = 120
max_family_size = 120
hmmsearch_evalue_cutoff = "1e-5"
msa_num_threads = 4
outgroup_id_arr = ['prupe', 'cucsa', 'arath', 'vitvi', 'solly']
tree_building_num_threads = 4
clade_species_representation_cutoff = 0.7
non_family_seq_count_cutoff = 10

family_worflow_orthofinder_legumes = FamilyWorflowFamFastaDir(min_family_size, max_family_size)
family_worflow_orthofinder_legumes.execute_workflow_for_family_dir(hmmsearch_evalue_cutoff, msa_num_threads,
                                                                   outgroup_id_arr, tree_building_num_threads,
                                                                   clade_species_representation_cutoff,
                                                                   non_family_seq_count_cutoff)
