import sys
from family_scoring_rooted_tree_workflow import PairBasedTreeScore
from clade_extraction_rooted_tree_workflow import IngroupClades


def execute_workflow_for_family(fam_id, clade_species_representation_cutoff):

    print 'Processing family {}'.format(fam_id)

    print "Scoring family tree"
    family_tree_score = PairBasedTreeScore(fam_id)
    family_tree_score.score_family_tree()
    print "Family tree scoring done"

    print "Extracting ingroup clades"
    ingroup_clades = IngroupClades(fam_id, clade_species_representation_cutoff)
    ingroup_clades.get_ingroup_monoplyletic_clades()
    print "Ingroup clade extraction done\n\n"


def main():
    fam_id = sys.argv[1]
    clade_species_representation_cutoff = 0.7

    execute_workflow_for_family(fam_id, clade_species_representation_cutoff)


if __name__ == '__main__':
    main()
