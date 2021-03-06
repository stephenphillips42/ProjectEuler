#/usr/bin/python
# Basic imports
import sys
import math

# My imports
import numberFunctions as nf
import primeFunctions as pf
import listUtils as lu
import constants as const


# Extra imports
from collections import Counter # Basically a multiset

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
	print maxx*maxy

#####################################################################
# Problem 5
if problem == 5:
	# Did this by hand
	print 232792560

#####################################################################
# Problem 6
if problem == 6:
	print (cumsum(100))**2 - sumofsquares(100)

#####################################################################
# Problem 7
# Note: 3137 is the 446th prime
# Failed method -- too high a probability of getting it wrong
def findnthprime():
	count = 446
	x = 3137
	progress = 1503
	lastprime = x
	while x < 10**7:
		if pf.isPrimeFast(x):
			count += 1
			lastprime = x
			if count == 10001:
				# print "FOUND IT"
				# print (x, count)
				return
		if x % progress == 0:
			print (lastprime,count)
		x += 2
# Best solution
if problem == 7:
	primelist = pf.sieveEratosthenes(2*10**6)
	print primelist[10000] 

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
	import data.problem0008
	print maxprod(data.problem0008.num1000Digits,13)[0]

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
	primelist = pf.sieveEratosthenes(2*10**6)
	print sum(primelist)

#####################################################################
# Problem 11

if problem == 11:
	import data.problem0011
	A = data.problem0011.grid20x20
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
	val = 0
	for x in xrange(9,50000):
		# Find prime factors of n*(n-1)/2
		numdiv = 0
		if x % 2 == 0:
			factorx = pf.factorTrialDivision(x//2)
			factorx1 = pf.factorTrialDivision(x+1)
			factorx.extend(factorx1)
			numdiv = lu.product(lu.addOne(lu.listCount(factorx)))
		else:
			factorx = pf.factorTrialDivision(x)
			factorx1 = pf.factorTrialDivision((x+1)//2)
			factorx.extend(factorx1)
			numdiv = lu.product(lu.addOne(lu.listCount(factorx)))

		if (numdiv) >= 500:
			val = x
			break
	print nf.cumsum(val)

#####################################################################
# Problem 13
# OK I cheated... thank you big number library of python
if problem == 13:
	import data.problem0013
	s = 0L
	for i in xrange(len(data.problem0013.numList100Digits)):
		s += (data.problem0013.numList100Digits[i])
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
	import data.problem0018
	T = data.problem0018.pathTriangle
	Cache = [ [ -1 for x in xrange(len(T)) ] for x in xrange(len(T)) ]
	print dftMaxPath(T,Cache)

if problem == 67:
	import data.problem0067
	Tbig = data.problem0067.pathTriangleBig
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
		Cache[N] = pf.trialDivisionDivisors(x)
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
def getScore(name):
	score = 0
	for x in name:
		score += const.alphaNum[x]
	return score

if problem == 22:
	import data.problem0022
	SortedNamesList = sorted(data.problem0022.NamesList)
	t = 0
	for i in xrange(len(SortedNamesList)):
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
		s = sum(pf.trialDivisionDivisors(i))
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
def poly(n,a,b):
	return n**2 + a*n + b

# assumes P is a list of primes, pi index for that list
def testQuadratic(pi, P):
	b = P[pi]
	m = 0
	ma = -1
	for a in xrange(-1000,1001):
		n = 0
		while poly(n,a,b) > 0 and pf.isPrime(poly(n,a,b)):
			n += 1
		if n > m:
			m = n
			ma = a
	return (m,ma)

if problem == 27:
	m = 0
	a = 0
	b = 0
	primelist = pf.primes(1000)
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
	allPrimes = set(pf.primes(10**6)) # All primes less than a million
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
	allPrimes = set(pf.primes(10**6)) # All primes less than a million
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
allDigits = Counter({1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1}) # Set we are comparing to

def isPandigital(N):
	return isPandigitalStr(str(N))

def isPandigitalStr(Nstr):
	if len(Nstr) != 9:
		return False
	return Counter([ int(x) for x in Nstr ]) == allDigits

if problem == 38:
	# Upper bounds:
	# We know that 1 * (5 digit number) = (5 digit number), and that
	# (> 1) * (5 digit number) = (>= 5 digit number)
	# Therefore 5 digit numbers CANNOT satisify the pandigital multiples property
	# And therefore 10**5-1 is our upper bound
	pandigitalMultiples = []
	pandigitalValues = []
	for n in xrange(1,10**5):
		Nstr = ""
		k = 0
		while len(Nstr) < 9:
			k += 1
			Nstr += str(k*n)
		if isPandigitalStr(Nstr):
			pandigitalMultiples.append((n,k))
			pandigitalValues.append(int(Nstr))
	print max(pandigitalValues)

#####################################################################
# Problem 39
# Generate all Pythagorean Triples of perimeter < P 
def generatePythagoreanTriples(P):
	# Notes:
	# - c can be at most P-2, insince 0 < a < b < c and (1)+(2)+(P-2) > P
	# - c is of the form 4*n + 1 (thanks Wikipedia!!)
	# - c is odd (see above), therefore exactly 1 of a or b is odd (thanks Wikipedia!!)
	# - Using the above we can generate all the primitive pythagorean triples and then
	#   use the fact that k**2*(a**2+b**2-c**2)==0 to generate the non-primitive ones
	pythagTriples = []
	for c in xrange(3,P+1,4):
		for b in xrange(1,c):
			for a in xrange(1+(b%2),b,2): # odd if b even, and vice versa
				if a**2 + b**2 - c**2 == 0:
					k = 1 # Generate not just primitive pythagorean triples
					while k*(a+b+c) < P:
						pythagTriples.append((k*a,k*b,k*c,k*(a+b+c)))
						k += 1
	return pythagTriples

if problem == 39:
	# Find all pythagorean triples with perimeter <= 1000
	pTriples = generatePythagoreanTriples(1000);
	maxPerim = 0
	maxPerimCount = 0
	for perim in xrange(1,1001):
		count = sum([ x for x in xrange(len(pTriples)) if pTriples[x][3] == perim])
		if maxPerimCount < count:
			maxPerim = perim
			maxPerimCount = count

	print maxPerim


#####################################################################
# Problem 40
if problem == 40:
	i = 0;
	loc = 0;
	done = False;
	digits = []
	while not done:
		i += 1
		for d in [ int(x) for x in str(i) ]:
			loc += 1
			if loc == 1:
				digits.append(d)
			elif loc == 10:
				digits.append(d)
			elif loc == 10**2:
				digits.append(d)
			elif loc == 10**3:
				digits.append(d)
			elif loc == 10**4:
				digits.append(d)
			elif loc == 10**5:
				digits.append(d)
			elif loc == 10**6:
				digits.append(d)
				done = True
				break

	print digits
	print lu.product(digits)

#####################################################################
# Problem 41
if problem == 41:
	currPrime = -1
	# Tested using 8 and 9 as well, returned no primes
	for pandigital in lu.permute([1,2,3,4,5,6,7]):
		primeCandidate =  lu.toNum(pandigital)
		if pf.isPrimeFermat(primeCandidate):
			if primeCandidate > currPrime:
				currPrime = primeCandidate
	print currPrime

#####################################################################
# Problem 42
# Using getScore from problem 22
def isTriangle(N):
	m = int((math.sqrt(1+8*N)-1)/2 + 0.5)
	return (m*(m+1)/2) == N

if problem == 42:
	import data.problem0042
	triangleWordList = data.problem0042.TriangleWordsLists
	triangleWordCount = 0
	for word in triangleWordList:
		if isTriangle(getScore(word)):
			triangleWordCount += 1
	print triangleWordCount


#####################################################################
# Problem 43
if problem == 43:
	substrDivisible = []
	divisibility = [2,3,5,7,11,13,17]
	for pandigital in lu.permute([0,1,2,3,4,5,6,7,8,9]):
		isCandidate = True
		for i in xrange(0,len(divisibility)):
			substr = lu.toNum(pandigital[(i+1):(i+4)])
			if substr % divisibility[i] != 0:
				isCandidate = False
				break
		if isCandidate:
			substrDivisible.append(lu.toNum(pandigital))
	print sum(substrDivisible)


#####################################################################
# Problem 44
def isPentagonal(N):
	m = int((1+math.sqrt(1+24*N))/6 + 0.5)
	return (m*(3*m-1)/2) == N

if problem == 44:
	B = 3000
	pentagonalNums = []
	for i in xrange(1,B+1):
		pentagonalNums.append((i*(3*i-1))/2)

	sumPentagonalCount = 0
	sumAndDiffPentagonalCount = 0
	minDiffVals = (-1,-1,10**10)
	for i in xrange(0,B):
		for j in xrange(0,i):
			if isPentagonal(pentagonalNums[i]-pentagonalNums[j]):
				if isPentagonal(pentagonalNums[i]+pentagonalNums[j]):
					if abs(pentagonalNums[i]-pentagonalNums[j]) < minDiffVals[2]:
						minDiffVals = (i,j,(pentagonalNums[i]-pentagonalNums[j]))

	print minDiffVals[2]

#####################################################################
# Problem 45
# Uses isTriangle from problem 42
# Uses isPentagonal from problem 44
# OK I never used this but I figured it out so here it is
def isHexagonal(N):
	m = int((1+math.sqrt(1+8*N))/4 + 0.5)
	return (m*(2*m-1)) == N

if problem == 45:
	for i in xrange(144,100000):
		n = i*(2*i-1)
		if isTriangle(n) and isPentagonal(n):
			print n
			break

#####################################################################
# Problem 46
if problem == 46:
	B = 2*10**6 # B for bound
	primelist = pf.sieveEratosthenes(B)
	primeset = set(primelist)
	for i in xrange(5,B-1,2):
		if i in primeset:
			continue
		goldbachSquare = False
		for p in primelist:
			m = i - p
			if m < 0: # Prime too large
				break
			if m % 2 == 1: # Conjecture requires divisible by 2
				continue
			# Test conjecture for this prime
			m = m // 2
			if m == 0 or (int(math.sqrt(m) + 0.5))**2 == m:
				goldbachSquare = True
				break
		if not goldbachSquare:
			print i
			break

#####################################################################
# Problem 47
if problem == 47:
	runLength = 4
	distinctPrimeRun = 0
	primeList = pf.sieveEratosthenes(2*10**6)
	for i in xrange(2*3*5*7,10**9):
		nFactors = len(set(pf.factorTrialDivision(i,primeList)))
		if nFactors == runLength:
			distinctPrimeRun += 1
			if distinctPrimeRun == runLength:
				print (i-3,i-2,i-1,i)
				break
		else:
			distinctPrimeRun = 0

#####################################################################
# Problem 48
if problem == 48:
	s = 0
	for i in xrange(1,1000):
		s += nf.modPow(i,i,10**10)
	print s % (10**10)


#####################################################################
# Problem 49
if problem == 49:
	primeList = pf.sieveEratosthenes(10000)

	# Find the first 4 digit prime
	i = 0
	while i < len(primeList):
		if primeList[i] > 1000:
			startIndex = i
			break
		i = i+1

	# Reduce the primeList
	primeList = primeList[startIndex:]
	primeSet = set(primeList)

	# Find the geometric sequences
	foundSequence = False
	for i in xrange(0,len(primeList)):
		# Now since we are avoiding this case we have to skip it
		if primeList[i] == 1487:
			continue
		for j in xrange(i+1,len(primeList)):
			# Find out if they are permutations
			if Counter(str(primeList[i])) != Counter(str(primeList[j])):
				continue
			# Now find if they from a geometric sequence
			if (primeList[j] + (primeList[j]-primeList[i])) not in primeSet:
				continue
			primeListK = (primeList[j] + (primeList[j]-primeList[i]))
			# Now check if that is a permutation
			if Counter(str(primeList[i])) == Counter(str(primeListK)):
				foundSequence = True
				print (primeList[i],primeList[j],primeListK)
				break
		if foundSequence:
			break



#####################################################################
# Problem 50
if problem == 50:
	primeList = pf.sieveEratosthenes(10**6)
	primeSet = set(primeList)
	maxStart = 0
	maxFin = 0
	maxSum = 0
	for i in xrange(0,len(primeList)):
		j = i+1
		while sum(primeList[i:j]) < 10**6 and j < len(primeList):
			currSum = sum(primeList[i:j])
			currRange = j-i
			if currSum in primeSet and currRange > maxFin-maxStart:
				maxStart = i
				maxFin = j
				maxSum = currSum
			j = j+1

	print maxStart
	print maxFin
	print maxSum

#####################################################################
# Problem 51
def blankSlotPrimes(n,m):
	d = n - m # d for digits
	# Create list of primes we will use
	primeList = pf.sieveEratosthenes(10**(n+1))

	# Remove primes that are too small
	startIndex = 0
	for i in xrange(0,len(primeList)):
		if primeList[i] > 10**(n-1):
			startIndex = i
			break
	primeList = primeList[startIndex:]

	# Set up set for fast prime checking
	primeSet = set(primeList)


	# Indecies for the repeated digits
	digitIndeces = []
	for i in xrange(0,m):
		digitIndeces.append(range(0,d+1))

	# Data structure cleverness - how we insert the repeated digits
	# into the number
	NumStruct = ['' for x in xrange(0,2*d+1)]
	numIndex = [ 2*x+1 for x in xrange(0,d)]
	repIndex = [ 2*x for x in xrange(0,d+1)]

	# Keep track of maximum
	maxPrimeCount = 0
	maxPrimeStruct = ([],[])

	# Go through all the numbers with the repeated digits
	for ni in xrange(0,10**d):
		# Set up the struct
		numStr = str(ni).zfill(d)
		for i in xrange(0,d):
			NumStruct[numIndex[i]] = numStr[i]

		# Find the repeated indecies with the most primes
		for t in itertools.product(*digitIndeces):
			primeCount = 0
			smallestValue = -1 # Store the smallest value of the prime
			# Loop through actual value of repeated digits
			for r in xrange(0,10):
				numStruct = list(NumStruct)
				# Place in the digits according to positions, t
				for i in xrange(0,len(t)):
					numStruct[repIndex[t[i]]] += (str(r))
				# Check if the number is prime
				num = int(''.join(numStruct))
				if num in primeSet:
					if smallestValue < 0:
						smallestValue = r # Update the smallest value of the prime
					primeCount += 1
			# Update maximum
			if primeCount > maxPrimeCount:
				maxPrimeCount = primeCount
				numStruct = list(NumStruct)
				for i in xrange(0,len(t)):
					numStruct[repIndex[t[i]]] += str(smallestValue)
				smallest = int(''.join(numStruct))
				maxPrimeStruct = (list(t),list(NumStruct),smallest)
	return (maxPrimeCount, maxPrimeStruct)

if problem == 51:
	n = 6
	m = 3
	(maxPrimeCount, maxPrimeStruct) = blankSlotPrimes(n,m)
	print maxPrimeStruct

#####################################################################
# Problem 52
if problem == 52:
	for d in xrange(2,7): # Go through all orders of magnitude
		found = False
		for i in xrange(10**(d-1),10**(d)):
			# Prepend 1 to number (must start with 1)
			n = i + 10**d
			digits = nf.getDigits(n)
			if digits == nf.getDigits(2*n) \
					and digits == nf.getDigits(3*n) \
					and digits == nf.getDigits(4*n) \
					and digits == nf.getDigits(5*n) \
					and digits == nf.getDigits(6*n):
				 print n
				 found = True
				 break
		if found:
			break

#####################################################################
# Problem 53
if problem == 53:
	count = 0
	for n in xrange(1,100+1):
		for k in xrange(0,n):
			if nf.nchoosek(n,k) > 10**6:
				count += 1

	print count

#####################################################################
# Problem 54
class PokerHand:
	"""Class for Poker Hand for problem 54"""
	def __init__(self, cards):
		# Get the number and suits for each of the cards
		self.cardnums = []
		self.cardsuits = []
		for c in cards:
			# This changes 2, ..., 9, T, J, Q, K, A to 2-14 for simplicity
			self.cardnums.append(const.pokerConversion[c[0]])
			# This just saves the suit
			self.cardsuits.append(c[1])
		# Get the cards in sorted order
		indeces = sorted(range(len(self.cardnums)), key=lambda k: self.cardnums[k])
		self.cardnums = sorted(self.cardnums)
		self.cardsuits = [ self.cardsuits[i] for i in indeces ]
		self.sortedorig = [ cards[i] for i in indeces ]

	# Find the rank, value of hand of said rank, and the max card of the hand
	def handRank(self):
		assert len(self.cardnums) == len(self.cardsuits), "Cannot match suits"
		assert len(self.cardnums) == 5, "We do not have the right number of cards"
		maxcard = max(self.cardnums)
		# Figure out what rank the card is - return rank of hand,
		# plus value of particular instance of that rank

		# Rank 10 - Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
		if self.cardnums == [10,11,12,13,14] \
				and lu.allSame(self.cardsuits):
			return (10,14)

		# Rank 9 - Straight Flush: All cards are consecutive values of same suit.
		if self.cardnums == [(x+self.cardnums[0]) for x in xrange(5)] \
				and lu.allSame(self.cardsuits):
			return (9,self.cardnums[0]+4)

		# Rank 8 - Four of a Kind: Four cards of the same value.
		if self.cardnums[0:4] == [self.cardnums[0] for x in xrange(4)] \
				or self.cardnums[1:5] == [self.cardnums[1] for x in xrange(4)]:
			# Value of the hand is the number of the repeated card
			return (8,self.cardnums[2])

		# Rank 7 - Full House: Three of a kind and a pair.
		if self.cardnums[0:2] == [self.cardnums[0], self.cardnums[0]] \
				and self.cardnums[3:5] == [self.cardnums[1], self.cardnums[1]]:
			# Have two pairs, check to see if it is actually a full house
			if self.cardnums[2] == self.cardnums[0] \
					or self.cardnums[2] == self.cardnums[4]:
				return (7,self.cardnums[2])

		# Rank 6 - Flush: All cards of the same suit.
		if lu.allSame(self.cardsuits):
			return (6,maxcard)

		# Rank 5 - Straight: All cards are consecutive values.
		if self.cardnums == [(x+self.cardnums[0]) for x in xrange(5)]:
			return (5,self.cardnums[0]+4)

		# Rank 4 - Three of a Kind: Three cards of the same value.
		if self.cardnums[0:3] == [self.cardnums[0] for x in xrange(3)] \
				or self.cardnums[1:4] == [self.cardnums[1] for x in xrange(3)] \
				or self.cardnums[2:5] == [self.cardnums[2] for x in xrange(3)]:
			return (4,self.cardnums[2])

		# Rank 3 - Two Pairs: Two different pairs.
		for i in xrange(2):
			if self.cardnums[i] == self.cardnums[i+1] \
					and self.cardnums[i+2] == self.cardnums[i+3]:
				return (3,max(self.cardnums[i], self.cardnums[i+2]))
		if self.cardnums[0] == self.cardnums[1] \
				and self.cardnums[3] == self.cardnums[4]:
			return (3,max(self.cardnums[0], self.cardnums[3]))

		# Rank 2 - One Pair: Two cards of the same value.
		for i in xrange(4):
			if self.cardnums[i] == self.cardnums[i+1]:
				return (2,self.cardnums[i])

		# Rank 1 - High Card: Highest value card.
		return (1,maxcard)


if problem == 54:
	import data.problem0054
	PokerHands = data.problem0054.PokerHands
	player1win = 0
	for i in xrange(len(PokerHands)):
		p = PokerHands[i]
		hand1 = PokerHand(p[0])
		hand2 = PokerHand(p[1])
		(rank1,value1) = hand1.handRank()
		(rank2,value2) = hand2.handRank()
		winner = 2
		if rank1 > rank2 \
				or rank1 == rank2 and value1 > value2:
			player1win += 1
		if rank1 == rank2 and value1 == value2:
			i = -1
			while i != -5 and hand1.cardnums[i] == hand2.cardnums[i]:
				i -= 1
			if hand1.cardnums[i] > hand2.cardnums[i]:
				player1win += 1


	print player1win

#####################################################################
# Problem 55
if problem == 55:
	lychrelNumCount = 0
	for i in xrange(1,10001):
		k = 0
		n = i
		while not nf.ispalindrome(n + nf.flip(n)) and k < 50:
			k += 1
			n += nf.flip(n)

		if k == 50:
			lychrelNumCount += 1

	print lychrelNumCount



#####################################################################
# Problem 56
if problem == 56:
	maxa = 0
	maxb = 0
	maxsum = 0
	for a in xrange(1,100):
		for b in xrange(1,100):
			n = a**b
			currsum = sum([int(x) for x in str(n)])
			if currsum > maxsum:
				maxsum = currsum
				maxa = a
				maxb = b

	print maxsum

#####################################################################
# Problem 57
if problem == 57:
	from fractions import Fraction
	largerNumeratorCount = 0
	stime1 = time.clock()
	frac = Fraction(2,1) # first iteration
	for i in xrange(1,1000):
		frac = 2 + 1 / frac
		sqrt2 = 1 + 1/frac
		if len(str(sqrt2.numerator)) > len(str(sqrt2.denominator)):
			largerNumeratorCount += 1

	print largerNumeratorCount

#####################################################################
# Problem 58
if problem == 58:
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

#####################################################################
# Problem 59
if problem == 59:
	pass

#####################################################################
# Problem 60
if problem == 60:
	pass

#####################################################################
# Problem 61
if problem == 61:
	pass

#####################################################################
# Problem 62
if problem == 62:
	pass

#####################################################################
# Problem 63
if problem == 63:
	pass

#####################################################################
# Problem 64
if problem == 64:
	pass

#####################################################################
# Problem 65
if problem == 65:
	pass

#####################################################################
# Problem 66
if problem == 66:
	pass

#####################################################################
# Problem 67
if problem == 67:
	pass

#####################################################################
# Problem 68
if problem == 68:
	pass

#####################################################################
# Problem 69
if problem == 69:
	pass

#####################################################################
# Problem 70
if problem == 70:
	pass

#####################################################################
# Problem 71
if problem == 71:
	pass

#####################################################################
# Problem 72
if problem == 72:
	pass

#####################################################################
# Problem 73
if problem == 73:
	pass

#####################################################################
# Problem 74
if problem == 74:
	pass

#####################################################################
# Problem 75
if problem == 75:
	pass

#####################################################################
# Problem 76
if problem == 76:
	pass

#####################################################################
# Problem 77
if problem == 77:
	pass

#####################################################################
# Problem 78
if problem == 78:
	pass

#####################################################################
# Problem 79
if problem == 79:
	pass

#####################################################################
# Problem 80
if problem == 80:
	pass





































