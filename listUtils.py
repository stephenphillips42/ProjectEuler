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

# Thank you stack overflow
def permute(xs, low=0):
	if low + 1 >= len(xs):
		yield xs
	else: # Do lots of swapping
		for p in permute(xs, low + 1):
			yield p        
		for i in range(low + 1, len(xs)):        
			xs[low], xs[i] = xs[i], xs[low]
			for p in permute(xs, low + 1):
				yield p        
			xs[low], xs[i] = xs[i], xs[low]

def toNum(lst):
	return int(''.join(map(str,lst)))

def allSame(lst):
	v = lst[0]
	for i in xrange(1,len(lst)):
		if lst[i] != v:
			return False
	return True

if __name__ == "__main__":
	pass

