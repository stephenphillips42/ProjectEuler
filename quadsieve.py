import sys

def Q(x,n):
	sqrtn = math.floor(math.sqrt(n));
	return (x + sqrtn)**2 - n

def quadsieve(n):
	sqrtn = math.floor(math.sqrt(n))
	for k in xrange(1,n-sqrtn):
		r = sqrtn + k
		# if 

if len(sys.argv[0]) > 1:
	quadsieve(int(sys.argv[1]))
else:
	print "No input"
