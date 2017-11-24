'''
10001st prime
Problem 7 

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
import time
from math import log10, floor

def round_sig(x, sig=4):
  """Round to significant figures."""
  return round(x, sig-int(floor(log10(abs(x))))-1)

start = time.time()

# Solution to problem.
count = 0
sieve = []

def is_prime(n, max_value=6000):
  if n <= 1:
    return False
    
  global sieve
  
  def brute_force(n):
    for i in range(1, n):
      if n % i == 0:
        return False
    return True
  
  def sieve_of_eratosthenes(n):
    global sieve
    for prime in sieve:
      if n % prime == 0:
        return False
    return True
  
  if n < max_value:
    if brute_force(n):
      sieve.append(n)
      return True
  else:
    if sieve_of_eratosthenes(n):
      return True
  return False

possible_prime = 0
while True:
  possible_prime += 1
  if is_prime(possible_prime):
    count += 1
  if count == 10001:
    break
  if possible_prime % 500 == 0:
    print(possible_prime, "numbers checked.", count, "primes found.")


elapsed = time.time() - start
print("The answer is %s." % count)
print("Solved in %s seconds." % round_sig(elapsed))
