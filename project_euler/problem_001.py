'''
Multiples of 3 and 5
Problem 1 

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

import time
from math import log10, floor

start = time.time()

def round_sig(x, sig=4):
  return round(x, sig-int(floor(log10(abs(x))))-1)

answer = 0
for number in range(1000):
  if number % 3 ==0 or number % 5 == 0:
    answer += number

elapsed = time.time() - start
print("The answer is %s." % answer)
print("Solved in %s seconds." % round_sig(elapsed))
