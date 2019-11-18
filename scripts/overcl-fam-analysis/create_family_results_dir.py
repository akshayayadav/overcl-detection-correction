import os


def create_family_results_dir(outpath, fam_id):
    if os.path.exists(outpath + "/" + fam_id):
        return 1
    else:
        os.makedirs(outpath + "/" + fam_id)


if __name__ == '__main__':
    exit()
