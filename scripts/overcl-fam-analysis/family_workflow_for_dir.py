import os
from base_overclfam import BasePath
from fasta_operations import count_sequences_from_fasta
from family_workflow_for_file import execute_workflow_for_family


class FamilyWorflowFamFastaDir(BasePath):
    def __init__(self, min_family_size, max_family_size):
        self.min_family_size = min_family_size
        self.max_family_size = max_family_size

    def execute_workflow_for_family_dir(self, phmmer_evalue_cutoff, msa_num_threads, outgroup_id_arr,
                                        tree_building_num_threads, clade_species_representation_cutoff,
                                        non_family_seq_representation_cutoff):

        famid_arr = self.get_family_list_arr()
        print "## Number of files = {0}\n\n".format(len(famid_arr))
        for fam_id in famid_arr:
            execute_workflow_for_family(fam_id, phmmer_evalue_cutoff, msa_num_threads, outgroup_id_arr,
                                        tree_building_num_threads, clade_species_representation_cutoff,
                                        non_family_seq_representation_cutoff)

    def get_family_list_arr(self):
        famid_arr = list()
        for fam_fasta_file in os.listdir(BasePath.family_fasta_filedir):
            fam_size = count_sequences_from_fasta(BasePath.family_fasta_filedir + "/" + fam_fasta_file)
            if self.min_family_size <= fam_size <= self.max_family_size:
                famid_arr.append(fam_fasta_file)
        return famid_arr


if __name__ == '__main__':
    exit()
