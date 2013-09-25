

input_string='proviamo questo Cazzo di python come funziona'
input_string=input_string.replace(' ','')
input_string=input_string.replace(',','')
set(input_string.upper())

l=len(set(input_string.upper()))
print set(input_string.upper())
print l
