#/usr/bin/python

import sys

a=int(sys.argv[1])

r = a
s = ""
while r != 0:
	s = str(r % 2) + s
	r = r // 2

s = s + '00'

while len(s) < 32:
	s = "0" + s

for i in xrange(len(s)/4):
	s1 = s[4*i]+s[4*i+1]+s[4*i+2]+s[4*i+3]
	print s1

print s



