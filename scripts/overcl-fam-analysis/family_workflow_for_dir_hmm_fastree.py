import os
import operator
from base_overclfam import BasePath
from fasta_operations import count_sequences_from_fasta
from family_worflow_for_file_hmm_fasttree import execute_workflow_for_family


class FamilyWorflowFamFastaDir(BasePath):
    def __init__(self, min_family_size):
        self.min_family_size = min_family_size

    def execute_workflow_for_family_dir(self, hmmsearch_evalue_cutoff, msa_num_threads,
                                        clade_species_representation_cutoff,
                                        non_family_seq_count_cutoff):

        famid_arr = self.get_family_list_arr()
        print "## Number of files = {0}\n\n".format(len(famid_arr))
        for fam_id in famid_arr:
            execute_workflow_for_family(fam_id, hmmsearch_evalue_cutoff, msa_num_threads,
                                        clade_species_representation_cutoff,
                                        non_family_seq_count_cutoff)

    def get_family_list_arr(self):
        famid_famsize_dict={}
        for fam_fasta_file in os.listdir(BasePath.family_fasta_filedir):
            fam_size = count_sequences_from_fasta(BasePath.family_fasta_filedir + "/" + fam_fasta_file)
            if self.min_family_size <= fam_size:
                famid_famsize_dict[fam_fasta_file] = fam_size

        famid_arr = self.get_sorted_famid_arr(famid_famsize_dict)
        return famid_arr

    @staticmethod
    def get_sorted_famid_arr(famid_famsize_dict):
        famid_arr = list()
        famid_famsize_dict_sorted = sorted(famid_famsize_dict.items(), key=operator.itemgetter(1))
        for famid_famsize_tuple in famid_famsize_dict_sorted:
            famid_arr.append(famid_famsize_tuple[0])

        return famid_arr


if __name__ == '__main__':
    exit()
