from collections import deque

dy = [1,0,0,-1]
dx = [0,1,-1,0]

def bfs(y,x):
    global resx, minV, startx, res
    q = deque()
    q.append([y,x,0,0])
    visited[y][x] = 1
    while q:
        curY,curX,cnt,move = q.popleft()
        if [curY,curX] in end:
            if minV >= move:
                minV = move
                resx = curX # 도착지점 
        else:
            for k in range(4):
                tmp =0
                if k ==1 or k==2:
                    tmp =1
                newY = curY +dy[k]
                newX = curX +dx[k]
                if 0<=newY<m and 0<=newX<n:
                    if not visited[newY][newX] and arr[newY][newX] == ".":
                        q.append([newY,newX,cnt+1, move+tmp])
                        visited[newY][newX] = 1

n, m = map(int,input().split())
arr = [list(input()) for _ in range(m)]

end = []
start = []
minV = 10**10
resy = m
resx = -1
res = 0
for i in range(n):
    if arr[0][i] == "c":
        start.append([0,i])
    if arr[m-1][i] == ".":
        end.append([m-1,i])

for y,x in start:
    visited= [[0]*n for _ in range(m)]
    bfs(y,x)
if resx == -1:
    print(-1)
else:
    print(minV)       