'''
Sum square difference
Problem 6 

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
import time
from math import log10, floor

def round_sig(x, sig=4):
  """Round to significant figures."""
  return round(x, sig-int(floor(log10(abs(x))))-1)

start = time.time()

# Solution to problem.
numbers = 100
sum_of_squares = 0
square_of_sums = 0

for i in range(1, numbers + 1):
  sum_of_squares += i * i
  square_of_sums += i
square_of_sums *= square_of_sums

answer = abs(sum_of_squares - square_of_sums)

elapsed = time.time() - start
print("The answer is %s." % answer)
print("Solved in %s seconds." % round_sig(elapsed))
