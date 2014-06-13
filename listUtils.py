# List utilities

def product(lst):
	p = 1
	for i in xrange(len(lst)):
		p *= lst[i]
	return p

def listCount(lst):
	l = sorted(lst)
	numels = [1]
	for i in xrange(1,len(lst)):
		if l[i] == l[i-1]:
			numels[-1] += 1
		else:
			numels.append(1)
	return numels

def addOne(lst):
	l = lst
	for i in xrange(len(lst)):
		l[i] += 1
	return l

if __name__ == "__main__":
	pass

