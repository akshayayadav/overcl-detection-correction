import re
from base_overclfam import BasePath
from fasta_operations import get_sequenceids_from_fasta


class ClosestNonFamilySequencesHMMsearch(BasePath):
    def __init__(self, fam_id, non_family_seq_count_cutoff):
        self.fam_id = fam_id
        self.non_family_seq_seq_cutoff = non_family_seq_count_cutoff

    def get_top_sequences_from_hmmsearch(self):
        seqid_list = list()
        seq_count = 0
        hmm_searchfilename = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + BasePath.hmmsearch_fileextension
        hmm_searchfile = open(hmm_searchfilename, "r")
        for line in hmm_searchfile:
            line = line.strip()
            if re.match(r'^\#', line):
                continue
            linearr = re.split(r'\s+', line)
            seqid_list.append(linearr[0])
            seq_count += 1
            if seq_count == self.non_family_seq_seq_cutoff:
                break

        if len(seqid_list) == 0:
            print "No outgroup sequences found\n\n"
            return 0

        fam_seqlist = get_sequenceids_from_fasta (BasePath.family_fasta_filedir + "/" + self.fam_id)
        seqid_list.extend(fam_seqlist)
        seqlist_outfilename = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + BasePath.seqlist_fileextension

        seqlist_outfile = open(seqlist_outfilename, "w")
        for seqid in seqid_list:
            seqlist_outfile.write(seqid + "\n")

        seqlist_outfile.close()

        return 1


if __name__ == '__main__':
    exit()



