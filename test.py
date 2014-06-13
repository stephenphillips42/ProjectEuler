#/usr/bin/python

import sys
import math
import numbers
import primes
import listUtils

# I did not come up with this. All the recursive relations I came
# up with were wrong
def latticeCount(N):
	# Grid of size n gives corners of (n+1)x(n+1)
	a = [ [ 0 for x in xrange(N+1) ] for x in xrange(N+1) ]
	# Initialization
	for i in xrange(N+1):
		a[0][i] = a[i][0] = 1

	# Counting
	for r in xrange(1,N+1):
		for c in xrange(1,N+1):
			a[r][c] = a[r-1][c] + a[r][c-1]
	
	return a[N][N]


if __name__ == '__main__':
	print "Test"
	N = 20
	print latticeCount(20)
 