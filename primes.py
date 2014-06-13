#/usr/bin/python

import random
from sets import Set
import math
import numbers
import listUtils

def naivesieve(k):
	A = [x for x in range(2,k)]
	p=2
	for j in xrange(k):
		A = [i for i in A if i % p != 0]
		A.append(p)
		p = A[0]
		if j % 1000 == 0:
			print j
	return sorted(A)

def sieveEratosthenes(k):
	# Create boolean array
	A = [ True for x in range(0,k) ]
	A[0] = A[1] = False # Simple cases
	for i in xrange(1+int(math.floor(math.sqrt(k)))):
		if A[i]:
			j = i**2
			while j < k:
				A[j] = False
				j = j + i
	return [ i for i in xrange(k) if A[i] == True ]

# Implement Pollard p-1 factorization
# modPow(b,k,N) is b^k (mod N)
def modPow(b,k,N):
	if k == 0:
		return 1
	elif k % 2 == 1:
		return (b*modPow(b,k-1,N)) % N
	else: # k % 2 == 0
		x = modPow(b,k//2,N)
		return (x*x) % N

def factorTrialDivision(n,verbose=False):
	factors = []
	sqrtN = 1+int(math.floor(math.sqrt(n)))
	i = 0
	checkup = n / 5
	for k in sieveEratosthenes(sqrtN):
		while n % k == 0:
			factors.append(k)
			n = n // k
		if verbose and i % (checkup) == 0:
			print "%d..." % k
		i = i+1
	return factors

def findFactors(n,verbose=False):
	if n < 10**7:
		return factorTrialDivision(n,verbose)
	print "Number too large for factoring"
	return []

def isprime(n):
	k = 9 # Confidence parameter
	for test in xrange(0,k):
		d = n - 1
		s = 1
		while d % 2 == 0:
			s += 1
			d /= 2
		a = random.randrange(2,n-1)
		x = a**d % n
		if x == 1 or x == n - 1:
			continue
		primebreak = False
		for i in xrange(0,s-1):
			x = x*x % n
			if x == 1:
				return False
			elif x == n - 1:
				primebreak = True
				break
		if not primebreak:
			return False
	return True

def numDivisors(N):
	factors = factorTrialDivision(numbers.cumsum(x))
	return listUtils.product(listUtils.addOne(listUtils.listCount(factors)))

if __name__ == "__main__":
	import sys
	if len(sys.argv) > 1:
		import time
		start = time.clock()
		sieveEratosthenes(int(sys.argv[1]))
		end = time.clock()
		print end - start
	print factorTrialDivision(600851475143)
	pass


