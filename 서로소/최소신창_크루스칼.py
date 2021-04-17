def find(x):
    if p[x] != x:
        p[x] = find(x)
    else:
        return p[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        p[b] = a
    else:
        p[a] = b