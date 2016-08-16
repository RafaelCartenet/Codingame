x1, y1 = [int(i) for i in input().split()]
x2, y2 = [int(i) for i in input().split()]

a=(y2-y1)/(x2-x1)
b=y2-a*x2

print(str(int(a))+"*x"+('','+')[b>=0]+str(int(b)))
