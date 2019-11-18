from __future__ import division
import re
import sys
from base_overclfam import BasePath


class ClosestNonFamilySequences(BasePath):

    def __init__(self, fam_id, non_family_seq_representation_cutoff=0.5):
        self.fam_id = fam_id
        self.non_family_seq_representation_cutoff = non_family_seq_representation_cutoff

    # for detection of closest outgroup sequences for the given family
    def get_sequences_from_phmmer_search(self):
        phmmertlbout_filename = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + BasePath.phmmertlbout_fileextension
        family_fasta_filename = BasePath.family_fasta_filedir + "/" + self.fam_id
        seqlist_filename = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + BasePath.seqlist_fileextension

        family_seqid_dict = self.get_family_seqid_dict(family_fasta_filename)
        phmmertblout_file = open(phmmertlbout_filename, "r")
        query_subject_dict = {}
        for line in phmmertblout_file:
            line = line.rstrip()
            if re.match(r'^\#', line):
                continue
            linearr = re.split(r'\s+', line)
            if query_subject_dict.has_key(linearr[2]):
                query_subject_dict[linearr[2]].append(linearr[0])
            else:
                query_subject_dict[linearr[2]] = list()
                query_subject_dict[linearr[2]].append(linearr[0])

        phmmertblout_file.close()
        query_subject_dict = self.remove_worst_nonfamily_sequences(query_subject_dict, family_seqid_dict)
        status = self.print_sequence_list(query_subject_dict, seqlist_filename)
        return status

    @staticmethod
    def get_family_seqid_dict(family_fasta_filename):
        family_seqid_dict = {}
        family_fasta_file = open(family_fasta_filename, "r")
        for line in family_fasta_file:
            line = line.rstrip()
            if re.match(r'^\>', line):
                family_seqid_dict[line[1:]] = 1

        family_fasta_file.close()
        return family_seqid_dict

    def remove_worst_nonfamily_sequences(self, query_subject_dict, family_seqid_dict):
        for query in query_subject_dict:
            seqlist = query_subject_dict[query]
            for seq in list(reversed(query_subject_dict[query])):
                if not (family_seqid_dict.has_key(seq)):
                    seqlist.remove(seq)
                else:
                    break

            query_subject_dict[query] = seqlist

        query_subject_dict = self.remove_less_represented_nonfamily_sequences(query_subject_dict)
        return query_subject_dict

    def remove_less_represented_nonfamily_sequences(self, query_subject_dict):
        non_family_seq_count_dict = self.get_non_family_seq_counts(query_subject_dict)
        query_subject_dict = self.remove_non_family_sequences(query_subject_dict, non_family_seq_count_dict)
        return query_subject_dict

    @staticmethod
    def get_non_family_seq_counts(query_subject_dict):
        non_family_seq_count_dict = {}
        for query in query_subject_dict:
            for seq in query_subject_dict[query]:
                if query_subject_dict.has_key(seq):
                    continue
                if non_family_seq_count_dict.has_key(seq):
                    non_family_seq_count_dict[seq] += 1
                else:
                    non_family_seq_count_dict[seq] = 1
        return non_family_seq_count_dict

    def remove_non_family_sequences(self, query_subject_dict, non_family_seq_count_dict):
        for query in query_subject_dict:
            subject_seqlist = query_subject_dict[query]
            for seq in list(query_subject_dict[query]):
                if non_family_seq_count_dict.has_key(seq):
                    if (non_family_seq_count_dict[seq] / len(query_subject_dict)) < self.non_family_seq_representation_cutoff:
                        subject_seqlist.remove(seq)
            query_subject_dict[query] = subject_seqlist

        return query_subject_dict

    @staticmethod
    def print_sequence_list(query_subject_dict, seqlist_filename):
        seqid_dict = {}
        for query in query_subject_dict:
            for seq in query_subject_dict[query]:
                seqid_dict[seq] = 1

        if len(seqid_dict) == len(query_subject_dict):
            print "No outgroup sequences found. Exiting..."
            return 0

        seqlist_file = open(seqlist_filename, "w")
        for seq in seqid_dict:
            seqlist_file.write(seq + "\n")

        seqlist_file.close()
        return 1


if __name__ == '__main__':
    sys.exit()
