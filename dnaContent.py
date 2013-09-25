def nucleotideContent(dnaString):    
#This function must return the contribution    
#of nucleotides ATCG (as uppercase) from a given DNA     
#string inside a dictionary, where each key refers to    
#a nucleotide    
    
 dnaDict = {}    
uniques=set(dnaString)    
for nucleotide in uniques:    
 dnaDict[nucleotide]=dnaString.count(nucleotide)     
return dnaDict
# Run and report    
passes = 0    
for (i, (seq, expected)) in enumerate(Test):    
 if nucleotideContent(seq) == expected:    
  passes += 1    
 else:    
  print('test %d failed' % i)    
    
print('%d/%d tests passed' % (passes, len(test)))

test=[
 ['gtcagtc',{'G':2,'T':2,'C':2,'A':2}]
['ACTGHR',{}],['gtcagt',{'G':2,'C':0,'A':2}]]
