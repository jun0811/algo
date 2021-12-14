from collections import deque
dy = [0,1,-1,0]
dx = [1,0,0,-1]
def check(i,j):
    visited[i][j] = 1
    q = deque()
    q.append([i,j])
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            newX = cx + dx[k]
            newY = cy + dy[k]
            if 0<=newY < m and 0<=newX < n and not visited[newX][newY] and arr[newX][newY]>0:
                q.append([newX,newY])
                visited[newX][newY] = 1

n, m = map(int,input().split())
arr = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    arr.append(tmp)

res = 0 # 시간 

island = 0
clear = False
while True:
    visited = [[0 for _ in range(m)] for _ in range(n)]
    island = 0
    
    # 녹이기
    cur_arr = []
    for a in arr:
        cur_arr.append(a[::])
    for i in range(n):
        for j in range(m):
            if cur_arr[i][j]>0:
                cnt = 0
                for k in range(4):
                    nx = i +dx[k]
                    ny = j +dy[k]
                    if 0<=ny < m and 0<=nx< n and cur_arr[nx][ny]<=0:
                        cnt +=1
                arr[i][j] -= cnt
            
    clear = True
    res += 1
                
    for i in range(n):
        for j in range(m):
            if arr[i][j]>0 and visited[i][j]==0:
                clear = False
                check(i,j)
                island += 1
            if arr[i][j] <0: arr[i][j] = 0
    if clear : 
        res = 0
        break
    if island>2:
        break

print(res)
                        
    