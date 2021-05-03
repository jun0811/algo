# https://www.acmicpc.net/problem/17144
import copy

dy = [-1,0,1,0] # 상 우 하 좌
dx = [0,1,0,-1]
def spread(y,x):
    q = []
    for k in range(4):
        ny = y+dy[k]
        nx = x+dx[k]
        if 0<= ny < r and 0<= nx <c and maps[ny][nx] != -1:
            q.append([ny,nx])
    return q

def move1(v,k):
    for i in range(v-1,0,-1):
        maps[i][0] = maps[i-1][0]
    for i in range(c-1):
        maps[0][i] = maps[0][i+1]
    for i in range(v):
        maps[i][c-1] = maps[i+1][c-1]
    for i in range(c-1,0,-1):
        maps[v][i] = maps[v][i-1]
    maps[v][1] = 0

def move2(v,k):
    for i in range(v+1, r-1):
        maps[i][0] = maps[i + 1][0]
    for i in range(c-1):
        maps[r-1][i] = maps[r-1][i + 1]
    for i in range(r-1, v, -1):
        maps[i][c - 1] = maps[i - 1][c - 1]
    for i in range(c-1, 0, -1):
        maps[v][i] = maps[v][i - 1]
    maps[v][1] = 0
r, c, t = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(r)]
cleaner = []
for j in range(r):
        if maps[j][0] == -1:
            cleaner.append(j)

for _ in range(t):
    move = []
    for y in range(r):
        for x in range(c):
            if maps[y][x]>0:
                d = spread(y,x)
                move.append([d,y,x])
    tmp = copy.deepcopy(maps)
    for d, j,i in move:
        dust = tmp[j][i]//5
        for y,x in d:
            maps[y][x] += dust
            maps[j][i] -= dust
    move1(cleaner[0],1)
    move2(cleaner[1],1)
res = 0
for arr in maps:
    res += sum(arr)
print(res+2)


