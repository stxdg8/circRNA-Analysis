#This script finds circRNAs that contain an infinite open reading frame.


import re # import regular expressions module

with open('multiples_of_three.txt') as infile:  # open file of previously sorted cirRNAs that are divisible by three
    mylist = list(infile) # make list of all lines

for line in mylist:  # read each line
    line_as_list = line.strip().split('\t')  # make new list for each line, splitting on tab and removing newline char.
    if len(line_as_list) >=3:  # ignore any lines that have fewer than 3 fields
        frame = 0            # set index to start reading sequence from.  0 set it to the start of the sequence
        while frame < 3:           # while the starting point is 0,1 or two i.e. three reading frames
            sequence = line_as_list[2]      # get sequence part of line
            sequence = sequence[frame:]       # set starting point of sequence (no effect the first time)
            [sequence[i:i+3] for i in range(0, len(sequence), 3)]  # split sequence into list of codons
            codon_string = ' '.join([sequence[i:i+3] for i in range(0, len(sequence), 3)])  # join list back to string but with spaces between codons
            stop = re.findall("tga|tag|taa", codon_string,re.I)  # find all stop codons in current frame
            start = re.findall("atg", codon_string,re.I)  # find all start codons in current frame
            frame +=1 #  increment the frame number for the next loop and to make frame number reader friendly for outfile
            if start and not stop:    #  if, in current frame, there is a start but no stop, full line to outfile
                with open('IORF.txt','a+') as outfile:  # open outfile to append lines with IORF sequences
                    outfile.write('frame is '+str(frame)+'\t'+line)
