#This script retrieves only the important results from the interproscan

import re # import regular expressions module

file = input('Enter file name: ')

with open(file) as infile:  # open file of circRNA sequences
    mylist = list(infile) # make list of all lines

for line in mylist:  # read each line
    line_as_list = line.strip().split('\t')  # make new list for each line, splitting on tab and removing newline char.
    name = line_as_list[0] # reads the ORFTJ peptide name
    panther_term =  line_as_list[4] # reads the panther term
    protein_family = line_as_list[5] # reads the protein family
    start = line_as_list[6] # reads where the interproscan result starts
    end = line_as_list[7] # reads where the interproscan result ends
    GO_terms = re.findall("GO:{1}[0-9]+", line) # find all start codons in current frame
    with open('interpro_important_results.txt','a+') as outfile:  # open outfile to append lines with good sequences
            outfile.write(name + "\t" + start + "\t" + end + "\t"  + panther_term + "\t" + protein_family + "\t" + str(GO_terms) + "\n") # writes only the importamt results
