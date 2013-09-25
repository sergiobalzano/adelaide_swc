pitching=open ('pitching.csv','r')
line=pitching.readline()
search_me= 'IPOuts'
search_me_index=0
header_values=line.split(',')
for header in header_values:
 if search_me == header:
  break
 search_me_index +=1

line=pitching.readline()

line_counts=0
total_ipouts=0
while line != '':
 row = line.split(',')
 value= row[12]
 total_ipouts += float(value)
 line_counts += 1
 line= pitching.readline()
print 'total ipouts: ' + str(total_ipouts)
print 'line count ' + str(line_counts)
print 'total average (IPOuts): ' + str(total_average)


