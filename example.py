import sys

#1. get the list of arguments
words=sys.argv[1:]
#2. sort them
words.sort()



#3. join all of the words except the last one with a comma
l=len(words)
#count on the other way around ignoring the first entry with [0:-1]

sentence =','.join(words[0:-1])



#4. capitalize the first letter]
#5. append the word "and" and the final word, and a period
sentence +=',and '+words[-1]+'.'

#6. print the result
print sentence[0].upper() + sentence[1:]
