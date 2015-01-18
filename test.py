#/usr/bin/python

# Basic imports
import sys
import math
import random

# My imports
import numberFunctions as nf
import primeFunctions as pf
import listUtils as lu
import constants as const
import largeconstants

# Extra imports
from collections import Counter # Basically a multiset
import itertools

# Timing stuff
import time




if __name__ == '__main__':
	starttime = time.clock()
	print "Test" 






	# Simulate the spiral after 49
	n = 49
	sidelen = 7
	diagPrimes = 8
	total = 13
	while diagPrimes / float(total) > 0.1:
		sidelen += 2
		for i in xrange(4):
			n += sidelen-1
			if pf.isPrimeFermat(n):
				diagPrimes += 1
		total += 4
		assert nf.isPerfectSquare(n)
		print "\rPercentage: %f%%" % (diagPrimes / float(total) ),
	print ""
	print sidelen

























	print "Time elapsed: %f" % (time.clock() - starttime)









