#This script finds circRNAs that are a multiple of three, these circRNAs maintain the frame if translation occurs through the circular junction

import re # import regular expressions module

file = input('Enter file name: ') # Prompts user for file name
with open(file) as infile:  # open file of cirRNA sequences
    mylist = list(infile) # make list of all lines
for line in mylist:  # read each line
    line_as_list = line.strip().split('\t')  # make new list for each line, splitting on tab and removing newline char.
    two_fields = len(line_as_list) == 2 # check there are three fields on the line
    whole_codons = len(line_as_list[1])%3 == 0 # check if exactly divisible by three
    only_ATCG = re.match(r'^[ACGT]+$', line_as_list[1], ) # check only ATGC in sequence
    if three_fields and whole_codons and only_ATCG:  # if all the three checks evaluate to True
        with open('multiples_of_three.txt','a+') as outfile:  # open outfile to append lines with good sequences
            outfile.write(line)  # add the current line to the outfile
    else:                        # if any of the above checks evaluate False
        with open('not_multiples_of_three.txt','a+') as discardfile:  #open second file to store everything to be dumped
            discardfile.write(line)  # add line to file to be dumped
