i=0
j=1
s=input().split()
l=[s[0]]
for k in s[1:]:
    l.append(j*(k[:2]+"-")+k)
    j,i=j+i,j
print(*l)