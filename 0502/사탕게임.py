dy = [-1,0,1,0]
dx = [0,1,0,-1]

def candy(arr):
    global res
    for j in range(n):
        cnt = 1
        color = arr[j][0]
        for i in range(1,n):
            if arr[j][i] == color:
                cnt += 1
                if cnt > res:
                    res = cnt
            else:
                color = arr[j][i]
                cnt = 1
    for i in range(n):
        cnt = 1
        color = arr[0][i]
        for j in range(1,n):
            if arr[j][i] == color:
                cnt += 1
                if cnt > res:
                    res= cnt
            else:
                color = arr[j][i]
                cnt = 1

            
def search(y,x,tmp):
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<n and 0<=nx<n and tmp[y][x] != tmp[ny][nx]:
            tmp[ny][nx], tmp[y][x] = tmp[y][x], tmp[ny][nx]
            candy(tmp)
            tmp[ny][nx], tmp[y][x] = tmp[y][x], tmp[ny][nx]


n = int(input())
arr = [list(input()) for _ in range(n)]

res=0

for j in range(n):
    for i in range(n):
        search(j,i,arr)

print(res)