# https://www.acmicpc.net/problem/14502
import copy
dy = [-1,0,1,0]
dx = [0,1,0,-1]

n, m = map(int,input().split())
arr =[ list(map(int,input().split())) for _ in range(n)]

res = 0
virus = []
for j in range(n):
    for i in range(m):
        if arr[j][i] == 2:
            virus.append([j,i])

def wall(start, count):
    global res
    if count == 3: # 벽 3개 골랏으면
        tmp = copy.deepcopy(arr)
        for num in range(len(virus)):
            y,x = virus[num]
            spread(y,x,tmp)
        safe = sum(i.count(0) for i in tmp)
        res = max(res, safe)
    else:
        for i in range(start, n*m): # 2차원 배열에서 조합 구하기
            y = i//m
            x = i%m
            if arr[y][x] == 0:
                arr[y][x] = 1 # 벽 변경
                wall(i,count+1)
                arr[y][x] = 0

def spread(y,x, tmp):
    if tmp[y][x] == 2:
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0<= ny < n and 0<= nx <m:
                if tmp[ny][nx] == 0:
                    tmp[ny][nx] = 2
                    spread(ny,nx,tmp)
wall(0,0)
print(res)