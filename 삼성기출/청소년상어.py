dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,-1,-1,-1,0,1,1,1]

arr = [[],[],[],[]]
for j in range(4):
    tmp = list(map(int,input().split()))
    for i in range(0,len(tmp),2):
        arr[j].append([tmp[i],tmp[i+1]-1])


fish = [[] for _ in range(17)]
for j in range(4):
    for i in range(4):
        fish[arr[j][i][0]] = [j,i,arr[j][i][1]] # y ,x , 방향
# 먹은 과정
res = 0 # 시작 상어
direction = arr[0][0][1] # 상어 방향
shark_y, shark_x = 0,0
start = arr[0][0][0]
fish[arr[0][0][0]] = [-2,-2,-2] # 물고기 사망
arr[0][0] = [-1,-1] # 상어 위치

def dfs(y,x, d, total,arr, fish):
    global res
    for i in range(1, 17):
        fish_y, fish_x, k = fish[i]
        if k != -1:
           move(fish_y, fish_x, k,arr, fish)
    print(arr)
    print(fish)
    for _ in range(4):
        y += dy[d]
        x += dx[d]
        if y < 0 or y > 3 or x < 0 or x > 3:
            res = max(total, res)
        else:
            if arr[y][x][0] != -2:
                tmp_fish = fish[arr[y][x][0]]
                tmp_arr = arr[y][x]
                fish[arr[y][x][0]] = [-2,-2,-2]
                arr[y][x] = [-1,-1] # 상어 위치
                dfs(y,x,tmp_arr[1], total+tmp_arr[0], arr, fish)
                fish[arr[y][x][0]] = tmp_fish
                arr[y][x] = tmp_arr


def move(y,x,k,arr,fish):
    for i in range(8):
        ny = y+ dy[(k+i)%8]
        nx = x+ dx[(k+i)%8]
        if 0<= ny < 4 and 0<=nx<4 and arr[ny][nx][0]!=-1:
            # 자리를 바꿀수 있으면 물고기 방향 바꿀것 적용하고
            arr[y][x][1] = (k+i)%8 # 물고기 회전한것 적용
            fish[arr[y][x][0]][2] = arr[y][x][1] # 물고기 리스트 방향 바꿔주고
            # 물고기 list에서  y,x 좌표 두개 바꿔주고
            fish[arr[y][x][0]][:2], fish[arr[ny][nx][0]][:2] = fish[arr[ny][nx][0]][:2], fish[arr[y][x][0]][:2]
            # arr
            arr[ny][nx][1], arr[y][x][1] = arr[y][x][1], arr[ny][nx][1] # 방향 바꾸고
            arr[ny][nx][0], arr[y][x][0] = arr[y][x][0], arr[ny][nx][0] # 물고기 바꾸고
            return arr, fish
    # 상어 움직임
dfs(shark_y,shark_x,direction,start ,arr, fish) # 상어

# 물고기 이동
print(arr)
print(res)