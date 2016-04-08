contact=[]
prefix=[]
d = int(input())
for i in range(d):
    contact.append(input().split())
    
b = int(input())
for i in range(b):
    prefix.append(input())
n = int(input())
for i in range(n):
    caller = input()
    for j in prefix:
        if caller in j:
            print("reject "+caller)
            for k in contact:
                if caller==k[0]:print(k[1])

print(contact)
print(prefix)
