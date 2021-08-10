import sys
import random
from random import randint
N = (input("Enter N "))
m = []
a = 0
if not (N.isdigit()):
	print ("N is not a digit")
	sys.exit()
N = int(N)
for i in range (N):
	m.append ([])
	for j in range (N):
		m[i].append(randint (0,9))
for k in (m):
	for t in (k):
		if t%3==0 : a=a+t
print (m)
print (a)