import os
from base_overclfam import BasePath
from family_worflow_for_file_rooted_tree_workflow import execute_workflow_for_family


class FamilyWorflowTreeDir(BasePath):
    def __init__(self, clade_species_representation_cutoff):
        self.clade_species_representation_cutoff = clade_species_representation_cutoff

    def execute_workflow_for_family_tree_dir(self):

        for fam_id in os.listdir(BasePath.rooted_famtrees_dir):
            execute_workflow_for_family(fam_id, self.clade_species_representation_cutoff)


if __name__ == '__main__':
    exit()
