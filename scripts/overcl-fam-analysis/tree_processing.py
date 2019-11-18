import re


def read_profile_file(profile_filename):
    profile_file = open(profile_filename, "r")
    outgrp_regex_str = ''
    ingroup_regex_str = ''
    species_dict = {}
    outgroup_id_arr = list()
    for line in profile_file:
        line = line.rstrip()
        linearr = re.split(r'\s+', line)
        species_id = linearr[0]
        seq_count = int(linearr[1])
        if seq_count == 0:
            outgrp_regex_str = outgrp_regex_str + "|" + species_id
            outgroup_id_arr.append(species_id)
        else:
            ingroup_regex_str = ingroup_regex_str + "|" + species_id
            species_dict[species_id] = seq_count

    outgrp_regex_str = outgrp_regex_str[1:]
    ingroup_regex_str = ingroup_regex_str[1:]
    return [outgrp_regex_str, species_dict, ingroup_regex_str, outgroup_id_arr]


def get_node_leaves(node):
    leaf_node_arr = node.get_leaves()
    leaf_arr = list()
    for leaf in leaf_node_arr:
        leaf_arr.append(leaf.name)

    return leaf_arr


def check_for_outgroups(leaf_arr, outgrp_re):
    outgrp_matches = list(filter(outgrp_re.search, leaf_arr))
    if len(outgrp_matches) == 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    exit()
