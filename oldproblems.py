#/usr/bin/python

import sys
import math
import numbers
import primes
import listUtils

#####################################################################
# Problem 4
def ispalindrome(N):
	return N == numbers.flip(N)

def findmaxpalindrom():
	for x in xrange(899,1,0,0,0,):
		for y in xrange(899,1,0,0,0,):
			if ispalindrome(x*y):
				maxx = x
				maxy = y
	print "Maximum:"
	print maxx*maxy
	print maxx
	print maxy

#####################################################################
# Problem 6
# See numbers.sumofsquares, and numbers.cumsum

#####################################################################
# Problem 8
nums = [
  7,3,1,6,7,1,7,6,5,3,1,3,3,0,6,2,4,9,1,9,2,2,5,1,1,9,6,7,4,4,2,6,5,7,4,7,4,2,3,5,5,
  3,4,9,1,9,4,9,3,4,9,6,9,8,3,5,2,0,3,1,2,7,7,4,5,0,6,3,2,6,2,3,9,5,7,8,3,1,8,0,1,6,
  9,8,4,8,0,1,8,6,9,4,7,8,8,5,1,8,4,3,8,5,8,6,1,5,6,0,7,8,9,1,1,2,9,4,9,4,9,5,4,5,9,
  5,0,1,7,3,7,9,5,8,3,3,1,9,5,2,8,5,3,2,0,8,8,0,5,5,1,1,1,2,5,4,0,6,9,8,7,4,7,1,5,8,
  5,2,3,8,6,3,0,5,0,7,1,5,6,9,3,2,9,0,9,6,3,2,9,5,2,2,7,4,4,3,0,4,3,5,5,7,6,6,8,9,6,
  6,4,8,9,5,0,4,4,5,2,4,4,5,2,3,1,6,1,7,3,1,8,5,6,4,0,3,0,9,8,7,1,1,1,2,1,7,2,2,3,8,
  3,1,1,3,6,2,2,2,9,8,9,3,4,2,3,3,8,0,3,0,8,1,3,5,3,3,6,2,7,6,6,1,4,2,8,2,8,0,6,4,4,
  4,4,8,6,6,4,5,2,3,8,7,4,9,3,0,3,5,8,9,0,7,2,9,6,2,9,0,4,9,1,5,6,0,4,4,0,7,7,2,3,9,
  0,7,1,3,8,1,0,5,1,5,8,5,9,3,0,7,9,6,0,8,6,6,7,0,1,7,2,4,2,7,1,2,1,8,8,3,9,9,8,7,9,
  7,9,0,8,7,9,2,2,7,4,9,2,1,9,0,1,6,9,9,7,2,0,8,8,8,0,9,3,7,7,6,6,5,7,2,7,3,3,3,0,0,
  1,0,5,3,3,6,7,8,8,1,2,2,0,2,3,5,4,2,1,8,0,9,7,5,1,2,5,4,5,4,0,5,9,4,7,5,2,2,4,3,5,
  2,5,8,4,9,0,7,7,1,1,6,7,0,5,5,6,0,1,3,6,0,4,8,3,9,5,8,6,4,4,6,7,0,6,3,2,4,4,1,5,7,
  2,2,1,5,5,3,9,7,5,3,6,9,7,8,1,7,9,7,7,8,4,6,1,7,4,0,6,4,9,5,5,1,4,9,2,9,0,8,6,2,5,
  6,9,3,2,1,9,7,8,4,6,8,6,2,2,4,8,2,8,3,9,7,2,2,4,1,3,7,5,6,5,7,0,5,6,0,5,7,4,9,0,2,
  6,1,4,0,7,9,7,2,9,6,8,6,5,2,4,1,4,5,3,5,1,0,0,4,7,4,8,2,1,6,6,3,7,0,4,8,4,4,0,3,1,
  9,9,8,9,0,0,0,8,8,9,5,2,4,3,4,5,0,6,5,8,5,4,1,2,2,7,5,8,8,6,6,6,8,8,1,1,6,4,2,7,1,
  7,1,4,7,9,9,2,4,4,4,2,9,2,8,2,3,0,8,6,3,4,6,5,6,7,4,8,1,3,9,1,9,1,2,3,1,6,2,8,2,4,
  5,8,6,1,7,8,6,6,4,5,8,3,5,9,1,2,4,5,6,6,5,2,9,4,7,6,5,4,5,6,8,2,8,4,8,9,1,2,8,8,3,
  1,4,2,6,0,7,6,9,0,0,4,2,2,4,2,1,9,0,2,2,6,7,1,0,5,5,6,2,6,3,2,1,1,1,1,1,0,9,3,7,0,
  5,4,4,2,1,7,5,0,6,9,4,1,6,5,8,9,6,0,4,0,8,0,7,1,9,8,4,0,3,8,5,0,9,6,2,4,5,5,4,4,4,
  3,6,2,9,8,1,2,3,0,9,8,7,8,7,9,9,2,7,2,4,4,2,8,4,9,0,9,1,8,8,8,4,5,8,0,1,5,6,1,6,6,
  0,9,7,9,1,9,1,3,3,8,7,5,4,9,9,2,0,0,5,2,4,0,6,3,6,8,9,9,1,2,5,6,0,7,1,7,6,0,6,0,5,
  8,8,6,1,1,6,4,6,7,1,0,9,4,0,5,0,7,7,5,4,1,0,0,2,2,5,6,9,8,3,1,5,5,2,0,0,0,5,5,9,3,
  5,7,2,9,7,2,5,7,1,6,3,6,2,6,9,5,6,1,8,8,2,6,7,0,4,2,8,2,5,2,4,8,3,6,0,0,8,2,3,2,5,
  7,5,3,0,4,2,0,7,5,2,9,6,3,4,5,0
]
############  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
smallnums = [ 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1]

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
				print "zero"
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
			print "no zero %f" % prod
			prod /= nums[i]
			prod *= nums[i+k]
			i += 1
			if prod > m:
				m = prod
				mi = i

	return (m,mi)

#####################################################################
# Problem 9
def pythagoreanTriple():
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
		if primes.isprime(x):
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
def getPrime10001():
	primelist = primes.sieveEratosthenes(2*10**6)
	l = len(primelist)
	if l > 10001:
		print "We got it!!"
		print primelist[10000]
	print l
	print primelist[l-1] 

#####################################################################
# Problem 10
def sumPrimes():
	primelist = primes.sieveEratosthenes(2*10**6)
	print sum(primelist)

#####################################################################
# Problem 11
A = [ [ 8, 2,22,97,38,15, 0,40, 0,75, 4, 5, 7,78,52,12,50,77,91, 8],
	  [49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48, 4,56,62, 0],
	  [81,49,31,73,55,79,14,29,93,71,40,67,53,88,30, 3,49,13,36,65],
	  [52,70,95,23, 4,60,11,42,69,24,68,56, 1,32,56,71,37, 2,36,91],
	  [22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80],
	  [24,47,32,60,99, 3,45, 2,44,75,33,53,78,36,84,20,35,17,12,50],
	  [32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70],
	  [67,26,20,68, 2,62,12,20,95,63,94,39,63, 8,40,91,66,49,94,21],
	  [24,55,58, 5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72],
	  [21,36,23, 9,75, 0,76,44,20,45,35,14, 0,61,33,97,34,31,33,95],
	  [78,17,53,28,22,75,31,67,15,94, 3,80, 4,62,16,14, 9,53,56,92],
	  [16,39, 5,42,96,35,31,47,55,58,88,24, 0,17,54,24,36,29,85,57],
	  [86,56, 0,48,35,71,89, 7, 5,44,44,37,44,60,21,58,51,54,17,58],
	  [19,80,81,68, 5,94,47,69,28,73,92,13,86,52,17,77, 4,89,55,40],
	  [ 4,52, 8,83,97,35,99,16, 7,97,57,32,16,26,26,79,33,27,98,66],
	  [88,36,68,87,57,62,20,72, 3,46,33,67,46,55,12,32,63,93,53,69],
	  [ 4,42,16,73,38,25,39,11,24,94,72,18, 8,46,29,32,40,62,76,36],
	  [20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74, 4,36,16],
	  [20,73,35,29,78,31,90, 1,74,31,49,71,48,86,81,16,23,57, 5,54],
	  [ 1,70,54,71,83,51,54,69,16,92,33,48,61,43,52, 1,89,19,67,48] ]

def findMaxGridProduct():
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
def triangleNumberDivisors():
	for x in xrange(9,50000):
		numdiv = primes.numDivisors(numbers.cumsum(x))
		if (numdiv) >= 500:
			print x
			print numbers.cumsum(x)
			print numdiv
			break

#####################################################################
# Problem 13
nums100Digits = [
  37107287533902102798797998220837590246510135740250L,
  46376937677490009712648124896970078050417018260538L,
  74324986199524741059474233309513058123726617309629L,
  91942213363574161572522430563301811072406154908250L,
  23067588207539346171171980310421047513778063246676L,
  89261670696623633820136378418383684178734361726757L,
  28112879812849979408065481931592621691275889832738L,
  44274228917432520321923589422876796487670272189318L,
  47451445736001306439091167216856844588711603153276L,
  70386486105843025439939619828917593665686757934951L,
  62176457141856560629502157223196586755079324193331L,
  64906352462741904929101432445813822663347944758178L,
  92575867718337217661963751590579239728245598838407L,
  58203565325359399008402633568948830189458628227828L,
  80181199384826282014278194139940567587151170094390L,
  35398664372827112653829987240784473053190104293586L,
  86515506006295864861532075273371959191420517255829L,
  71693888707715466499115593487603532921714970056938L,
  54370070576826684624621495650076471787294438377604L,
  53282654108756828443191190634694037855217779295145L,
  36123272525000296071075082563815656710885258350721L,
  45876576172410976447339110607218265236877223636045L,
  17423706905851860660448207621209813287860733969412L,
  81142660418086830619328460811191061556940512689692L,
  51934325451728388641918047049293215058642563049483L,
  62467221648435076201727918039944693004732956340691L,
  15732444386908125794514089057706229429197107928209L,
  55037687525678773091862540744969844508330393682126L,
  18336384825330154686196124348767681297534375946515L,
  80386287592878490201521685554828717201219257766954L,
  78182833757993103614740356856449095527097864797581L,
  16726320100436897842553539920931837441497806860984L,
  48403098129077791799088218795327364475675590848030L,
  87086987551392711854517078544161852424320693150332L,
  59959406895756536782107074926966537676326235447210L,
  69793950679652694742597709739166693763042633987085L,
  41052684708299085211399427365734116182760315001271L,
  65378607361501080857009149939512557028198746004375L,
  35829035317434717326932123578154982629742552737307L,
  94953759765105305946966067683156574377167401875275L,
  88902802571733229619176668713819931811048770190271L,
  25267680276078003013678680992525463401061632866526L,
  36270218540497705585629946580636237993140746255962L,
  24074486908231174977792365466257246923322810917141L,
  91430288197103288597806669760892938638285025333403L,
  34413065578016127815921815005561868836468420090470L,
  23053081172816430487623791969842487255036638784583L,
  11487696932154902810424020138335124462181441773470L,
  63783299490636259666498587618221225225512486764533L,
  67720186971698544312419572409913959008952310058822L,
  95548255300263520781532296796249481641953868218774L,
  76085327132285723110424803456124867697064507995236L,
  37774242535411291684276865538926205024910326572967L,
  23701913275725675285653248258265463092207058596522L,
  29798860272258331913126375147341994889534765745501L,
  18495701454879288984856827726077713721403798879715L,
  38298203783031473527721580348144513491373226651381L,
  34829543829199918180278916522431027392251122869539L,
  40957953066405232632538044100059654939159879593635L,
  29746152185502371307642255121183693803580388584903L,
  41698116222072977186158236678424689157993532961922L,
  62467957194401269043877107275048102390895523597457L,
  23189706772547915061505504953922979530901129967519L,
  86188088225875314529584099251203829009407770775672L,
  11306739708304724483816533873502340845647058077308L,
  82959174767140363198008187129011875491310547126581L,
  97623331044818386269515456334926366572897563400500L,
  42846280183517070527831839425882145521227251250327L,
  55121603546981200581762165212827652751691296897789L,
  32238195734329339946437501907836945765883352399886L,
  75506164965184775180738168837861091527357929701337L,
  62177842752192623401942399639168044983993173312731L,
  32924185707147349566916674687634660915035914677504L,
  99518671430235219628894890102423325116913619626622L,
  73267460800591547471830798392868535206946944540724L,
  76841822524674417161514036427982273348055556214818L,
  97142617910342598647204516893989422179826088076852L,
  87783646182799346313767754307809363333018982642090L,
  10848802521674670883215120185883543223812876952786L,
  71329612474782464538636993009049310363619763878039L,
  62184073572399794223406235393808339651327408011116L,
  66627891981488087797941876876144230030984490851411L,
  60661826293682836764744779239180335110989069790714L,
  85786944089552990653640447425576083659976645795096L,
  66024396409905389607120198219976047599490197230297L,
  64913982680032973156037120041377903785566085089252L,
  16730939319872750275468906903707539413042652315011L,
  94809377245048795150954100921645863754710598436791L,
  78639167021187492431995700641917969777599028300699L,
  15368713711936614952811305876380278410754449733078L,
  40789923115535562561142322423255033685442488917353L,
  44889911501440648020369068063960672322193204149535L,
  41503128880339536053299340368006977710650566631954L,
  81234880673210146739058568557934581403627822703280L,
  82616570773948327592232845941706525094512325230608L,
  22918802058777319719839450180888072429661980811197L,
  77158542502016545090413245809786882778948721859617L,
  72107838435069186155435662884062257473692284509516L,
  20849603980134001723930671666823555245252804609722L,
  53503534226472524250874054075591789781264330331690L  ]
def sumLargeNumbers():
	s = 0L
	for i in xrange(len(nums100Digits)):
		s += (nums100Digits[i])
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

def collatzMax():
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

#####################################################################
# Problem 16
def sumOfDigits():
	L = 2**1000
	s = 0
	for i in xrange(302):
		s = s + (L % 10)
		L = L // 10
	return s

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

def getLengthOfLetters():
	l = 0
	for i in xrange(1,1001):
		l += len(digitsToLetters(i).replace(' ',''))
	return l










