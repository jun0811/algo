# BOJ 1303
from collections import deque
dy = [1,0,-1,0]
dx = [0,1,0,-1] 
def check(y,x, color):
    q = deque()
    q.append([y,x,])
    visited[y][x] = 1
    cnt = 1
    while q:
        y,x = q.popleft()
        for k in range(4):
            newy = y+dy[k]
            newx = x+dx[k]
            if 0<=newy<m and 0<=newx<n:
                # 색갈 비교
                if arr[newy][newx] == color and not visited[newy][newx]:
                    q.append([newy,newx])
                    visited[newy][newx] = 1
                    cnt+=1
    return cnt
n, m = map(int, input().split())

arr = [input() for _ in range(m)]
B = 0
W = 0
visited = [[0]*n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            if arr[i][j] == "B": # 블랙
                B+= (check(i,j,"B") **2)
                
            else:
                W+= (check(i,j,"W") **2) 
print(W,B)