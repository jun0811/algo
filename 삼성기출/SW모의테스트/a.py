import sys
import copy
sys.stdin = open('test')

dy= [-1,0,1,0]
dx= [0,1,0,-1]

def invision(y,x, arr, temp_arr1,temp_arr):
    total = 0
    # 침략하는 곳 병사
    tmp=temp_arr1[y][x]
    q = []
    current = 0
    if [y,x] in first:
        current = 0
    if [y,x] in second:
        current = 1
    if [y,x] in third:
        current = 2
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < n and 0 <= nx < n:
            if [ny,nx] in temp_arr: # 내 국가가 있으면 일단 센다
                q.append([ny,nx])
                total += temp_arr1[ny][nx]
    # 주변 지역 체크 후 병사 확인
    if total > tmp*5:
        s = 0
        while q:
            # 병력 차출
            cy, cx = q.pop()
            arr1[cy][cx] -= temp_arr1[cy][cx] // 4
            s += temp_arr1[cy][cx] // 4 # 공격 병력
        arr1[y][x] = s - arr1[y][x] # 남은 병력
        # 지역 소속 변경
        arr.append([y,x])
        if current == 0:
            first.pop(first.index([y,x]))
        if current == 1:
            second.pop(second.index([y,x]))
        if current == 2:
            third.pop(third.index([y,x]))

def attack(arr):
    # 주변 국가 탐색
    temp_arr1 = copy.deepcopy(arr1)
    temp_arr = copy.deepcopy(arr)
    for a in arr:
        y,x = a
        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if 0<=ny<n and 0<=nx<n:
                # 다른 나라가 있다면
                if [ny,nx] not in arr and arr1[ny][nx] != 0: # 내 나라가 아니면 탐색
                    invision(ny,nx, arr, temp_arr1, temp_arr) # 좌표 , 침공하는 나라


def support(arr):
    temp_arr1 = copy.deepcopy(arr1)
    for a in arr:
        y, x = a
        q = []
        check = True  # 인접한 국가 체크

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < n:
                # 다른 나라가 있다면
                if [ny, nx] in arr:  # 내 나라 탐색
                    q.append([ny,nx])
                elif arr1[ny][nx] == 0:
                    continue
                else:
                    check = False
        s = temp_arr1[y][x] //5 # 지원 병력
        if check:# 주변에 아군만 있을 때 무조건 보내기
            while q:
                ny,nx = q.pop() # 지원 갈곳
                arr1[ny][nx] += s # 병력 지원
                arr1[y][x] -= s # 병력 감소
        else:
            while q:
                ny,nx = q.pop()
                if arr1[ny][nx] * 5 < arr1[y][x]:
                    arr1[ny][nx] += s  # 병력 지원
                    arr1[y][x] -= s  # 병력 감소

def supply():
    for j in range(n):
        for i in range(n):
            arr1[j][i] += arr2[j][i]


for tc in range(1,int(input())+1):
    n = int(input()) # 지도크기
    maps = [list(map(int,input().split())) for _ in range(n)] # 나라
    arr1 = [list(map(int,input().split())) for _ in range(n)] # 병력
    arr2 = [list(map(int,input().split())) for _ in range(n)] # 보충
    first = []
    second = []
    third = []
    for j in range(n):
        for i in range(n):
            if maps[j][i] == 1:
                first.append([j,i])
            if maps[j][i] == 2:
                second.append([j,i])
            if maps[j][i] == 3:
                third.append([j,i])
    location = len(first) + len(second) + len(third)
    while True:
        # 공격 탐색
        if first:
            attack(first)
            support(first)
            supply()
        print(arr1)

        if second:
            attack(second)
            support(second)
            supply()
        print(arr1)

        if third:
            attack(third)
            support(third)
            supply()
        print(arr1)

        print(first)
        print(second)
        print(third)
        if location == len(first) or location == len(second) or location == len(third):
            break
    res = 0
    for j in range(n):
        res += sum(arr1[j])


    print('#{} {}'.format(tc, res))
