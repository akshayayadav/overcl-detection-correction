import subprocess
from base_overclfam import BasePath


class BuildMSA(BasePath):
    def __init__(self, fam_id, num_threads=1):
        self.fam_id = fam_id
        self.num_threads = num_threads

    def build_msa_from_fasta(self):
        msa_outfilename = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + BasePath.msa_outfileextension
        fam_outgrp_fasta_filename = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + BasePath.fam_outgrp_fasta_fileextension

        msa_outfile = open(msa_outfilename, "w")
        run_mafft = subprocess.Popen([BasePath.mafft_executable, "--auto", "--amino", "--thread", str(self.num_threads), fam_outgrp_fasta_filename], stdout=msa_outfile, stderr=subprocess.PIPE)
        run_mafft.communicate()
        msa_outfile.close()


if __name__ == '__main__':
    exit()
