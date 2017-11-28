'''10001st primeProblem 7 
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?'''import timefrom math import log10, floor
def round_sig(x, sig=4):  """Round to significant figures."""  return round(x, sig-int(floor(log10(abs(x))))-1)
start = time.time()
# Solution to problem.sieve = [2, 3]
count = 2while len(sieve) < 10001:  for prime in sieve:    if count % prime == 0:      break  else:    sieve.append(count)  count += 1  answer = sieve[-1]
elapsed = time.time() - startprint("The answer is %s." % count)print("Solved in %s seconds." % round_sig(elapsed))
