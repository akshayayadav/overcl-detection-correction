from __future__ import division
import re
from ete3 import PhyloTree
from base_overclfam import BasePath
from tree_processing import read_profile_file, get_node_leaves, check_for_outgroups


class IngroupClades(BasePath):
    def __init__(self, fam_id, species_representation_cutoff=0.5):
        self.fam_id = fam_id
        self.species_representaion_cutoff = species_representation_cutoff

    def get_ingroup_monoplyletic_clades(self):
        outgrp_regex_str, species_dict, ingroup_regex_str = read_profile_file(BasePath.species_profile_filename)
        fam_tree_filename = BasePath.outpath + "/" + self.fam_id + "/" + BasePath.raxml_tree_fileprefix + self.fam_id
        outgroup_re = re.compile(outgrp_regex_str)
        fam_tree = PhyloTree(fam_tree_filename, format=1)
        self.process_family_tree(fam_tree, outgroup_re, species_dict)

    def process_family_tree(self, fam_tree, outgrp_re, species_dict):
        ingroup_clade_arr = list()
        clade_counter = 1
        clade_filename = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + BasePath.clade_fileextension
        clade_file = open(clade_filename, "w")
        for node in fam_tree.traverse("levelorder"):
            leaf_arr = get_node_leaves(node)
            if check_for_outgroups(leaf_arr, outgrp_re):
                flag = self.check_for_clade_overlap(leaf_arr, ingroup_clade_arr)
                if flag == 1:
                    clade_flag = self.check_ingroup_clade_composition(node, species_dict)
                    if clade_flag == 1:
                        self.print_clade_sequences(node, self.fam_id, clade_counter, clade_file)
                        clade_counter += 1

        clade_file.close()

    @staticmethod
    # this function detects and selects only the largest and ingroup clade
    def check_for_clade_overlap(ingroup_clade, ingroup_clade_arr):
        new_clade_detection_flag = 1
        for clade in ingroup_clade_arr:
            overlap = list(set(ingroup_clade).intersection(clade))
            if len(overlap) > 0:
                new_clade_detection_flag = 0
                break
        if new_clade_detection_flag == 1:
            ingroup_clade_arr.append(ingroup_clade)
            return 1
        else:
            return 0

    def check_ingroup_clade_composition(self, ingrp_clade_node, species_dict):
        ingrp_clade_leaves_arr = get_node_leaves(ingrp_clade_node)
        ingrp_clade_species_dict = self.ingrp_clade_species_count(ingrp_clade_leaves_arr)
        no_of_represented_species = self.compare_species_compositions(ingrp_clade_species_dict, species_dict)
        if no_of_represented_species:
            return 1
        else:
            return 0

    @staticmethod
    # gets species counts for the ingroup clade
    def ingrp_clade_species_count(ingrp_clade_leaves_arr):
        ingrp_clade_species_dict = {}
        for seq_id in ingrp_clade_leaves_arr:
            species_id = re.split(r'\.', seq_id)[0]
            if ingrp_clade_species_dict.has_key(species_id):
                ingrp_clade_species_dict[species_id] += 1
            else:
                ingrp_clade_species_dict[species_id] = 1

        return ingrp_clade_species_dict

    # comparing ingroup clade species composition with the expected species composition
    def compare_species_compositions(self, ingrp_clade_species_dict, species_dict):
        species_representation_cutoff = self.species_representaion_cutoff
        no_of_represented_species = 0
        for cl_sp in ingrp_clade_species_dict:
            if ingrp_clade_species_dict[cl_sp] >= species_dict[cl_sp]:
                no_of_represented_species += 1
        if (no_of_represented_species / len(species_dict)) >= species_representation_cutoff:
            return no_of_represented_species
        else:
            return 0

    @staticmethod
    def print_clade_sequences(node, fam_id, clade_counter, clade_file):
        leaf_node_arr = node.get_leaves()
        for leaf in leaf_node_arr:
            # print '{0} {1} {2}'.format(fam_id, clade_counter, leaf.name)
            clade_file.write(fam_id + "_" + str(clade_counter) + " " + leaf.name + "\n")


if __name__ == '__main__':
    exit()
