test = [
    ['gtcagtc', {'G':2, 'T':2, 'C':2, 'A':1}],
    ['gtagt', {'G':2, 'T':2, 'A':1}],
    ['GTCNGAT', {'G': 2, 'T':2, 'C':1,'A':1}]
]

class UnknownbaseException(Exception):
 pass     

def nucleotideContent(dnaString):    
'''This function must return the contribution    
of nucleotides ATCG (as uppercase) from a given DNA     
string inside a dictionary, where each key refers to    
a nucleotide 
'''

    dnaString=dnaString.upper()
    dnaDict = {}    
    uniques=uniques.intersection(set('ACTG'))
   
for nucleotide in uniques:    
dnaDict[nucleotide]=dnaString.count(nucleotide)    
    
return dnaDict
# Run and report    
passes = 0    
for (i, (seq, expected)) in enumerate(Tests):    
  if nucleotideContent(seq) == expected:    
    passes += 1    
else:    
  print('test %d failed' % i)    
    
print('%d/%d tests passed' % (passes, len(Tests)))

