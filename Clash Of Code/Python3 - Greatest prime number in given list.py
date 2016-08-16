def isPrime(n):
	return 2 in[n,2**n%n]

res=0

n = int(input())
for _ in range(n):
    number = int(input())
    if number != 0:
        if isPrime(number):res=max(res,number)

print(res)
