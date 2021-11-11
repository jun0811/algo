from collections import deque

def bfs(v):
    visited[v-1] = 1
    q = deque()
    q.append([v,0])
    while q:
        cur, deps = q.popleft()
        for k in friend[cur]:
            if not visited[k-1]:
                q.append([k,deps+1])
                visited[k-1] = 1
    score[v-1] = deps
n = int(input())
friend = [[] for _ in range(n+1)]

while True:
    a, b = map(int,input().split())
    if a== -1 and b==-1:
        break
    friend[a].append(b)
    friend[b].append(a)
    
score = [0] * (n)
for i in range(1,n+1):
    visited = [0] * (n)
    bfs(i)

minV = min(score)
cnt = score.count(minV)
print(minV, cnt)
for i in range(n):
    if score[i] == minV:
        print(i+1,end=" ")