l, h = list(map(int, input().split()))

compt = 1
T = [[0 for _ in range(l)] for _ in range(h)]

Mii, Mai = 0, h
Mij, Maj = 0, l
dirj = 1
diri = 1
i = 0
j=0

direction = 1

def change(nombre):
    res = str(nombre)
    if len(res) != 2:
        res = '0'+res
    return res

while compt <= l*h:
    if direction == 1:
        if dirj == 1:
            for j in range(Mij, Maj, 1):
                T[i][j] = compt
                compt += 1
            Mii += 1
            dirj = -1
        else:
            for j in range(Maj - 1, Mij-1, -1):
                T[i][j] = compt
                compt += 1
            Mai -= 1
            dirj = 1
        direction = -1
    else:
        if diri == 1:
            for i in range(Mii, Mai, 1):
                T[i][j] = compt
                compt += 1
            Maj -= 1
            diri = -1
        else:
            for i in range(Mai - 1, Mii-1, -1):
                T[i][j] = compt
                compt += 1
            Mij += 1
            diri = 1
        direction = 1

T = [list(map(change, T[i])) for i in range(h)]
for i in range(h):
    print(*T[i])
