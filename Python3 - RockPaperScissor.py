dic = ["ROCK","PAPER","SCISSOR","PAPER","SCISSOR","ROCK"]

n = int(input())

for i in range(n):
    coups=[]
    s = input().split()
    ok = 0
    for coup in s:
        if coup not in dic:
            print("CHEATER")
            ok = -1
            break
        else:
            coups.append(dic[dic.index(coup)+3])
    if ok == 0:print(*coups)
