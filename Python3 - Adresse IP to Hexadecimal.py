IP = input().split('.')
H = "0x"
for n in IP:
    a = str(hex(int(n)))[2:].upper()
    H += ("", "0")[len(a) == 1] + a
print(H)
