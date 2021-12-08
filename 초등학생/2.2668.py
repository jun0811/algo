def dfs(v,i):
    visited[v] = 1
    for s in load[v]:
        if not visited[s]:
            dfs(s,i)
        elif visited[s] and s ==i:
            print("-----",s)
            res.append(s)


n = int(input())
load = [[] for _ in range(n+1)]

for i in range(1,n+1):
    num = int(input())
    load[i].append(num)
length = 0
res = []
for i in range(1,n+1):
    visited = [0] * (n+1)
    dfs(i,i)

print(len(res))
for r in res:
    print(r)