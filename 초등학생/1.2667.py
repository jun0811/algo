dy = [1,0,-1,0]
dx = [0,-1,0,1]

def dfs(y,x):
    global t
    t += 1
    visited[y][x] = 1
    for k in range(4):
        ny = dy[k] + y
        nx = dx[k] + x
        if 0<=ny<N and 0<=nx <N and not visited[ny][nx] and arr[ny][nx] == 1:
            dfs(ny,nx)
            
N = int(input())
visited = [[0]*N for _ in range(N)]
arr =[]
total = []
for i in range(N):
    arr.append(list(map(int,input())))
t=0
for i in range(N):
    for j in range(N):
        if not visited[i][j] and arr[i][j]==1:
            dfs(i,j)
            total.append(t)
            t=0
            
print(len(total))
total.sort()
for t in (total):
    print(t)