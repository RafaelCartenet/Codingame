import sys
import math

def next(T,x,y,width,height):
    for i in range(3):
        for j in range(3):
            if (i-1>=0) & (j-1>=0) & (i-1<height) & (j-1<width):
                if (i-1!=x)&(j-1!=y):
                    if T[i-1][j-1]=='.':
                        print(i-1)
                        print(j-1)
                        x=i-1
                        y=j-1
                        break
                    

x, y = [int(i) for i in input().split()]

width, height = [int(i) for i in input().split()]
T=[[j for j in input().split()] for i in range(height)]

print(T)
print(x)
print(y)

next(T,x,y,width,height)
print(x)
print(y)
