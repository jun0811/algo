from collections import deque

def dfs(v):
    visited[v] = 1
    print(v,end=" ")
    for i in(arr[v]):
        if not visited[i]:
            dfs(i) 

n, m, v = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs(v):
    visited[v] = 1
    q = deque()
    q.append(v)
    while q:
        i = q.popleft()
        print(i, end= " ")
        for a in arr[i]:
            if not visited[a]:
                q.append(a)
                visited[a] = 1


for a in arr:
    a.sort()
visited = [0] * (n+1)
dfs(v)
print()
visited = [0] * (n+1)
bfs(v)