import heapq

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(y,x):
    global size, feed, time
    h = [ ]
    heapq.heappush(h,[0,y,x])
    visited = [[0] *n for _ in range(n)]
    visited[y][x] = 1
    while h:
        d, cy,cx, = heapq.heappop(h)
        if 0 <arr[cy][cx] < size : # 작은 물고기를 찾앗을 때.
            fish.pop(fish.index([cy,cx]))
            arr[cy][cx] = 0
            feed += 1
            if feed == size:
                feed=0
                size +=1
            time += d
            return [cy,cx]
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<n and 0<=nx<n and not visited[ny][nx] and arr[ny][nx] <= size:
                # 방문하지 않고 물고기 사이즈가 자기보다 작을 때
                visited[ny][nx] = 1
                heapq.heappush(h,[d+1,ny,nx])
    return [-1,-1]


n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
# 아기상어 크기는 2
# 크기가 같으면 지나갈수 있고 크면 지나가지도 못하고
# 크기가 작으면 먹을수 있다.
# 물고기 많다면 가장 위의 물고기, 여러마리면 가장 왼쪽
time = 0 # 결과
sy,sx = 0, 0 # 시작 위치
fish = [ ]
for j in range(n):
    for i in range(n):
        if arr[j][i] == 9:
            sy,sx = j,i
        elif arr[j][i]>0:
            fish.append([j,i])

# 아기상어
size = 2
feed = 0 # 물고기 먹은 수
arr[sy][sx] = 0
while fish:
    sy,sx = bfs(sy,sx)
    if sy == -1:
        break

print(time)