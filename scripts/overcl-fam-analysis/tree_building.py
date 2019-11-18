import re
import subprocess
from base_overclfam import BasePath


class BuildRAxMLTree(BasePath):
    def __init__(self, fam_id, outgroup_id_arr, num_threads=1):
        self.fam_id = fam_id
        self.outgroup_id_arr = outgroup_id_arr
        self.num_threads = num_threads

    def build_tree(self):
        outgroup_sequence_id_arr = self.get_outgroup_sequences()
        arrange_outgroup_sequence_id_arr = self.arrange_outgroup_sequence_ids(outgroup_sequence_id_arr)
        outgroup_string = self.get_outgroup_string(arrange_outgroup_sequence_id_arr)
        self.execute_raxml(outgroup_string)

    def get_outgroup_sequences(self):
        fam_outgrp_fasta_filename = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + \
            BasePath.fam_outgrp_fasta_fileextension
        outgroup_id_arr = self.outgroup_id_arr
        outgroup_sequence_id_arr = list()
        fam_outgrp_fasta_file = open(fam_outgrp_fasta_filename, "r")
        for line in fam_outgrp_fasta_file:
            line = line.rstrip()
            if not re.match(r'^>', line):
                continue
            for outgroup_id in outgroup_id_arr:
                outgroup_id_regex = '^>' + outgroup_id
                if re.match(outgroup_id_regex, line):
                    outgroup_sequence_id_arr.append(line[1:])
                    break

        fam_outgrp_fasta_file.close()
        # print outgroup_sequence_id_arr
        # print len(outgroup_sequence_id_arr)
        return outgroup_sequence_id_arr

    def arrange_outgroup_sequence_ids(self, outgroup_sequence_id_arr):
        outgroup_id_arr = self.outgroup_id_arr
        arranged_outgroup_id_arr = list()
        for outgroup_id in outgroup_id_arr:
            outgroup_id_regex = '^' + outgroup_id
            for outgroup_sequence_id in outgroup_sequence_id_arr:
                if re.match(outgroup_id_regex, outgroup_sequence_id):
                    arranged_outgroup_id_arr.append(outgroup_sequence_id)
        # print arranged_outgroup_id_arr
        # print len(arranged_outgroup_id_arr)
        return arranged_outgroup_id_arr

    @staticmethod
    def get_outgroup_string(arrange_outgroup_sequence_id_arr):
        outgroup_string = ""
        for arrange_outgroup_sequence_id in arrange_outgroup_sequence_id_arr:
            outgroup_string = outgroup_string + "," + arrange_outgroup_sequence_id
        # print outgroup_string[1:]
        return outgroup_string[1:]

    def execute_raxml(self, outgroup_string):
        num_threads = self.num_threads
        msa_outfilename = BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + BasePath.msa_outfileextension
        out_dirname = BasePath.outpath + "/" + self.fam_id
        raxml_out = open(BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id+".raxml_out", "w")
        raxml_err = open(BasePath.outpath + "/" + self.fam_id + "/" + self.fam_id + ".raxml_err", "w")
        run_raxml = subprocess.Popen(
            [BasePath.raxml_executable, "-p", "8", "-m", "PROTGAMMAAUTO", "-T", str(num_threads), "-o", outgroup_string,
             "-s", msa_outfilename, "-n", self.fam_id, "-w", out_dirname], stdout=raxml_out, stderr=raxml_err)

        run_raxml.communicate()
        raxml_out.close()
        raxml_err.close()


if __name__ == '__main__':
    exit()


