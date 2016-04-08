mdp = input()
ch = 0
mi = 0
ma = 0

if len(mdp) >= 8:
    for i in mdp:
        a = ord(i)
        if (a <= 57) & (a >= 48):
            ch = 1
        elif (a <= 90) & (a >= 65):
            ma = 1
        elif (a <= 122) & (a >= 97):
            mi = 1
        if mi == 1 & ma == 1 & ch == 1:
            break
    if mi == ch == ma == 1:
        print("True")
    else:
        print("False")
else:
    print("False")
