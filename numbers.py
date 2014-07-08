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

if __name__ == "__main__":
	pass

