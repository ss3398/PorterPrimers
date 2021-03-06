#!/usr/bin/env python

import argparse


primer_dict = {
"R":["A","G"],
"Y":["C","T"],
"S":["G","C"],
"W":["A","T"],
"K":["G","T"],
"M":["A","C"],
"B":["C","G","T"],
"D":["A","G","T"],
"H":["A","C","T"],
"V":["A","C","G"],
"N":["A","T","C","G"],
".":[" "],
"-":[" "]
}
primer_string = list()
primer_list = list()
given_primer_list = list()
deg_primers_list = list()
seq_name_list = list()

parser = argparse.ArgumentParser(description='Hackathon2 Porter Primers')

parser.add_argument('-s','--input',help='input file',required=True)
parser.add_argument('-p','--primer',help='primers file',required=True)

args = vars(parser.parse_args())

#print "input given" + args['input']
#print "primer given" + args['primer']

with open(args['primer']) as my_input_file:
	content = my_input_file.readlines()
	for my_line in content:
		if(my_line.startswith('>')):
			continue
		else:
			#print "read primer " + my_line.strip()
			given_primer_list.append(my_line.strip())

my_seq_line_list = list()
my_seq_list = list()
with open(args['input']) as my_input_file:
	content = my_input_file.readlines()
	for my_line in content:
		if(my_line.startswith('>')):
			seq_name_list.append(my_line[1:].strip())
			#print my_line[1:]
			if(len(my_seq_line_list) > 0):
				my_seq_list.append(''.join(my_seq_line_list))
				my_seq_line_list = list()
		else:
			my_seq_line_list.append(my_line.strip())

my_seq_list.append(''.join(my_seq_line_list))

#print(my_seq_list)
#print(given_primer_list)
#print(len(my_seq_list))
#print(len(primer_list))
#print(len(list(set(my_seq_list))))
#print(len(primer_list))

#primer_string = primer_list
my_seq = my_seq_list

def explode(p_primer_string):
        found_count = 0
        for from_char in primer_dict:
                if (p_primer_string.find(from_char) != -1):
                        found_count = found_count + 1
        if ( found_count == 0 ):
                deg_primer_list.append(p_primer_string)
        else:
                for from_char in primer_dict:
                        if ( p_primer_string.find(from_char) != -1):
                                for to_char in primer_dict[from_char]:
                                        explode(p_primer_string.replace(from_char,to_char,1))

match_count_list = list()
match_count = 0
for my_primer_instance in given_primer_list:
	#print "Given primer is " + my_primer_instance
        deg_primer_list = list()
        explode(my_primer_instance)
	#print "deg primer is " + str(list(set(deg_primer_list)))

        seq_count = 0
	match_count = 0
        for my_seq_instance in my_seq:
                seq_count = seq_count + 1
                for my_primer in list(set(deg_primer_list)):
                        #print my_primer
                        match_pos = my_seq_instance.find(my_primer)
                        if (match_pos != -1):
                                print "found " + my_primer + " at position " + str(match_pos) + " for seq # " + str(seq_count) + " " + seq_name_list[seq_count-1]
				match_count = match_count + 1
	print "Sequence count is " + str(len(my_seq)) + ". Match count for given primer " + my_primer_instance + " across all its " + str(len(list(set(deg_primer_list)))) + " degenerates is " + str(match_count)

