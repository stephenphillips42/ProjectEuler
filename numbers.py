import numpy as np

def gcd(a,b):
	while not b == 0:
		a, b = b, a % b
	return a

def egcd(a, b):
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	gcd = b
	return gcd, x, y

if __name__ == "__main__":
	pass

