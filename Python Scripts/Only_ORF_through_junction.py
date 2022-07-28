#This script retives only the 1st ORF found by Embossgetorf, which is the ORF that runs through the circular junction.

import re # import regular expressions module

file = input('Enter file name: ') # prompts user for file name
with open(file) as infile:  # opens file
        mylist = list(infile) # make list of all lines

for line in mylist:
    line_as_list = line.strip().split('\t')  # make new list for each line, splitting on tab and removing newline     [newline and tab here - teams has messed formatting]   sequence = line_as_list[2]      # get sequence part of line
    name = line_as_list[0] # 1st tab deliminated section defined as name
    sequence = line_as_list[1] # 2nd tab deliminated section defined as sequence
    ORF_through_junction_with_stop = re.find("[1", name)  # finds the 1st ORF found by emboss, which is also the ORF through the junction due to prior rearrangement
    if ORF_through_junction_with_stop:    #  if, the ORF_through_junction_with_stop condition applies
        with open('Only_ORF_through_junction.txt','a+') as outfile:  # open outfile to append lines with good sequences
                outfile.write(line)

    else:
        with open('other_ORF_after_junction.txt','a+') as outfile:  # open outfile to append lines with good sequences
                outfile.write(line) # write line to file
