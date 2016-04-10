def isPrime(n):
	return 2 in[n,2**n%n]

n = int(input())
m=n-1
o=n+1
while not isPrime(m):m-=1
while not isPrime(o):o+=1
moy=(m+o)/2
if n < moy:print("WEAK")
elif n > moy:print("STRONG")
else:print("BALANCED")
