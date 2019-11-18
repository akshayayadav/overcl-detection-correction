import subprocess
from base_overclfam import BasePath


class BuildHMM(BasePath):
    def __init__(self, fam_id):
        self.fam_id = fam_id

    def build_hmm_from_msa(self):
        msa_outfilename = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + BasePath.msa_famoutfileextension
        hmm_outfilename = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + BasePath.hmm_fileextension

        run_hmmbuild = subprocess.Popen([BasePath.hmmbuild_executable, "-n", self.fam_id, hmm_outfilename,
                                         msa_outfilename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        run_hmmbuild.communicate()
