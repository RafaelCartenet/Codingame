c = input()[1:]
nb = [c[2*i:2*(i+1)] for i in range(3)]

result = '#'
for n in nb:
    new = str(hex(int(255-int(n,16))))[2:].upper()
    if len(new) == 1:
        new = '0' + new
    result += new

print(result)
