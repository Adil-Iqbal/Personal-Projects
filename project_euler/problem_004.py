'''Largest palindrome productProblem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.'''
import timefrom math import log10, floor
def round_sig(x, sig=4):  """Round to significant figures."""  return round(x, sig-int(floor(log10(abs(x))))-1)
start = time.time()
# Solution to problem.def is_palindrome(n):  return str(n) == str(n)[::-1]
answer = 0for i in reversed(range(100, 1000)):  for j in reversed(range(100, 1000)):    if is_palindrome(i * j) and (i * j) > answer:      answer = i * j      elapsed = time.time() - startprint("The answer is %s." % answer)print("Solved in %s seconds." % round_sig(elapsed))
