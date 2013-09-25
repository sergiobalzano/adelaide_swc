def factorial(n):
# return the factorial of n, an integer >=0

# >>> do like we are inside python
# >>> factorial(4)
# 24
 import math
 if not n >=0:
  raise ValueError('n must be >= 0')
# if the number is not an integer
 if math.floor(n) !=0:
  raise ValueError('n must be integer')
 result= 1
 factor= 2
 while factor <= n:
  result *= factor
  factor += 1
 return result

if __name__=='__main__':
 import doctest
 doctest.testmod()

# when nothing is returned it means that the test worked


