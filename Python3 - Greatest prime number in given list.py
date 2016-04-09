def isPrime(n):
	return 2 in[n,2**n%n]

l=[]
n = int(input())
for _ in range(n):
    number = int(input())
    if number != 0:
        if isPrime(number):l.append(number)

print(max(l))
