# !/usr/bin/python3
"""This script will take a blast output file and return a two column list of
   the top percentage match gene pairs
"""
import collections
file = open("blastn-brachyasDB.csv", "r")
outfile = open("blastn-brachyasDB_best_candidates.txt", "w")
print("Wheat", "Brachy", sep="\t", file=outfile )

header = file.readline()

Best_Genes = collections.OrderedDict()
# Loop through the file and pull out information
for line in file:
    cols = line.split(",")
    wheat = cols[0].split(".")[0]
    brach = cols[1].rsplit(".", 2)[0]
    Identity = cols[2]
    # Add to dict, it gene alread in it, compare identity and replace if higher
    if wheat in Best_Genes.keys():
        if Best_Genes[wheat][1] >= Identity:
            pass
        else:
            Best_Genes[wheat] = [brach, Identity]
    else:
        Best_Genes[wheat] = [brach, Identity]

# Output results
for key, value in Best_Genes.items():
    print(key, value[0], sep="\t", file=outfile)


file.close()
outfile.close()
