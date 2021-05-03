# https://www.acmicpc.net/problem/14502
import copy
from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def selectWall(start, count):
    global res
    if count == 3:
        tmp = copy.deepcopy(arr)
        for k in range(len(virus)):
            spread(virus[k][0], virus[k][1], tmp)
        safe = sum(a.count(0) for a in tmp)
        res = max(safe, res)
    else:
        for i in range(start,n*m):
            y = i//m
            x = i% m
            if arr[y][x] == 0:
                arr[y][x] = 1
                selectWall(i, count+1)
                arr[y][x] = 0

def spread(y,x,tmp):
    q = deque()
    q.append([y,x])
    while q:
        cy,cx = q.popleft()
        for k in range(4):
            ny = cy +dy[k]
            nx = cx +dx[k]
            if 0<=ny< n and 0<= nx <m and tmp[ny][nx] == 0:
                tmp[ny][nx] = 2
                q.append([ny,nx])

n, m = map(int,input().split())
arr =[ list(map(int,input().split())) for _ in range(n)]
res= 0
virus = []
for j in range(n):
    for i in range(m):
        if arr[j][i] == 2:
            virus.append([j,i])


selectWall(0,0)
print(res)