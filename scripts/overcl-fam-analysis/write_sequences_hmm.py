from base_overclfam import BasePath
from fasta_operations import get_seqid_sequence_dict_from_multiple_files


class WriteSequencesToFile (BasePath):
    def __init__(self, fam_id):
        self.fam_id = fam_id

    def write_fasta_from_sequence_list(self):
        seqlist_filename = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + BasePath.seqlist_fileextension

        fasta_filename = BasePath.family_fasta_filedir + self.fam_id

        outgroup_fasta = BasePath.outgroup_fasta_filename

        fam_outgrp_fasta_filename = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + \
            BasePath.fam_outgrp_fasta_fileextension

        seqid_sequence_dict = get_seqid_sequence_dict_from_multiple_files([fasta_filename, outgroup_fasta])
        outfasta_file = open(fam_outgrp_fasta_filename, "w")
        seqlist_file = open(seqlist_filename, "r")
        for line in seqlist_file:
            line = line.rstrip()
            outfasta_file.write('>' + line + "\n")
            outfasta_file.write(seqid_sequence_dict[line] + "\n")
        seqlist_file.close()
        outfasta_file.close()


if __name__ == '__main__':
    exit()
