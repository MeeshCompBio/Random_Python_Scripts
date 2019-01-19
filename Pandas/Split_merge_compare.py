import pandas as pd
import multiprocessing
from functools import partial
import numpy as np


# function to compare one to one gene keys form all by all blast
def one_to_one_compare(comparison_1, comparison_2):
    # get the number row of df
    total = comparison_1.shape[0]
    interm = 0
    one2one = 0
    for row in comparison_1.itertuples():
        if row.gene_type == "one_to_one_mapping":
            interm += 1
            Q_gene = row.Query_gene
            S_gene = row.Sytentic_genes.split(",")[0]
            # get the index of the query gene in second file using subject gene var
            idx = comparison_2[comparison_2.Query_gene.isin([S_gene])].index.tolist()
            # check to see if the index is empty
            if idx:
                if comparison_2.at[idx[0], "gene_type"] == "one_to_one_mapping":
                    comp_2_S_gene = comparison_2.at[idx[0], "Sytentic_genes"].split(",")[0]
                    if comp_2_S_gene == Q_gene:
                        one2one += 1
    return(total, interm, one2one)


# Create a function to open up the file and set up parallelization
def All_By_All_compare(i_file1, i_file2, threads):
    num_processes = int(threads)
    compare_1 = pd.read_csv(i_file1, sep="\t", index_col=False)
    compare_2 = pd.read_csv(i_file2, sep="\t", index_col=False)
    chunks = np.array_split(compare_1, num_processes)
    # pool.map will only take one arg so set up partial fill
    parallel = partial(one_to_one_compare, comparison_2=compare_2)
    pool = multiprocessing.Pool(processes=num_processes)
    result_list = pool.map(parallel, chunks)
    # our fuction returns lists and we want each item to sum accord to pos
    result = [sum(i) for i in zip(*result_list)]
    return(result)
