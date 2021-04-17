from collections import deque
dy = [0,0,-1,1]
dx = [1,-1,0,0]

n, m, y, x, k = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(n)]
# 바닥 앞 위 뒤 좌 우
dice = [0, 0, 0 ,0 ,0 ,0] #
command = deque(list(map(int, input().split())))

def change(c):
    if c==1:
        dice[0], dice[5], dice[2], dice[4] = dice[5], dice[2], dice[4], dice[0]
    if c==2:
        dice[0], dice[4], dice[2], dice[5] = dice[4], dice[2], dice[5], dice[0]
    if c==3:
        dice[0], dice[3],dice[2], dice[1] = dice[3], dice[2], dice[1], dice[0]
    if c==4:
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]


while command:
    c = command.popleft()
    y += dy[c-1]
    x += dx[c-1]
    if 0<=x<m and 0<=y<n:
        change(c)
        if maps[y][x] == 0:
            maps[y][x] = dice[0]
        else:
            dice[0] = maps[y][x]
            maps[y][x] = 0
        print(dice[2])
    else:
        y -= dy[c-1]
        x -= dx[c-1]

