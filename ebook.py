#1) Read the contents of the file pg76.txt
#2) get the length of each line and sum the lines as you go
#3) count the total number of lines in the file

# read the content of the file
reader=open('ebook.txt','r')
# get the first line
line=reader.readline()
# declare some variables for our length and line count
total_length=0
line_count=0

# read the rest of the file 
# get the length of each line and aggregate it
# get the total number of lines in a file

while line !='':
 total_length += len(line)
 line_count +=1
 line.reader.readline()
reader.close()



print length



