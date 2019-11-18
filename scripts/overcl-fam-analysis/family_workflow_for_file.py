import sys
import re
from fasta_database import FamFastaDatabase
from family_search import PhmmerFamilySearch
from closest_nonfamily_sequences import ClosestNonFamilySequences
from write_sequences import WriteSequencesToFile
from build_msa import BuildMSA
from tree_building import BuildRAxMLTree
from family_scoring import PairBasedTreeScore
from clade_extraction import IngroupClades


def execute_workflow_for_family(fam_id, phmmer_evalue_cutoff, msa_num_threads, outgroup_id_arr,
                                tree_building_num_threads, clade_species_representation_cutoff,
                                non_family_seq_representation_cutoff):
    # fam_id = "OG0000243"
    # phmmer_evalue_cutoff = "1e-5"
    # msa_num_threads = 5
    # outgroup_id_arr = ['prupe', 'cucsa', 'arath', 'vitvi', 'solly']
    # tree_building_num_threads = 5
    # clade_species_representation_cutoff = 0.7

    print 'Processing family {}'.format(fam_id)

    print "Preparing fasta database"
    family_fasta_database = FamFastaDatabase(fam_id)
    family_fasta_database.prepare_fasta_database()
    print "Fasta database done"

    print "Phmmer database search"
    phmmer_family_search = PhmmerFamilySearch(fam_id, phmmer_evalue_cutoff)
    phmmer_family_search.execute_phmmer_familyfasta_vs_masterfasta()
    print "Phmmer database search done"

    print "Searching for closest outgroup sequences"
    closest_outgroup_sequences = ClosestNonFamilySequences(fam_id, non_family_seq_representation_cutoff)
    status = closest_outgroup_sequences.get_sequences_from_phmmer_search()
    if status == 0:
        return None
    print "Closest outgroup sequence search done"

    print "Writing family-outgroup fasta"
    family_outgroup_fasta = WriteSequencesToFile(fam_id)
    family_outgroup_fasta.write_fasta_from_sequence_list()
    print "Family-outgroup fasta done"

    print "Build family-outgroup MSA"
    family_outgroup_msa = BuildMSA(fam_id, msa_num_threads)
    family_outgroup_msa.build_msa_from_fasta()
    print "Family-outgroup MSA done"

    print "Building family-outgroup ML tree"
    family_outgroup_tree = BuildRAxMLTree(fam_id, outgroup_id_arr, tree_building_num_threads)
    family_outgroup_tree.build_tree()
    print "Family-outgroup ML tree done"

    print "Scoring family-outgroup ML tree"
    family_tree_score = PairBasedTreeScore(fam_id)
    family_tree_score.score_family_tree()
    print "Family-outgroup ML tree scoring done"

    print "Extracting ingroup clades"
    ingroup_clades = IngroupClades(fam_id, clade_species_representation_cutoff)
    ingroup_clades.get_ingroup_monoplyletic_clades()
    print "Ingroup clade extraction done\n\n"


def main():
    fam_id = sys.argv[1]
    phmmer_evalue_cutoff = sys.argv[2]
    msa_num_threads = sys.argv[3]
    outgroup_id_arr = re.split(r',', sys.argv[4])
    tree_building_num_threads = sys.argv[5]
    clade_species_representation_cutoff = sys.argv[6]
    non_family_seq_representation_cutoff = sys.argv[7]

    execute_workflow_for_family(fam_id, phmmer_evalue_cutoff, msa_num_threads, outgroup_id_arr,
                                tree_building_num_threads, clade_species_representation_cutoff,
                                non_family_seq_representation_cutoff)


if __name__ == '__main__':
    main()
