from collections import deque
dy = [0,0,1,-1]
dx = [1,-1,0,0]

def bfs():
    visited = [[0]*5 for _ in range(5)]
    q = deque()
    visited[0][0] = 1
    q.append([0,0,1])
    while q:
        cy,cx,cnt = q.popleft()
        print(cy,cx)
        for k in range(4):
            ny = cy+ dy[k]
            nx = cx+ dx[k]
            if 0<=ny<5 and 0<=nx<5 and not visited[ny][nx]:
                visited[ny][nx] = cnt+1
                q.append([ny,nx, cnt+1])
    print(visited)
arr = [[1]*5 for _ in range(5)]

bfs()
# dfs()