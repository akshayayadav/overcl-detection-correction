import re
from ete3 import PhyloTree
from base_overclfam import BasePath
from tree_processing import read_profile_file, get_node_leaves


class TreeRooting(BasePath):
    def __init__(self, fam_id, non_family_seq_count_cutoff):
        self.fam_id = fam_id
        self.non_family_seq_count_cutoff = non_family_seq_count_cutoff

    def root_tree(self):
        outgrp_regex_str, species_dict, ingroup_regex_str, outgroup_id_arr = read_profile_file(BasePath.species_profile_filename)
        fam_tree_filename = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + BasePath.fasttree_fileextension
        fam_tree = PhyloTree(fam_tree_filename, format=1)

        outgrp_re = re.compile(outgrp_regex_str)
        ingrp_re = re.compile(ingroup_regex_str)

        outgroup_sequence_list = self.get_regex_matching_sequence_list_from_node(fam_tree, outgrp_re)
        outgroup_monophyly_check = fam_tree.check_monophyly(values=outgroup_sequence_list, target_attr="name")
        if outgroup_monophyly_check[0]:
            print "Outgroups are monophyletic"
            root_node = fam_tree.get_common_ancestor(outgroup_sequence_list)
            fam_tree.set_outgroup(root_node)
            self.write_rooted_tree(fam_tree)

        else:
            print "Outgroups are not monophyletic"

            outgroup_sequence_list_from_seqlist = self.get_outgroup_sequences_from_seqlist()
            arranged_outgroup_sequence_list = self.arrange_outgroup_sequence_ids(outgroup_sequence_list_from_seqlist, outgroup_id_arr)
            root_node = arranged_outgroup_sequence_list[0]
            print "Rooting using sequence {0}".format(root_node)
            fam_tree.set_outgroup(root_node)
            self.write_rooted_tree(fam_tree)

    @staticmethod
    def get_regex_matching_sequence_list_from_node(fam_tree, regex):
        leaf_arr = get_node_leaves(fam_tree)
        sequence_matches_arr = list(filter(regex.search, leaf_arr))
        return sequence_matches_arr

    def write_rooted_tree(self, fam_tree):
        rooted_fam_tree_outfilename = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + \
                        BasePath.rooted_fasttree_fileextension
        fam_tree.write(format=1, outfile=rooted_fam_tree_outfilename)

    def get_outgroup_sequences_from_seqlist(self):
        seqlist_filename = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + BasePath.seqlist_fileextension
        seqlist_file = open (seqlist_filename, "r")
        line_count = 0
        outgroup_sequence_list_from_seqlist = list()
        for line in seqlist_file:
            line = line.strip()
            outgroup_sequence_list_from_seqlist.append(line)
            line_count += 1
            if line_count == self.non_family_seq_count_cutoff:
                break
        seqlist_file.close()
        return outgroup_sequence_list_from_seqlist

    @staticmethod
    def arrange_outgroup_sequence_ids(outgroup_sequence_list, outgroup_id_arr):
        arranged_outgroup_sequence_list = list()
        for outgroup_id in outgroup_id_arr:
            outgroup_id_regex = '^' + outgroup_id
            for outgroup_sequence_id in outgroup_sequence_list:
                if re.match(outgroup_id_regex, outgroup_sequence_id):
                    arranged_outgroup_sequence_list.append(outgroup_sequence_id)

        return arranged_outgroup_sequence_list


if __name__ == '__main__':
    exit()
