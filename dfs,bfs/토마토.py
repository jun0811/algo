from collections import deque
# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 


def bfs():
    global res
    q= deque()
    for j in range(n*h):
        for i in range(m):
            if arr[j][i] == 1:
                q.append([j,i,1])
                visited[j][i] = 1
    if len(q) == (m*n*h):
        res = -2
        return
    while q:
        y,x,d = q.popleft()
        for k in range(6):
            newy = y+dy[k]
            newx = x+dx[k]
            if 0<= newx< m and 0<= newy < (n*h) and arr[newy][newx] !=-1:
                # 값 안에 들어오면
                if not visited[newy][newx]:
                    q.append([newy,newx,d+1])
                    visited[newy][newx] = d+1
                elif visited[newy][newx] > d+1:
                    # 지금 방문한 값이(3) d(1)
                    q.append([newy,newx,d+1])
                    visited[newy][newx] = d+1


m,n,h = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(n*h)]
visited = [[0]*m for _ in range(n*h)] 
res = 0
dx = [0,1,-1,0,0,0]
dy = [1,0,0,-1,n,-n]
bfs()

for j in range(n*h):
    if res==-1 or res== -2:
        break
    for i in range(m):
        if arr[j][i] == 0 and visited[j][i] ==0:
            res = -1
            break
        else:
            if visited[j][i] > res:
                res = visited[j][i]


print(visited) 
if res==-2: print(0)
elif res == -1:
    print(-1)
else:
    print(res-1)
