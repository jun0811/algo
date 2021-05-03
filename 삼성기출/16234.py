# https://www.acmicpc.net/problem/16234
from collections import deque
import copy
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def bfs(y,x):
    q = deque([])
    q.append([y,x])
    visited[y][x] = 1
    move = deque()
    people, num  = 0, 0
    while q:
        cy,cx = q.popleft()
        move.append([cy,cx])
        people += arr[cy][cx]
        num += 1
        for k in range(4):
            ny = cy + dy[k]
            nx = cx + dx[k]
            if 0 <= nx < n and 0 <= ny <n and not visited[ny][nx]:
                if l <= abs(arr[cy][cx] - arr[ny][nx]) <= r:
                    visited[ny][nx] = num
                    q.append([ny,nx])
    while move:
        y,x = move.popleft()
        arr[y][x] = people//num
    if num == 1:
        return 0
    return 1

n, l, r = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
res = 0

while True:
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for j in range(n):
        for i in range(n):
            if visited[j][i] == 0:
                cnt += bfs(j,i)
    if cnt ==0:
        break
    res += 1
print(res)