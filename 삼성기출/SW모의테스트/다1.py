def find(v):
    if p[v] == v:
        return v
    else:
        x = find(p[v])
        p[v] = x
        return x

def union(x,y):
    x = find(x)
    y = find(y)
    if x!=y:
        p[y] = x




v, e = map(int,input().split())
g = []
p = [i for i in range(v+1)]

for _ in range(e):
    a,b,c = map(int,input().split())
    g.append([c,a,b])

g.sort(key=lambda x:x[0])
mst = 0
cnt = 0
for i in range(e):
    w = g[i][0]
    s = g[i][1]
    e = g[i][2]
    if find(s) != find(e):
        union(s,e)
        mst += w
        cnt += 1
    if cnt == v-1:
        break
print(mst)