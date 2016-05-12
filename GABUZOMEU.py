l=['GA','BU','ZO','MEU']
n=int(input())
t=''
if n==0:print('GA')
else:
    while n>0:t=l[n%4]+t;n//=4;
    print(t)
