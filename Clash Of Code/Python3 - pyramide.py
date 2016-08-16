n=int(input())
for j in range(2*n-1):
    print(*[max(abs(min(j,2*n-2-j)-n),abs(min(i,2*n-2-i)-n))for i in range(2*n-1)], sep='')