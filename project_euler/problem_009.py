'''
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import time
from math import log10, floor, sqrt

def round_sig(x, sig=4):
  """Round to significant figures."""
  return round(x, sig-int(floor(log10(abs(x))))-1)

start = time.time()

# Solution to problem.
answer = 0

for a in range(1, 1000):
  for b in range(1, 1000-a):
    c = 1000 - a - b
    if (a * a) + (b * b) == (c * c):
      answer = a * b * c

elapsed = time.time() - start
print("The answer is %s." % answer)
print("Solved in %s seconds." % round_sig(elapsed))
