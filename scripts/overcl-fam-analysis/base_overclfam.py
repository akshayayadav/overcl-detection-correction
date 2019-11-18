class BasePath:
    outpath = "/data/results/"
    outgroup_fasta_filename = "/data/outgroup-sequences.fa"
    family_fasta_filedir = "/data/family_fasta/"
    species_profile_filename = "/data/species.profile"

    # for workflow directly processing rooted family trees
    # rooted_famtrees_dir = "/data/family_trees/"

    phmmer_executable = "phmmer"
    mafft_executable = "mafft"
    raxml_executable = "raxmlHPC-PTHREADS-AVX"
    fasttree_executable = "FastTreeMP"
    hmmbuild_executable = "hmmbuild"
    hmmsearch_executable = "hmmsearch"

    fasta_database_fileextension = "_db.fa"
    phmmertlbout_fileextension = ".phmmertlbout"
    seqlist_fileextension = ".seqlist"
    fam_outgrp_fasta_fileextension = "_outgroup_sequences.fa"
    msa_outfileextension = "_outgroup_sequences.fa.msa"
    msa_famoutfileextension = ".msa"
    raxml_tree_fileprefix = "RAxML_bestTree."
    fasttree_fileextension = ".fasttree"
    rooted_fasttree_fileextension = ".rooted_fasttree"
    tree_score_fileextension = ".tree_score"
    clade_fileextension = ".ingroup_monophyletic_clades"
    hmm_fileextension = ".hmm"
    hmmsearch_fileextension = ".hmmsearch"


if __name__ == '__main__':
    exit()
