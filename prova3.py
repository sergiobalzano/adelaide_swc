import sys

my_list=sys.argv

my_list.sort()

l=len(my_list)-1

my_list_short=my_list[0:l]

my_list_short[0]=my_list_short[0].title()
new_list=my_list_short.append('and')
new_list.append(l)

