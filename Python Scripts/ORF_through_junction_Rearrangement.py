# This script rearranges the ORF through the junction circRNAs so they begin with start codon of the ORF that runs through the junction.

import re # import regular expressions module

count = 0
file = input('Enter file name: ') # prompts user for file name
with open(file) as infile:  # opens file
        mylist = list(infile) # make list of all lines



for line in mylist:  # read each line
           line_as_list = line.strip().split('\t')  # make new list for each line, splitting on tab and removing newline     [newline and tab here - teams has messed formatting]   sequence = line_as_list[2]      # get sequence part of line
           name = line_as_list[0] # 1st tab deliminated section defined as name
           sequence = line_as_list[1] # 2nd tab deliminated section defined as sequence
           sequence_length = len(sequence)
           # assign placeholder values of -1 to be replaced by indices
           # note -1 as placeholder value not 0, as 0 is the start position in the code
           # start and stop positions for each frame
           start_f1 = -1
           start_f2 = -1
           start_f3 = -1
           stop_f1 = -1
           stop_f2 = -1
           stop_f3 = -1
           start = re.compile('atg', re.IGNORECASE)  #  start regex to be found in sequences
           stop = re.compile('tga|tag|taa', re.IGNORECASE)  #  stop regex to be found in sequences

           indices_start = [s.start() for s in re.finditer(start, sequence)]  # finds the indices of all the matches.
           indices_stop = [s.start() for s in re.finditer(stop, sequence)]  # finds the indices of all the matches.

           for n in indices_start: # separates each indices on a line

               if n % 3 == 0: # start indices in frame 1 will be divisible by 3
                   start_f1 = n # assign the indices to start_f1

               if ((n + 2) % 3) == 0: # start indices +2  in frame 2 will be divisible by 3
                   start_f2 = n # assign the indices to start_f2

               if ((n + 1) % 3) == 0: # start indices +1  in frame 2 will be divisible by 3
                   start_f3 = n # assign the indices to start_f3


           for n in indices_stop: # separates each indices on a line

               if n % 3 == 0: # stop indices in frame 1 will be divisible by 3
                   stop_f1 = n # assign the indices to start_f3

               if ((n + 2) % 3) == 0: # stop indices +2 in frame 2 will be divisible by 3
                   stop_f2 = n # assign the indices to start_f3

               if ((n + 1) % 3) == 0: # stop indices +1 in frame 3 will be divisible by 3
                   stop_f3 = n  # assign the indices to start_f3



#when the for loop has gone through all of the indices the start/stop f1/2/3 will be the last indices from the end



           if start_f1 > stop_f1: # if the last indices for start is greater than the last for stop then there is an ORF through junction in the given frame

              F1_before_ATG = sequence[:start_f1]
              F1_ATG_to_seq_end = sequence[start_f1:]
              F1_rearranged_sequence = F1_ATG_to_seq_end + F1_before_ATG
              F1_junction_position = int(sequence_length) - int(start_f1)

              with open('rearranged_ORF_through_junction.txt','a+') as outfile:
                  outfile.write(name + '\t' + 'Junction position is ' +  str(F1_junction_position) + '\t' +   str(F1_rearranged_sequence) + '\n')


           if start_f2 > stop_f2: # if the last indices for start is greater than the last for stop then there is an ORF through junction in the given frame
                   F2_before_ATG = sequence[:start_f2]
                   F2_ATG_to_seq_end = sequence[start_f2:]
                   F2_rearranged_sequence = F2_ATG_to_seq_end + F2_before_ATG
                   F2_junction_position = int(sequence_length) - int(start_f2)

                   with open('rearranged_ORF_through_junction.txt','a+') as outfile:
                       outfile.write(name + '\t' + 'Junction position is ' +  str(F2_junction_position) + '\t' +   str(F2_rearranged_sequence) + '\n')


           if start_f3 > stop_f3: # if the last indices for start is greater than the last for stop then there is an ORF through junction in the given frame
                   F3_before_ATG = sequence[:start_f3]
                   F3_ATG_to_seq_end = sequence[start_f3:]
                   F3_rearranged_sequence = F3_ATG_to_seq_end + F3_before_ATG
                   F3_junction_position = int(sequence_length) - int(start_f3)

                   with open('rearranged_ORF_through_junction.txt','a+') as outfile:
                       outfile.write(name + '\t' + 'Junction position is ' +  str(F3_junction_position) + '\t' +   str(F3_rearranged_sequence) + '\n')
