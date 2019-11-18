import subprocess
from base_overclfam import BasePath


class PhmmerFamilySearch (BasePath):

    def __init__(self, fam_id, phmmer_evalue_cutoff="1e-5"):
        self.fam_id = fam_id
        self.phmmer_evalue_cutoff = phmmer_evalue_cutoff

    def execute_phmmer_familyfasta_vs_masterfasta(self):
        phmmertlbout_filename = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + \
            BasePath.phmmertlbout_fileextension
        family_fasta_filename = BasePath.family_fasta_filedir + "/" + self.fam_id
        fasta_database_filename = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + \
            BasePath.fasta_database_fileextension
        run_phmmer = subprocess.Popen([BasePath.phmmer_executable, "--tblout", phmmertlbout_filename, "--noali", "-E",
                                       str(self.phmmer_evalue_cutoff), family_fasta_filename, fasta_database_filename],
                                      stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        run_phmmer.communicate()


if __name__ == '__main__':
    exit()
