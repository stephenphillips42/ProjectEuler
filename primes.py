#/usr/bin/python

import random
from sets import Set
import math
import numbers

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

def factorTrialDivision(n):
	factors = []
	sqrtN = 1+int(math.floor(math.sqrt(n)))
	i = 0
	checkup = n / 5
	for k in sieveEratosthenes(sqrtN):
		if n % k == 0:
			factors.append(k)
			n = n // k
		if i % (checkup) == 0:
			print "%d..." % k
		i = i+1
	return factors

def findFactors(n):
	if n < 1000:
		return factorTrialDivision(n)
	print "Number too large for factoring"
	return []





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

