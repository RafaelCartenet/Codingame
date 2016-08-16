h=int(input().split()[1])
T=[input()for _ in range(h)]
for j in range(len(T[0])):print(*[T[i][j]for i in range(h-1,-1,-1)],sep='')
