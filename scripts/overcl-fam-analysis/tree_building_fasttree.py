
import subprocess
from base_overclfam import BasePath


class BuildFastTree(BasePath):
    def __init__(self, fam_id):
        self.fam_id = fam_id

    def execute_fasttree(self):
        msa_outfilename = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + BasePath.msa_outfileextension
        fasttree_outfile = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + BasePath.fasttree_fileextension
        fasttree_log = open(BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + ".fasttree_log", "w")

        run_fasttree = subprocess.Popen(
            [BasePath.fasttree_executable, "-out", fasttree_outfile, msa_outfilename], stderr=fasttree_log)

        run_fasttree.communicate()
        fasttree_log.close()


if __name__ == '__main__':
    exit()
