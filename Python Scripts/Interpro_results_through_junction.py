#This script finds InterproScan results that run through 10 aa through the circular junction

import re # import regular expressions module

file = input('Enter file name: ') # prompts user for file name
with open(file) as infile:  # opens file
        mylist = list(infile) # make list of all lines

for line in mylist:  # read each line
            line_as_list = line.strip().split('\t')  # make new list for each line, splitting on tab and removing newline char.
            start =  line_as_list[3] # reads where the interproscan result starts
            end = line_as_list[4] # reads where the interproscan result ends
            interpro_start_nt = int(start)*3 # converts Interpro aa start poosition to nucleotide position
            interpro_end_nt = int(end)*3 # converts Interpro aa end poosition to nucleotide position
            interpro_start_minus_10_aa = interpro_start_nt + 30 # find the position 10 aa after the start of the InterproScan result
            interpro_end_minus_10_aa = interpro_end_nt - 30 # find the position 10 aa before the end of the Interproscan result
            name = line_as_list[0] # reads the ORFTJ name
            junction_pull =  re.findall("_position_is_\d+", str(name)) # pulls the circRNA junction position
            find_junction = re.findall("\d+", str(junction_pull)) # reads only the junction position number
            int_junction = int(find_junction[0]) # reads the junction position as an integer

            if interpro_start_minus_10_aa <= int_junction and int_junction <= interpro_end_minus_10_aa: # If the Interpro result runs 10 aa before the circ junction and 10 aa after
                with open('Interpro_significant.txt','a+') as outfile:  # open outfile to append lines with good sequences
                         outfile.write(line)
