import pandas as pd
import multiprocessing
from functools import partial
import numpy as np


def one_to_one_compare(comparison_1, comparison_2):
    """Compare one to one gene key files from an
       all by all blast comparsion"""
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


# Split gene iteration function
def recip_compare(s_file, c_file):
    """Compare split and merge gene calls across reciprocal blast files"""
    recip_list = []
    cross_match = 0
    for row in s_file.itertuples():
        Q_gene = row.Query_gene
        adj_gene_interm = row.adjacent_genes.split(";")
        # list comp to strip metadata and keep gene name
        adj_genes = [i.split(",")[0] for i in adj_gene_interm]
        counter = 0
        for adj_gene in adj_genes:
            Q_search = c_file[c_file.Query_gene.isin([adj_gene])].index.tolist()
            # check to to see that the is one to one match first
            if Q_search and c_file.at[Q_search[0], "gene_type"] =="one_to_one_mapping":
                # Q_search will always results in a list size of 1
                S_search = c_file.at[Q_search[0], "Sytentic_genes"].split(",")[0]
                if S_search == Q_gene:
                    counter += 1
        if counter == len(adj_genes):
            cross_match += 1
            recip_list.append(row)
    recip_df = pd.DataFrame(recip_list)
    return(recip_df)


# Create a function to open up the file and set up parallelization
def All_By_All_compare(i_file1, i_file2, cores):
    """Parallel calls for one to one all by all blast, remember we are using
    cores and not threads"""
    num_processes = int(cores)
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


# check confirmation of split vs merged genes in both direction
def split_compare(i_file1, i_file2, cores):
    """Parallel calls for cplit merge compare from by all blast in reciprocal
    direcitons, remember we are using cores and not threads"""
    num_processes = int(cores)
    file1 = pd.read_csv(i_file1, sep="\t", index_col=False)
    file2 = pd.read_csv(i_file2, sep="\t", index_col=False)
    f1_split = file1[file1.gene_type.isin(["adjacent_genes_syntenic"])]
    f2_split = file2[file2.gene_type.isin(["adjacent_genes_syntenic"])]

    # set up for parallelization
    chunks_1 = np.array_split(f1_split, num_processes)
    # pool.map will only take one arg so set up partial fill
    parallel_1 = partial(recip_compare, c_file=file2)
    pool = multiprocessing.Pool(processes=num_processes)
    # Will return list of pd dfs, need to concat
    recip_1 = pd.concat(pool.map(parallel_1, chunks_1))

    # set up for parallelization
    chunks_2 = np.array_split(f2_split, num_processes)
    parallel_2 = partial(recip_compare, c_file=file1)
    recip_2 = pd.concat(pool.map(parallel_2, chunks_2))

    # merge from both tested directions
    merged_recip = pd.concat([recip_1, recip_2])
    return(merged_recip)


# exmpale run commands
JMM_O2O_B73_Mo17 = All_By_All_compare("B73_Mo17_AllbyAll_res.txt",
                                      "Mo17_B73_AllbyAll_res.txt",
                                      4)

JMM_SC_B73_Mo17 = split_compare("B73_Mo17_AllbyAll_res.txt",
                                "Mo17_B73_AllbyAll_res.txt",
                                4)
