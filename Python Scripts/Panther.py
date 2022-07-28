#The script finds sequnces in which the Panther terms are different


import re  # import regular expressions module


with open('comparable_results_PANTHER_original_and_circRNA.txt') as infile:  # open file of circRNA sequences
    mylist = list(infile) # make list of all lines
    for line in mylist:  # read each line
        line_as_list = line.strip().split('\t')  # make new list for each line, splitting on tab and removing newline char.
        gene = line_as_list[0] # Field in which the parent gene is located
        circRNA_name = line_as_list[1] # Field of the circRNA name
        panther_term_gene = line_as_list[2] # Field of the parent gene PANTHER term
        panther_term_circRNA = line_as_list[3] # Field of circRNA PANTHER term
        find_panther_gene = re.findall('PTHR\d+', panther_term_gene) # Find only the parent gene PANTHER Term
        find_panther_circRNA = re.findall('PTHR\d+', panther_term_circRNA) # Find only the circRNA PANTHER Term
        if str(find_panther_gene) == str(find_panther_circRNA): # If the PANTHER term of the Parent gene is the same as the circRNA PANTHER term
            with open('Same_panther_circRNA_and_original.txt','a+') as outfile:  #Outfile with same PANTHER Terms
                   outfile.write(line)
        else:
            with open('different_panther_circRNA_and_original.txt','a+') as outfile:  #Outfile with different PANTHER Terms
                   outfile.write(line)
