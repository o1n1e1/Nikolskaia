import sys
import random
from random import randint
q = []
n = input ("Enter n ")
m = input ("Enter m ")
a = 0
if not (n.isdigit() and m.isdigit()):
	print ("N and/or M is not a digit")
	sys.exit()
m = int(m)
n = int(n)
for i in range (n):
	q.append ([])
	for j in range (m):
		q[i].append(randint (0,9))
for i in q:
	for j in i:
		if j == 7 : a = a+1
print (q)
print (a)