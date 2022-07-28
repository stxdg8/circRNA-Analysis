#Retrieves all of the parent gene names from the circRNA names

import re # import regular expressions module


file = input('Enter file name: ') # prompts user for file name
with open(file) as infile:  # open file of circRNA sequences
    mylist = list(infile) # make list of all lines
for line in mylist:  # read each line
    line_as_list = line.strip().split('\t')  # make new list for each line, splitting on tab and removing newline char.
    name = line_as_list[0] # identifies the field in which the circRNA name is
    only_gene = re.findall('\w+_\d{4}', name) # reads just the circRNA name
    Gene_name1 = str(only_gene).split('_') # Split on the _ which separates the parent gene name and the transcript number
    Gene_name2 = Gene_name1[0] # Identifies which field of the split contains the parent gene
    Gene_name3 = Gene_name2[2:] # reads only the Parent gene name
    with open('Just_gene_name.txt','a+') as outfile:  #open  file to store parent gene names
           outfile.write(Gene_name3 + '\n')  # writes each parent gene on a separate line
