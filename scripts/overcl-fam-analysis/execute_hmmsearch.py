import subprocess
from base_overclfam import BasePath


class HMMsearch(BasePath):
    def __init__(self, fam_id, hmmsearch_evalue_cutoff="1e-5"):
        self.fam_id = fam_id
        self.hmmsearch_evalue_cutoff = hmmsearch_evalue_cutoff

    def search_family_hmm_against_outgroupfasta(self):
        hmm_modelfilename = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + BasePath.hmm_fileextension
        fasta_database_filename = BasePath.outgroup_fasta_filename
        hmmsearch_outfilename = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + BasePath.hmmsearch_fileextension

        run_hmmsearch = subprocess.Popen([BasePath.hmmsearch_executable, "--tblout", hmmsearch_outfilename, "--noali",
                                          "-E", str(self.hmmsearch_evalue_cutoff), hmm_modelfilename,
                                          fasta_database_filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        run_hmmsearch.communicate()
