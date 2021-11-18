from collections import deque
# 치즈
dy = [0,0,1,-1]
dx = [1,-1,0,0]
def bfs():
    visited = [[0]*x for _ in range(y)]
    q = deque()
    cnt = 0
    q.append([0,0])
    visited[0][0] = 1
    while q:
        cy, cx = q.popleft()
        for k in range(4):
            ny = cy + dy[k]
            nx = cx + dx[k]
            if 0<=ny<y and 0<= nx < x and not visited[ny][nx]:
                visited[ny][nx] = 1
                if arr[ny][nx] == 0:
                    q.append([ny,nx])
                else:
                    arr[ny][nx] = 0
                    cnt += 1
    return cnt
y, x = map(int,input().split())

arr = []
for _ in range(y):
    tmp = list(map(int,input().split()))
    arr.append(tmp)
time = 0
cheese = []
while True:
    time += 1
    cnt = bfs()
    cheese.append(cnt)
    if cnt ==0:
        break
print(time-1)
print(cheese[-2])