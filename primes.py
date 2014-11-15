#/usr/bin/python

import random
from sets import Set
import math
import numberFunctions
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

def primes(k):
	return sieveEratosthenes(k)

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

def factorTrialDivision(N,verbose=False):
	factors = []
	bound = (N // 2) + 1
	norig = N
	i = 0
	checkup = N / 5
	for k in sieveEratosthenes(bound):
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
	assert listUtils.product(factors) == norig, (str(factors) + (", %d != %d" % (listUtils.product(factors), norig)))
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
	assert listUtils.product(factors) == norig, (str(factors) + (", %d != %d" % (listUtils.product(factors), norig)))
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

def numDivisors(N):
	factors = factorTrialDivision(numbers.cumsum(N))
	return listUtils.product(listUtils.addOne(listUtils.listCount(factors)))

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


