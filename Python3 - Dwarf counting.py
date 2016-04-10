a=["one","two","three"]

LOTS=0
MANY=0
REST=0

chaine=[]

nb = int(input())

while (nb>0):
    if (nb//16)!=0:
        LOTS += nb//16
        nb = nb%16
    elif (nb//4)!=0:
        MANY += nb//4
        nb = nb%4
    else:
        REST = nb
        nb=0

for _ in range(LOTS):chaine.append("LOTS")
for _ in range(MANY):chaine.append("many")
if REST!=0:chaine.append(a[REST-1])

print(*chaine,sep='-')
