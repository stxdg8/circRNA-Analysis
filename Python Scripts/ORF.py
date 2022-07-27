#This scripts sorts circRNA sequences from the circATLAs database into those that contain an ORF and those that lack an ORF. 

import re # import regular expressions module

file = input('Enter file name: ') # Prompts the user to enter a file name
with open(file) as infile: # open file of circRNA sequences
    mylist = list(infile) # make list of all lines

for line in mylist:  # read each line
    line_as_list = line.strip().split('\t')  # make new list for each line, splitting on tab and removing newline char.
    if len(line_as_list) >=3:  # ignore any lines that have fewer than 3 fields
        sequence = line_as_list[2]      # get sequence part of line
        start = re.findall("ATG", sequence)  # finds any start codons in the sequnce
        if start:    #  if, in current frame, there is a start but no stop, full line to outfile
           with open('ORF.txt','a+') as outfile:  # open outfile to append lines with circRNAs with an ORF
                    outfile.write(line) # add the current line to the outfile
        else:                           # if any of the above checks evaluate False
           with open('no_ORF.txt','a+') as outfile: # open outfile to append lines with circRNAs with no ORF
                    outfile.write(line) # add the current line to the outfile
