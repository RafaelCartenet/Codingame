k=int(input())
n=[1]
for _ in range(k):
    m=[1]
    n.append(0)
    for i in range(1,len(n)):m.append(n[i]+n[i-1])
    n=m
print(*n)
