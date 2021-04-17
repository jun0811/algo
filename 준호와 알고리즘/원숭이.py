from collections import deque

dy = [-1,0,1,0] # 원숭이
dx = [0,1,0,-1] # 원숭이
hy = [-2, -2, -1, 1, 2, 2, 1, -1]
hx = [-1, 1, 2, 2, 1, -1, -2, -2]

def bfs():
    global res
    q = deque()
    q.append([0,0,0])
    while q:
        y,x,z = q.popleft()
        # 도착
        if y == h-1 and x == w-1:
            res = visited[y][x][z]
            return
        for k in range(4):
            newY = y + dy[k]
            newX = x + dx[k]
            if 0<=newY<h and 0<=newX<w:
                # 장애물이 없고 방문한적 없으면
                if arr[newY][newX] != 1 and not visited[newY][newX][z]:
                    visited[newY][newX][z] = visited[y][x][z] + 1
                    q.append([newY,newX,z])
        if z<c:
            for k in range(8):
                newY = y + hy[k]
                newX = x + hx[k]
                if 0<=newY<h and 0<=newX<w:
                    # 장애물이 없고 방문한적 없으면
                    if arr[newY][newX] != 1 and not visited[newY][newX][z+1]:
                        visited[newY][newX][z+1] = visited[y][x][z] + 1
                        q.append([newY,newX,z+1])

c = int(input())
w,h = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(h)]

visited = [[[0 for i in range(31)] for i in range(w)] for i in range(h)]  # 0 부터 30까지

res = 0
bfs()
if w-1==0 and h-1==0:
    print(0)
elif res==0:
    print(-1)
else:
    print(res)
