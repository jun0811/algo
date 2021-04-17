from collections import deque
dy = [0,0,-1,1]
dx = [1,-1,0,0]

n, m, y, x, k = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(n)]
# 바닥 좌 위 우 앞 뒤
command = deque(list(map(int, input().split())))
dice = [0,0,0,0,0,0]

def move(dir):
    if dir == 1:
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    elif dir == 2:
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
    elif dir == 3:
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[2]
    else:
        dice[0], dice[2], dice[4], dice[5] = dice[4], dice[5], dice[2], dice[0]


dice[0] = maps[y][x]
while command:
    d = command.popleft()
    x += dx[d-1]
    y += dy[d-1]
    if 0<= x < m and 0 <= y <n:
        move(d)
        if maps[y][x]==0:
            maps[y][x] = dice[0]
        else:
            dice[0] = maps[y][x]
            maps[y][x] = 0
        print(dice[2])
    else:
        y -= dy[d-1]
        x -= dx[d-1]