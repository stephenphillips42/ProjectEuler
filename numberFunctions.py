import numpy as np
import listUtils

# Number theory stuff
def gcd(a,b):
	while not b == 0:
		a, b = b, a % b
	return a

def gcdl(lst):
	if len(lst) == 1:
		return lst[0]
	return gcd(lst[0],gcdl(lst[1:]))

def lcm(a,b):
	return (a*b)/gcd(a,b)

def lcml(lst):
	if len(lst) == 1:
		return lst[0]
	return lcm(lst[0],lcml(lst[1:]))

def egcd(a, b):
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	gcd = b
	return gcd, x, y

# Utility functions
def flip(N):
	M = 0
	while N > 0:
		M = M * 10 + N % 10;
		N = N / 10
	return M

def cumsum(N):
	return N*(N+1)/2

def sumofsquares(N):
	return N*(N+1)*(2*N+1)/6

# Problem specific functions
def ispalindrome(N):
	return N == flip(N)

def factorial(N):
	if N == 0:
		return 1
	p=1
	for i in xrange(1,N+1):
		p *= i
	return p

def base2(N):
	M = 0 # N in base 2
	k = 0 # Location we are at
	while N != 0:
		M = M + (10**k)*(N % 2)
		N /= 2
		k += 1
	return M

# modPow(b,k,N) is b^k (mod N)
def modPow(b,k,N):
	if k == 0:
		return 1
	elif k % 2 == 1:
		return (b*modPow(b,k-1,N)) % N
	else: # k % 2 == 0
		x = modPow(b,k//2,N)
		return (x*x) % N

# Thank you stack overflow
# Use Newton's/Hero's method to find
# the integer square root of an integer
def isqrt(N):
	x = N
	y = (x + 1) // 2
	while y < x:
		x = y
		y = (x + N // x) // 2
	return x

def isPerfectSquare(N):
	return N == (isqrt(N))**2

if __name__ == "__main__":
	pass

