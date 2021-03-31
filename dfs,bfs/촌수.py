# https://www.acmicpc.net/problem/2644

def dfs(v,d):
    visited[v] = d
    if v == b:
        return

    for i in arr[v]:
        if not visited[i]:
            dfs(i,d+1)

n = int(input())
a, b = map(int,input().split())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    c,d = map(int,input().split())
    arr[d].append(c)
    arr[c].append(d)
# print(arr)
visited= [0] * (n+1)
# print(a)
dfs(a,1)

if visited[b] == 0:
    print(-1)
else:
    print(visited[b]-1)