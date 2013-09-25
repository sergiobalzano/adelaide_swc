#Exercise 3:
#input_string = "GATCAGTCGATCGACTGCTAGCTAGCTAGTACGGCGTATA"
#create a dictionary in the following format:
#{'G': (# of occurences in the string),
#'A': ...
#}
#print the dictionary
#dna_dict

input_string = "GATCAGTCGATCGACTGCTAGCTAGCTAGTACGGCGTATA"
no_A=input_string.count('A')
no_C=input_string.count('C')
no_G=input_string.count('G')
no_T=input_string.count('T')
dictionary={'A':no_A,'C':no_C,'G':no_G,'T':no_T}
print dictionary
print float(dictionary['G']+dictionary['C'])/len(input_string)

