def isinsquare(x1,y1,x2,y2,x,y):
    return (x>x1)&(x<x2)&(y>y1)&(y<y2)

n = int(input())
for _ in range(n):
    x1, y1, x2, y2, side = [int(j) for j in input().split()]
    if isinsquare(x1-side,y1-side,x1+side,y1+side,x2,y2):print("true")
    else:print("false")
