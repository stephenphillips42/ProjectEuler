#/usr/bin/python

import sys
import math
import numberFunctions as nf
import primes
import listUtils
import largeconstants

problem = 0
if len(sys.argv) > 1:
	problem = int(sys.argv[1])

#####################################################################
# Problem 4
if problem == 4:
	for x in xrange(899,1000):
		for y in xrange(899,1000):
			if nf.ispalindrome(x*y):
				maxx = x
				maxy = y
	print "Maximum:"
	print maxx*maxy

#####################################################################
# Problem 5
if problem == 5:
	print "Did this by hand"

#####################################################################
# Problem 6
if problem == 6:
	print (cumsum(100))**2 - sumofsquares(100)

#####################################################################
# Problem 7
def maxprime(N):
	# Create boolean array
	A = [ True for x in range(0,N) ]
	A[0] = A[1] = False # Simple cases
	maxp = 0
	primecount = 0
	for i in xrange(1+int(math.floor(math.sqrt(N)))):
		if A[i]:
			j = i**2
			while j < N:
				A[j] = False
				j = j + i
			maxp = i
			primecount = primecount + 1
	return maxp, primecount

# Note: 3137 is the 446th prime
def findnthprime():
	count = 446
	x = 3137
	progress = 1503
	lastprime = x
	while x < 10**7:
		if primes.isPrimeFast(x):
			count += 1
			lastprime = x
			if count == 10001:
				print "FOUND IT"
				print (x, count)
				return
		if x % progress == 0:
			print (lastprime,count)
		x += 2
# Best solution
if problem == 7:
	primelist = primes.sieveEratosthenes(2*10**6)
	l = len(primelist)
	if l > 10001:
		print "We got it!!"
		print primelist[10000]
	print l
	print primelist[l-1] 

#####################################################################
# Problem 8

def maxprod(nums,k):
	prod = 1
	for i in xrange(k):
		prod = nums[i]
	m = prod
	i = 0
	mi = i
	while i < len(nums) - k:
		if i + k > len(nums):
			break
		# handling zero case
		if nums[i+k] == 0:
			zeropos = i+k
			atzero = True
			while atzero:
				# print "zero"
				prod = 1
				success = True
				for j in xrange(1,k+1):
					if len(nums) <= zeropos+j:
						return (m, mi)
					if nums[zeropos+j] == 0:
						success = False
						zeropos = zeropos+j
						break
					prod *= nums[zeropos+j]
				if success:
					atzero = False
			i = zeropos+1
			if prod > m:
				m = prod
				mi = i
			continue
		else:
			# print "no zero %f" % prod
			prod /= nums[i]
			prod *= nums[i+k]
			i += 1
			if prod > m:
				m = prod
				mi = i

	return (m,mi)

if problem == 8:
	print maxprod(largeconstants.num1000Digits,13)[0]

#####################################################################
# Problem 9
if problem == 9:
	for x in xrange(1,1000):
		for y in xrange(1,x):
			if 500000 - 1000*x - 1000*y + x*y == 0:
				a = x
				b = y
				c = 1000 - a - b
	print "%d^2 + %d^2 = %d^2" % (a, b, c)
	print "%d + %d = %d, %d" % (a**2, b**2, a**2 + b**2, c**2)
	print a*b*c

#####################################################################
# Problem 10
if problem == 10:
	primelist = primes.sieveEratosthenes(2*10**6)
	print sum(primelist)

#####################################################################
# Problem 11

if problem == 11:
	A = largeconstants.grid20x20
	maxprod = 0
	for r in xrange(len(A)):
		for c in xrange(len(A[0])-3):
			prod = 1
			for i in xrange(4):
				prod *= (A[r][c+i])
			if prod > maxprod:
				maxprod = prod
	for r in xrange(len(A)-3):
		for c in xrange(len(A[0])):
			prod = 1
			for i in xrange(4):
				prod *= (A[r+i][c])
			if prod > maxprod:
				maxprod = prod
	for r in xrange(len(A)-3):
		for c in xrange(len(A[0])-3):
			prod = 1
			for i in xrange(4):
				prod *= (A[r+i][c+i])
			if prod > maxprod:
				maxprod = prod
	for r in xrange(len(A)-3):
		for c in xrange(3,len(A[0])):
			prod = 1
			for i in xrange(4):
				prod *= (A[r+i][c-i])
			if prod > maxprod:
				maxprod = prod
	print maxprod

#####################################################################
# Problem 12
if problem == 12:
	for x in xrange(9,50000):
		numdiv = primes.numDivisors(nf.cumsum(x))
		if (numdiv) >= 500:
			print x
			print nf.cumsum(x)
			print numdiv
			break

#####################################################################
# Problem 13
# OK I cheated... thank you big number library of python
if problem == 13:
	s = 0L
	for i in xrange(len(largeconstants.numList100Digits)):
		s += (largeconstants.numList100Digits[i])
	print s

#####################################################################
# Problem 14
def collatz(N):
	a = N
	count = 0
	while a > 1:
		if a % 2 == 0:
			a = a // 2
		else:
			a = 3*a + 1
		count += 1
	return count

if problem == 14:
	cmax = 0
	cmaxval = 1
	for i in xrange(1,10**6+1):
		c = collatz(i)
		if c > cmax:
			cmax = c
			cmaxval = i
	print cmax
	print cmaxval

#####################################################################
# Problem 15
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

if problem == 12:
	print latticeCount(20)

#####################################################################
# Problem 16
if problem == 16:
	L = 2**1000
	s = 0
	for i in xrange(302):
		s = s + (L % 10)
		L = L // 10
	print s

#####################################################################
# Problem 17
def digitsToLetters(d):
	assert 0 <= d <= 1000
	if d == 0:
		return 'zero'
	elif d == 1:
		return 'one'
	elif d == 2:
		return 'two'
	elif d == 3:
		return 'three'
	elif d == 4:
		return 'four'
	elif d == 5:
		return 'five'
	elif d == 6:
		return 'six'
	elif d == 7:
		return 'seven'
	elif d == 8:
		return 'eight'
	elif d == 9:
		return 'nine'
	elif d == 10:
		return 'ten'
	elif d == 11:
		return 'eleven'
	elif d == 12:
		return 'twelve'
	elif d == 13:
		return 'thirteen'
	elif d == 14:
		return 'fourteen'
	elif d == 15:
		return 'fifteen'
	elif d == 16:
		return 'sixteen'
	elif d == 17:
		return 'seventeen'
	elif d == 18:
		return 'eighteen'
	elif d == 19:
		return 'nineteen'
	elif d == 20:
		return 'twenty'
	elif 20 < d < 30:
		return 'twenty ' + digitsToLetters(d % 10)
	elif d == 30:
		return 'thirty'
	elif 30 < d < 40:
		return 'thirty ' + digitsToLetters(d % 10)
	elif d == 40:
		return 'forty'
	elif 40 < d < 50:
		return 'forty ' + digitsToLetters(d % 10)
	elif d == 50:
		return 'fifty'
	elif 50 < d < 60:
		return 'fifty ' + digitsToLetters(d % 10)
	elif d == 60:
		return 'sixty'
	elif 60 < d < 70:
		return 'sixty ' + digitsToLetters(d % 10)
	elif d == 70:
		return 'seventy'
	elif 70 < d < 80:
		return 'seventy ' + digitsToLetters(d % 10)
	elif d == 80:
		return 'eighty'
	elif 80 < d < 90:
		return 'eighty ' + digitsToLetters(d % 10)
	elif d == 90:
		return 'ninety'
	elif 90 < d < 100:
		return 'ninety ' + digitsToLetters(d % 10)
	elif d < 1000 and d % 100 == 0:
		return digitsToLetters(d // 100) + ' hundred'
	elif d < 1000:
		return digitsToLetters(d // 100) + ' hundred and ' + digitsToLetters(d % 100)
	elif d == 1000:
		return 'one thousand'
	else:
		return ''

if problem == 17:
	l = 0
	for i in xrange(1,1001):
		l += len(digitsToLetters(i).replace(' ',''))
	print l


#####################################################################
# Problem 18 AND 67
# YEAH DYNAMIC PROGRAMMING
def dftMaxPathHelper(T,Cache,d,x):
	if d == len(T):
		return 0
	if Cache[d][x] >= 0:
		return Cache[d][x]
	Cache[d][x] = T[d][x]+max(dftMaxPathHelper(T,Cache,d+1,x),dftMaxPathHelper(T,Cache,d+1,x+1))
	return Cache[d][x]

def dftMaxPath(T,Cache):
	return dftMaxPathHelper(T,Cache,0,0)

if problem == 18:
	T = largeconstants.pathTriangle
	Cache = [ [ -1 for x in xrange(len(T)) ] for x in xrange(len(T)) ]
	print dftMaxPath(T,Cache)

if problem == 67:
	Tbig = largeconstants.pathTriangleBig
	CacheBig = [ [ -1 for x in xrange(len(Tbig)) ] for x in xrange(len(Tbig)) ]
	print dftMaxPath(Tbig,CacheBig)


#####################################################################
# Problem 19
regYearMonthDays = [
  31, # January
	28, # February
	31, # March
	30, # April
	31, # May
	30, # June
	31, # July
	31, # August
	30, # September
	31, # October
	30, # November
	31 # December
 ]
leapYearMonthDays = [
  31, # January
	29, # February
	31, # March
	30, # April
	31, # May
	30, # June
	31, # July
	31, # August
	30, # September
	31, # October
	30, # November
	31 # December
 ]

monthDays = [ regYearMonthDays, leapYearMonthDays ]

# Monday = 0, Tuesday = 1, Wednesday = 2, Thursday = 3, Friday = 4, Saturday = 5, Sunday = 6

def isLeapYear(year):
	return (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0)

if problem == 19:
	weekday = 0 # On monday
	sundays = 0
	for year in xrange(1900,2001):
		leapYear = 0
		if isLeapYear(year):
			leapYear = 1
		for month in xrange(12):
			if (weekday+sum(monthDays[leapYear][0:(month+1)])) % 7 == 6:
				sundays += 1
		weekday = (weekday + sum(monthDays[leapYear])) % 7

	year = 1900
	for month in xrange(12):
		if sum(monthDays[0][0:(month+1)]) % 7 == 6:
			sundays -= 1
	print sundays


#####################################################################
# Problem 20
if problem == 20:
	Total = 1
	for i in xrange(100):
		Total *= (i+1)
	print Total
	digitsum = 0
	while Total > 0:
		digitsum += Total % 10
		Total = Total // 10
	print digitsum


#####################################################################
# Problem 21
def getDivisorsCached(N,Cache):
	if not N in Cache:
		Cache[N] = primes.trialDivisionDivisors(x)
	return Cache[N]
if problem == 21:
	Cache = {}
	amicable = []
	for x in xrange(1,10000):
		if x % 100 == 0:
			print x
		for y in xrange(1,x+1):
			xdivisors = getDivisorsCached(x,Cache)
			ydivisors = getDivisorsCached(y,Cache)
			if x == sum(ydivisors) and y == sum(xdivisors):
				print "found one %d %d" % (x,y)
				if not y == x:
					amicable.append(x)
					amicable.append(y)
	print amicable
	print sum(amicable)

#####################################################################
# Problem 22
alphaNum = {
	"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,
	"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26
	}
def getScore(name):
	score = 0
	for x in name:
		score += alphaNum[x]
	return score

if problem == 22:
	SortedNamesList = sorted(largeconstants.NamesList)
	t = 0
	for i in xrange(len(largeconstants.NamesList)):
		t += (i+1) * getScore(SortedNamesList[i])
	print t 

#####################################################################
# Problem 23
def getnfTypes(Upper):
	abundant = []
	perfect = []
	deficient = []
	for i in xrange(Upper):
		if i % 100 == 0:
			sys.stdout.write(".")
			sys.stdout.flush()
		if i % 1000 == 0:
			print i
		s = sum(primes.trialDivisionDivisors(i))
		if i < s:
			abundant.append(i)
		elif i == s:
			perfect.append(i)
		else:
			deficient.append(i)

	print "Done"
	return abundant, perfect, deficient

if problem == 23:
	Upper = 28123
	abundant, perfect, deficient = getnfTypes(Upper)
	nums = set()
	for x in abundant:
		for y in abundant:
			nums.add(x+y)
	underNums = set([ x for x in xrange(1,Upper)])
	nonAbundantSums = underNums.difference(nums)
	print sum(list(nonAbundantSums))

#####################################################################
# Problem 24
global permutationstep
permutationstep = 1
global permutationdone
permutationdone = False

def permuteAll(perm,used):
	global permutationstep
	global permutationdone
	if permutationdone == True:
		return
	next = [ x for x in xrange(len(used)) if used[x] == False ]
	if len(next) == 0:
		if permutationstep == 10**6:
			print "FINAL:"
			print perm
			permutationdone = True
		permutationstep += 1
		return
	for i in next:
		used[i] = True
		perm.append(i)
		permuteAll(perm,used)
		used[i] = False
		perm.pop()

# print '0123456789'
# print "Permutation 10000"
# print "10*9*8*7*6*5*4*3*2*1=%d" % (10*9*8*7*6*5*4*3*2*1)
# print "-----------"
# print "2*9*8*7*6*5*4*3*2*1=%d < 1000000 < %d=3*9*8*7*6*5*4*3*2*1" % (2*9*8*7*6*5*4*3*2*1, 3*9*8*7*6*5*4*3*2*1)
# print "1000000-2*9*8*7*6*5*4*3*2*1=%d" % (1000000-2*9*8*7*6*5*4*3*2*1)
# print '2, 023456789'
# print "-----------"
# print "6*8*7*6*5*4*3*2*1=%d < 274240 < %d=7*8*7*6*5*4*3*2*1" % (6*8*7*6*5*4*3*2*1, 7*8*7*6*5*4*3*2*1)
# print "274240-6*8*7*6*5*4*3*2*1=%d" % (274240-6*8*7*6*5*4*3*2*1)
# print '27, 02345789'
# print "-----------"
# print "6*7*6*5*4*3*2*1=%d < 32320 < %d=7*7*6*5*4*3*2*1" % (6*7*6*5*4*3*2*1, 7*7*6*5*4*3*2*1)
# print "32320-6*7*6*5*4*3*2*1=%d" % (32320-6*7*6*5*4*3*2*1)
# print '278, 0234589'
# print "-----------"
# print "2*6*5*4*3*2*1=%d < 2080 < %d=3*6*5*4*3*2*1" % (2*6*5*4*3*2*1, 3*6*5*4*3*2*1)
# print "2080-2*6*5*4*3*2*1=%d" % (2080-2*6*5*4*3*2*1)
# print '2783, 034589'
# print "-----------"
# print "5*5*4*3*2*1=%d < 640 < %d=6*5*4*3*2*1" % (5*5*4*3*2*1, 6*5*4*3*2*1)
# print "640-5*5*4*3*2*1=%d" % (640-5*5*4*3*2*1)
# print '27839, 03459'
# print "-----------"
# print "1*4*3*2*1=%d < 40 < %d=2*4*3*2*1" % (1*4*3*2*1, 2*4*3*2*1)
# print "40-1*4*3*2*1=%d" % (40-1*4*3*2*1)
# print '278391, 3459'
# print "-----------"
# print "2*3*2*1=%d < 16 < %d=3*3*2*1" % (2*3*2*1, 3*3*2*1)
# print "16-2*3*2*1=%d" % (16-2*3*2*1)
# print '2783915, 046'
# print "-----------"
# print "2*2*1=%d <= 4 < %d=3*2*1" % (2*2*1, 3*2*1)
# print "4-2*2*1=%d" % (4-2*2*1) # 0
# print '2783915460'

if problem == 24:
	# Brute Force Through the rotations
	perm = [  ]
	used = [ False for x in xrange(10) ]
	permuteAll([],used)

#####################################################################
# Problem 25
def fastfibonacci(N):
	f1 = 1
	f2 = 1
	for x in xrange(1,N):
		f1, f2 = f2, (f1 + f2)
	return f1

if problem == 25:
	fl = 1
	while True:
		F = fastfibonacci(fl)
		l = 0
		while F > 0:
			F = F // 10
			l += 1
		if l >= 1000:
			break
		fl += 1
	print fl
	print fastfibonacci(fl)

#####################################################################
# Problem 26
def repDecLength(N):
	if nf.gcd(N,10) != 1:
		return -1
	for i in xrange(1,N):
		if 10**i % N == 1:
			return i

if problem == 26:
	m = 0
	mi = 0
	for i in xrange(3,1000,2):
		if i % 5 == 0:
			continue
		repDecLen = repDecLength(i)
		print "%d : %d" % (i, repDecLen)
		if repDecLen > m:
			m = repDecLen
			mi = i
	print m
	print mi


#####################################################################
# Problem 27
def p(n,a,b):
	return n**2 + a*n + b

# assumes P is a list of primes, pi index for that list
def testQuadratic(pi, P):
	b = P[pi]
	m = 0
	ma = -1
	for a in xrange(-1000,1001):
		n = 0
		while p(n,a,b) > 0 and primes.isPrime(p(n,a,b)):
			n += 1
		if n > m:
			m = n
			ma = a
	return (m,ma)

if problem == 27:
	m = 0
	a = 0
	b = 0
	primelist = primes.primes(1000)
	for pi in xrange(len(primelist)):
		l, tmpA = testQuadratic(pi,primelist)
		if l > m:
			m = l
			a = tmpA
			b = primelist[pi]
			print a, b, l
	print "-----------"
	print a,b,m
	print a*b


#####################################################################
# Problem 28
if problem == 28:
	S = 1001
	i = 1
	s = 0
	while (2*i+1) <= S:
		s += (2*i+1)**2
		s += (2*i+1)**2-2*i
		s += (2*i+1)**2-4*i
		s += (2*i+1)**2-6*i
		i += 1
	print s+1


#####################################################################
# Problem 29
if problem == 29:
	terms = set([])
	for a in xrange(2,101):
		for b in xrange(2,101):
			terms.add(a**b)
	print len(terms)


#####################################################################
# Problem 30
if problem == 30:
	# Graciously given by The Online Encylopedia of Integer Sequences 
	# (http://oeis.org/A052464/list)
	# 0 and 1 not included because they are not sums
	print sum([4150,4151,54748,92727,93084,194979])


#####################################################################
# Problem 31
if problem == 31:
	coins = [1, 2, 5, 10, 20, 50, 100, 200]
	W = 200;
	C = len(coins);
	OPT = [ [-1 for x in xrange(0,C) ] for x in xrange(0,(W+1)) ] ;

	# Dynamic Program
	# coins is the list of length C of our coin types
	# OPT[i][j] = number of ways to make i pence using coins less than or equal to j pence
	# OPT[i][j] = sum_{k : k \le j, i - coins[k] \ge 0} OPT[i-coins[k],k]
	# Initializations
	for j in xrange(0,C):
		OPT[0][j] = 1;
	for i in xrange(0,W+1):
		OPT[i][0] = 1;

	for i in xrange(1,W+1):
		for j in xrange(1,C):
			s = 0
			for k in xrange(0,j+1):
				if (i - coins[k]) >= 0:
					s += OPT[i-coins[k]][k]
			OPT[i][j] = s;

	print OPT[W][C-1]
	# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in OPT]))



#####################################################################
# Problem 32
if problem == 32:
	from collections import Counter
	# Finding pan-digital products
	# Upper bound for the products: 2000 (why?)
	digits = Counter({1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1}) # Set we are comparing to
	panDigitalProds = set([])
	for y in xrange(0,2000):
		y_digits = Counter([])
		for dig in str(y):
			y_digits[int(dig)] += 1
		for x in xrange(0,y+1):
			these_digits = y_digits.copy()
			for dig in str(x):
				these_digits[int(dig)] += 1;
			# print (x,y,x*y)
			# print digits
			# print these_digits
			for dig in str(x*y):
				these_digits[int(dig)] += 1;
			if these_digits == digits:
				panDigitalProds.add((x,y,x*y))
				print (x,y,x*y)	

	print panDigitalProds
	panDigitalSum = 0
	uniquePanDigitalProds = set([x[2] for x in panDigitalProds])
	for panDigitalProd in uniquePanDigitalProds:
		panDigitalSum += panDigitalProd
	print panDigitalSum

#####################################################################
# Problem 33
if problem == 33:
	from fractions import Fraction

	specialFractions = []
	for num in xrange(10,100):
		for denom in xrange(num+1,100):
			s_num = str(num)
			s_denom = str(denom)
			if int(s_num[0]) == int(s_denom[0]) \
					and int(s_num[0]) != 0 \
					and int(s_denom[1]) != 0 \
					and Fraction(int(s_num[1]),int(s_denom[1])) == Fraction(num,denom):
				specialFractions.append((num,denom))
			if int(s_num[0]) == int(s_denom[1]) \
					and int(s_num[0]) != 0 \
					and int(s_denom[0]) != 0 \
					and Fraction(int(s_num[1]),int(s_denom[0])) == Fraction(num,denom):
				specialFractions.append((num,denom))
			if int(s_num[1]) == int(s_denom[0]) \
					and int(s_num[1]) != 0 \
					and int(s_denom[1]) != 0 \
					and Fraction(int(s_num[0]),int(s_denom[1])) == Fraction(num,denom):
				specialFractions.append((num,denom))
			if int(s_num[1]) == int(s_denom[1]) \
					and int(s_num[1]) != 0 \
					and int(s_denom[0]) != 0 \
					and Fraction(int(s_num[0]),int(s_denom[0])) == Fraction(num,denom):
				specialFractions.append((num,denom))
	p = Fraction(1)
	for x in specialFractions:
		p *= Fraction(x[0],x[1])
	print p.denominator



#####################################################################
# Problem 34
if problem == 34:
	# Upper bound on these:
	# 8*(9!) = 2903040 which has 7 digits, meaning that the number must have
	# 7 digits or less. The max of 7 digits we can reach is 7*(9!) = 2540160
	digitFactorials = []
	for N in xrange(3,2540160):
		if sum([ nf.factorial(int(x)) for x in str(N)]) == N:
			digitFactorials.append(N)

	print sum(digitFactorials)


#####################################################################
# Problem 35
if problem == 35:
	allPrimes = set(primes.primes(10**6)) # All primes less than a million
	circularPrimes = set([])
	for p in allPrimes:
		circular = True
		# Do all rotations
		qstr = str(p)
		print qstr
		for i in xrange(len(qstr)):
			q = int(qstr)
			if not q in allPrimes:
				circular = False
				break
			qstr = qstr[1:] + qstr[0]
		# Final check
		if circular:
			circularPrimes.add(p)

	print len(circularPrimes)




#####################################################################
# Problem 36
if problem == 36:
	# Because we are using palindromes in base 2, the last digit in base 2 needs to be a 1
	# This means that we only care about odd numbers which halves our search space!
	doubleBasePalindromes = []
	for x in xrange(1,10**6,2):
		if nf.ispalindrome(x) and nf.ispalindrome(nf.base2(x)):
			doubleBasePalindromes.append(x)
	print sum(doubleBasePalindromes)



#####################################################################
# Problem 37
if problem == 37:
	allPrimes = set(primes.primes(10**6)) # All primes less than a million
	truncablePrimes = []
	for p in allPrimes:
		if p < 10:
			continue
		leftTruncable = True
		rightTruncable = True
		# Do all rotations
		qstr = str(p)
		# Check if left trucable
		for i in xrange(1,len(qstr)):
			q = int(qstr[i:])
			if not q in allPrimes:
				leftTruncable = False
				break
		if not leftTruncable:
			continue
		for i in xrange(1,len(qstr)):
			q = int(qstr[0:(len(qstr)-i)])
			if not q in allPrimes:
				rightTruncable = False
				break
		# Final check
		if leftTruncable and rightTruncable:
			truncablePrimes.append(p)

	print sum(truncablePrimes)


#####################################################################
# Problem 38
if problem == 38:
	pass

#####################################################################
# Problem 39
if problem == 39:
	pass


#####################################################################
# Problem 40
if problem == 40:
	pass

#####################################################################
# Problem 41
if problem == 41:
	pass

#####################################################################
# Problem 42
if problem == 42:
	pass

#####################################################################
# Problem 43
if problem == 43:
	pass

#####################################################################
# Problem 44
if problem == 44:
	pass

#####################################################################
# Problem 45
if problem == 45:
	pass

#####################################################################
# Problem 46
if problem == 46:
	pass

#####################################################################
# Problem 47
if problem == 47:
	pass

#####################################################################
# Problem 48
if problem == 48:
	pass

#####################################################################
# Problem 49
if problem == 49:
	pass

























