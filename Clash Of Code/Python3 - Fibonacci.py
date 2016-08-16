n = int(input())

if n==1:print("0")
elif n==2:print("0 1")
else:
    res = [0,1]
    for _ in range(2,n):
        res.append(res[-1]+res[-2])
    print(*res)
