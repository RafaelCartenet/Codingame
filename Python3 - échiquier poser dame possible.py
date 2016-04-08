E = []
Q = []
res = ["PPPPPPPP"] * 8
for i in range(8):
    a = input()
    E.append(a)
    ind = [i for i in range(8) if a[i] == "Q"]
    for q in ind:
        Q.append([q, i])

for queen in Q:
    for i in range(8):
        if queen[1] == i:
            res[i] = "........"
        else:
            for j in range(8):
                if (res[i][j] == "P") & ((queen[0] == j) | (abs(queen[0] - j) == abs(queen[1] - i))):
                    res[i] = res[i][:j] + "." + res[i][j + 1:]
print(*res, sep='\n')
