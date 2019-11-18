from __future__ import division
import re
from ete3 import PhyloTree
from base_overclfam import BasePath
from create_family_results_dir import create_family_results_dir
from tree_processing import read_profile_file, get_node_leaves, check_for_outgroups


class PairBasedTreeScore(BasePath):
    def __init__(self, fam_id):
        self.fam_id = fam_id
        create_family_results_dir(BasePath.outpath, fam_id)

    # processes given family file
    def score_family_tree(self):

        outgrp_regex_str, species_dict, ingroup_regex_str = read_profile_file(BasePath.species_profile_filename)
        fam_tree_filename = BasePath.rooted_famtrees_dir + "/" + self.fam_id
        fam_tree = PhyloTree(fam_tree_filename, format=1)

        outgrp_re = re.compile(outgrp_regex_str)
        ingrp_re = re.compile(ingroup_regex_str)

        flag = self.check_if_tree_contains_outgroups(fam_tree, outgrp_re)
        if flag == 1:
            return 0

        ingroup_matches_arr = self.get_ingroup_sequence_list(fam_tree, ingrp_re)
        ingroup_pair_arr = self.get_ingroup_sequence_pairs(ingroup_matches_arr)
        precision_val = self.inspect_ingroup_pairs(fam_tree, ingroup_pair_arr, outgrp_re)

        tree_score_filename = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + \
            BasePath.tree_score_fileextension

        tree_score_file = open(tree_score_filename, "w")
        tree_score_file.write(self.fam_id + " " + str(precision_val)+"\n")
        tree_score_file.close()

    @staticmethod
    # function to skip if trees do not have trees
    def check_if_tree_contains_outgroups(fam_tree, outgrp_re):
        leaf_arr = get_node_leaves(fam_tree)
        flag = check_for_outgroups(leaf_arr, outgrp_re)
        return flag

    # function to get ingroup sequence list from the tree
    def get_ingroup_sequence_list(self, fam_tree, ingrp_re):
        leaf_arr = get_node_leaves(fam_tree)
        ingroup_matches_arr = self.get_ingroup_sequences(leaf_arr, ingrp_re)
        return ingroup_matches_arr

    @staticmethod
    # function to get filter out ingroup sequences from all the leaves of the tree
    def get_ingroup_sequences(leaf_arr, ingrp_re):
        ingroup_matches_arr = list(filter(ingrp_re.search, leaf_arr))
        return ingroup_matches_arr

    @staticmethod
    # function to get ingroup sequence pairs
    def get_ingroup_sequence_pairs(ingroup_matches_arr):
        ingroup_matches_arr_len = len(ingroup_matches_arr)
        ingroup_pair_arr = list()
        for ind1 in range(0, ingroup_matches_arr_len):
            for ind2 in range(ind1 + 1, ingroup_matches_arr_len):
                ingroup_pair_arr.append([ingroup_matches_arr[ind1], ingroup_matches_arr[ind2]])
        return ingroup_pair_arr

    # function for checking if given ingroup pair is true/false positive
    def inspect_ingroup_pairs(self, fam_tree, ingroup_pair_arr, outgrp_re):
        fp_pair_count = 0
        tp_pair_count = 0
        for ingroup_pair in ingroup_pair_arr:
            pair_mrca = fam_tree.get_common_ancestor(ingroup_pair[0], ingroup_pair[1])
            pair_mrca_leaf_arr = get_node_leaves(pair_mrca)
            outgrp_flag = check_for_outgroups(pair_mrca_leaf_arr, outgrp_re)
            if outgrp_flag == 1:
                tp_pair_count += 1
            else:
                fp_pair_count += 1

        precision_val = self.calculate_precison_value(tp_pair_count, fp_pair_count)
        return precision_val

    @staticmethod
    # function for calculating precision value
    def calculate_precison_value(tp_pair_count, fp_pair_count):
        precision_val = tp_pair_count / (tp_pair_count + fp_pair_count)
        return precision_val


if __name__ == '__main__':
    exit()
