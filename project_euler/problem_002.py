'''
Even Fibonacci numbers
Problem 2 

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

import time
from math import log10, floor


def round_sig(x, sig=4):
  """Round to significant figures."""
  return round(x, sig-int(floor(log10(abs(x))))-1)


start = time.time()

# Solution to problem.
answer = 0
fibonacci_sequence = [1, 2]
next_number = fibonacci_sequence[-2] + fibonacci_sequence[-1]

while next_number <= 4000000:
  fibonacci_sequence.append(next_number)
  if next_number % 2 == 0:
    answer += next_number
  next_number = fibonacci_sequence[-2] + fibonacci_sequence[-1]

elapsed = time.time() - start
print("The answer is %s." % answer)
print("Solved in %s seconds." % round_sig(elapsed))
