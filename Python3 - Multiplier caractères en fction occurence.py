d={}
T=''
for c in input():
    if c in d:
        d[c]+=1
        T+=d[c]*c
    else:
        d[c]=1
        T+=c
print(T)
