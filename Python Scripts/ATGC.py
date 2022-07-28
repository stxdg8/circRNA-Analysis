#This script retreives only circRNAs in the circAtlas database that contain a nucleotide sequence

import re # import regular expressions module

file = input('Enter file name: ')

with open(file) as infile:  # open file of circRNA sequences
    mylist = list(infile) # make list of all lines
for line in mylist:  # read each line
    line_as_list = line.strip().split('\t')  # make new list for each line, splitting on tab and removing newline char.
    three_fields = len(line_as_list) == 3 # check there are three fields on the line
    only_ATCG = re.match(r'^[ACGT]+$', line_as_list[2], ) # check only ATGC in sequence

    if three_fields and only_ATCG:  # if the 2 checks evaluate to True
        with open('Only_ATGC.txt','a+') as outfile:
            outfile.write(line)  # add the current line to the outfile

    else:                        # if any of the above checks evaluate False
        with open('not_ATGC.txt','a+') as discardfile:  #open second file to store everything to be dumped
            discardfile.write(line)  # add line to file to be dumped
