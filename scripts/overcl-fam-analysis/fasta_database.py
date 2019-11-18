from base_overclfam import BasePath
from create_family_results_dir import create_family_results_dir


class FamFastaDatabase(BasePath):
    def __init__(self, fam_id):
        self.fam_id = fam_id
        create_family_results_dir(BasePath.outpath, fam_id)

    # function for preparing the database file containing the family sequences and the outgroup sequences
    def prepare_fasta_database(self):
        outgroup_fasta_filename = BasePath.outgroup_fasta_filename
        family_fasta_filename = BasePath.family_fasta_filedir + "/" + self.fam_id
        fasta_database_filename = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + \
            BasePath.fasta_database_fileextension

        fasta_filename_arr = [outgroup_fasta_filename, family_fasta_filename]
        fasta_database_file = open(fasta_database_filename, "w")
        for fasta_filename in fasta_filename_arr:
            fasta_file = open(fasta_filename, "r")
            for line in fasta_file:
                line = line.rstrip()
                fasta_database_file.write(line + "\n")
            fasta_file.close()
        fasta_database_file.close()


if __name__ == '__main__':
    exit()
