#This script returns BLAST hits that run 10 aa either side of the circular junction and are of >= 95 identity

import re # import regular expressions module


file = input('Enter file name: ') # prompts user for file name
with open(file) as infile:  # open file of circRNA sequences
   mylist = list(infile) # make list of all lines

for line in mylist: # read each line
    identities = re.findall('Identities\s{1}={1}\s{1}\S+\s{1}\S+', line) # Read the entire Identity result
    identity_percentage = re.findall('\d+%{1}', str(identities)) # Read the indentity percentage
    identity_percentage_digit = re.findall('\d+', str(identity_percentage)) # Read only the identity number
    for i in range(len(identity_percentage_digit)):
        identity_percentage_digit[i] = int(identity_percentage_digit[i]) # Read the number as an integer
        if identity_percentage_digit[i] >= 95:  # if the identity is greater or equal to 95%
           junct_position = re.findall('position\sis\s{1}\d+', str(line)) # Read the junction positon
           junct_position_digit = re.findall('\d+', str(junct_position)) # Read only the junction position number
           Query_position = re.findall('Query{1}\s+\d+\s+\S+\s+\d+', str(line)) # Read the Query positon
           numbers_Query_position = re.findall('\d+', str(Query_position)) # Read only the Query position number
           Query_length_start = numbers_Query_position[0] # Reads only the query length starts position
           int_Query_length_start = int(Query_length_start) # Read the Query length start number as an integer
           Query_length_end = numbers_Query_position[-1] # Reads only the query length end position
           int_Query_length_end = int(Query_length_end) # Read the Query length end number as an integer
           for n in range(len(junct_position_digit)): # separates each indices on a line
               junct_position_digit[n] = int(junct_position_digit[n]) # Read the junction number as an integer
               aa_junct = float(junct_position_digit[n] / 3) # divides the junction position by 3 to convert from nt to aa
               # if the query start + 10 is smaller than the junction position and query end - 10 is greater than the junction position
           if (int_Query_length_start + 10) < aa_junct and (int_Query_length_end - 10) > aa_junct:
               line2 = line.replace("sp", "\nsp") # add hits on new line
               with open('over_94.txt','a+') as outfile:  # open outfile to append lines with good sequences
                  outfile.write(line2) # write line to file
