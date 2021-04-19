# import sys
import heapq
# sys.stdin= open('test')
dx = [0,1,0,-1]
dy = [1,0,-1,0]
# 손님
def guest(sy,sx):
    global k
    h = []
    heapq.heappush(h,[0,sy,sx])
    visited = [[0]*n for _ in range(n)]
    visited[sy][sx] = 1
    while h:
        # h.sort(lambda x: x[1])
        d, cy,cx = heapq.heappop(h) # 이동거리, 현대 위치
        if [cy,cx] in s:
            h = []
            return [d,cy,cx] #
        if k < d:
            continue
        for i in range(4):
            newy = cy + dy[i]
            newx = cx + dx[i]
            if 0<= newy <n and 0<= newx<n and not visited[newy][newx] and arr[newy][newx] != 1:
                heapq.heappush(h, [d+1,newy,newx])
                visited[newy][newx] = 1
    return [-1, -1, -1]


def goal(sy,sx):
    global k
    idx = s.index([sy,sx])
    h = []
    heapq.heappush(h,[0,sy,sx])
    visited = [[0]*n for _ in range(n)]
    visited[sy][sx] = 1
    while h:
        d, cy,cx = heapq.heappop(h) # 이동거리, 현대 위치
        if [cy,cx] == e[idx]:
            h = []
            e.pop(idx)
            s.pop(idx)
            return [d,cy,cx] #
        if k < d:
            continue
        for i in range(4):
            newy = cy + dy[i]
            newx = cx + dx[i]
            if 0<= newy <n and 0<= newx<n and not visited[newy][newx] and arr[newy][newx] != 1:
                heapq.heappush(h, [d+1,newy,newx])
                visited[newy][newx] = 1
    return [-1,-1,-1]

n,m,k = map(int,input().split())
# 0은 빈킨 1은 벽
# arr : 활동 지도
arr = [list(map(int,input().split())) for _ in range(n)]

# 운전 시작 행 열
y, x = map(int,input().split())
#
s = [] # 시작
e = [] # 도착
for _ in range(m):
    s_y,s_x,e_y,e_x = map(int,input().split())
    s.append([s_y-1,s_x-1])
    e.append([e_y-1,e_x-1])

y -= 1
x -= 1
res = 0

for _ in range(m):
    d1,nexty,nextx = guest(y,x)
    if k < d1 or d1 ==-1:
        d1= -1
        break
    k -= d1
    d2,y,x = goal(nexty,nextx)

    if k < d2 or d2 ==-1:
        d2 = -1
        break
    k -= d2
    k += (d2)*2
if d1 == -1 or d2 == -1:
    print(-1)
else:
    print(k)