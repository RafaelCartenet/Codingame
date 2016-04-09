import math
def isPrime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

n = int(input())

for i in range(2,n+1):
    if isPrime(i):print(i)
    
