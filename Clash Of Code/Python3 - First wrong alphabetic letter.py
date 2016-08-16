w=input()
print([w[i] for i in range(len(w)) if (w[:i+1]!=''.join(sorted(w[:i+1])))][0])
