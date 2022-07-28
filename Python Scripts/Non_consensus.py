# This script finds circRNAs that contain non_consensus (CTG, GUG and ACG) start codons.

import re # import regular expressions module

file = input('Enter file name: ') #Prompts the user to enter a file name

with open(file) as infile:  # open file of circRNA sequences
    mylist = list(infile) # make list of all lines

for line in mylist:  # read each line
    line_as_list = line.strip().split('\t')  # make new list for each line, splitting on tab and removing newline char.
    sequence = line_as_list[2]      # get sequence part of line
    CUG = re.findall("CTG", sequence)  # find all CTG codons in circRNA sequence
    GUG = re.findall("GUG", sequence)  # find all GUG codons in circRNA sequence
    ACG = re.findall("ACG", sequence)  # find all ACG codons in circRNA sequence
    if CUG or GUG or ACG:    #  if, in current frame, there is a start but no stop, full line to outfile
           with open('non_consensus_ORF.txt','a+') as outfile:  # open outfile to append lines with non consensus start codons
                    outfile.write(line)
    else:
           with open('no_non_consensus_ORF3.txt','a+') as outfile: # open outfile to append lines with no non consensus start codons
                    outfile.write(line)
