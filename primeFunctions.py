#/usr/bin/python

import random
from sets import Set
import math
import numberFunctions as nf
import listUtils as lu

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
	if k < 2:
		return []
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

# Returns primes less than or equal to k
def primes(k):
	return sieveEratosthenes(k)

# Implement Pollard p-1 factorization

def factorTrialDivision(N,primeList=None,verbose=False):
	factors = []
	if primeList == None:
		bound = (N // 2) + 1
		primeList = sieveEratosthenes(bound)
	norig = N # Original N for latter verification
	i = 0
	checkup = N / 5
	for k in primeList:
		while N % k == 0:
			factors.append(k)
			N = N // k
		if N == 1:
			break
		if verbose and i % (checkup) == 0:
			print "%d..." % k
		i = i+1
	if len(factors) == 0:
		factors.append(N)
	assert lu.product(factors) == norig, (str(factors) + (", %d != %d" % (lu.product(factors), norig)))
	return factors

def findFactors(N,verbose=False):
	if N < 10**7:
		return factorTrialDivision(N,verbose)
	print "Number too large for factoring"
	return []

def findFactorsPairs(N):
	factors = []
	bound = (N // 2) + 1
	norig = N
	checkup = N / 5
	for k in sieveEratosthenes(bound):
		j = 0
		while N % k == 0:
			j += 1
			N = N // k
		if j > 0:
			factors.append((k,j))
		if N == 1:
			break
	if len(factors) == 0:
		factors.append(N)
	assert lu.product(factors) == norig, (str(factors) + (", %d != %d" % (lu.product(factors), norig)))
	return factors

def isPrime(N):
	B = 1+int(math.sqrt(N))
	if N < 100:
		B = N
	for i in xrange(2,B):
		if N % i == 0:
			return False
	return True

def isPrimeFast(N):
	if k % 2 == 0:
		return False
	k = 9 # Confidence parameter
	for test in xrange(0,k):
		d = N - 1
		s = 1
		while d % 2 == 0:
			s += 1
			d /= 2
		a = random.randrange(2,N-1)
		x = a**d % N
		if x == 1 or x == N - 1:
			continue
		primebreak = False
		for i in xrange(0,s-1):
			x = x*x % N
			if x == 1:
				return False
			elif x == N - 1:
				primebreak = True
				break
		if not primebreak:
			return False
	return True

# The math is complicated and beautiful
# Refer to: http://www.math.mit.edu/phase2/UJM/vol1/DORSEY-F.PDF
# Really good primality test
def isPrimeFermat(N):
	if N % 2 == 0:
		return False
	s = 0
	d = N-1
	while d % 2 == 0:
		s += 1
		d = d // 2
	# Now we have N = 1 + 2**s * d
	for test in xrange(1,25):
		a = random.randint(1, N-1)
		# Using modPow is ESSENTIAL (otherwise we get MASSIVE numbers)
		if nf.modPow(a,d,N) != 1: # Did not pass first test
			passed = False
			for j in xrange(s):
				if nf.modPow(a,d * (2**j),N) == N - 1:
					passed = True
			if not passed:
				return False
	return True



def numDivisors(N):
	factors = factorTrialDivision(N)
	return lu.product(lu.addOne(lu.listCount(factors)))

def trialDivisionDivisors(N):
	divisors = []
	sqrtN = int(math.ceil(N/2))+1
	for i in xrange(1,sqrtN):
		if N % i == 0:
			divisors.append(i)
	return divisors

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


