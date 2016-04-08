w=input().lower()
print(("false","true")[True in[w[i]==w[i+1]for i in range(len(w)-1)]])

s=input().lower()
print(str(any(s[i]==s[i+1]for i in range(len(s)-1))).lower())
