import copy

def r(k):
    y, c, k = rotation[k]
    d = 1
    if c == 1:
        d = -1
    for j in range(y, n+1, y):
        tmp = arr[j - 1][::]
        for i in range(m):
            arr[j-1][i] = tmp[(i-d*k)%m]

def remove(y,x):
    global check
    q = [(y,x)]
    for k in range(4):
        ny = (y+ dy[k])
        nx = (x +dx[k]) % m
        if 0<=ny< n and temp[ny][nx] == temp[y][x]:
            q.append((ny,nx))
    
    if len(q)>1:
        while q:
            cy, cx = q.pop()
            arr[cy][cx] = 0
            check = True

n, m, t = map(int,input().split())
dy = [-1,0,1,0]
dx = [0,-1,0,1]

arr = [list(map(int,input().split())) for _ in range(n)]
rotation = []
for _ in range(t):
    x, d, k = map(int,input().split())
    # x의 배수 원판을 (0 :시계, 1: 반시계)로 k만큼 돌린다/
    rotation.append([x,d,k])

for k in range(t):
    r(k)
    check = False
    temp = copy.deepcopy(arr)
    for j in range(n):
        for i in range(m):
            if arr[j][i]>0:
                remove(j,i)

    if not check:
        total = 0
        q = []
        for j in range(n):
            for i in range(m):
                if arr[j][i]: 
                    q.append([j,i])
                    total += arr[j][i]
        if len(q)>0:
            mean = total/len(q)
        else: break
        while q:
            y,x = q.pop()
            if arr[y][x] > mean:
                arr[y][x] -= 1
            elif arr[y][x]< mean: arr[y][x] += 1
res = 0
for a in arr:
    res += sum(a)
print(res)