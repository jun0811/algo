from collections import deque

dy= [-1,0,1,0]
dx = [0,1,0,-1]

def other(y,x):
    global ans
    total = arr[y][x]
    cnt = 0
    for k in range(4):
        newy = y + dy[k]
        newx = x + dx[k]
        if 0<=newy<n and 0<=newx<m:
            cnt+=1
            total += arr[newy][newx]
    if cnt ==3:
        ans = max(ans,total)
        return
    elif cnt == 4:
        for k in range(4):
            newy = y + dy[k]
            newx = x + dx[k]
            total -= arr[newy][newx]
            ans = max(ans,total)
            total += arr[newy][newx]

def dfs(y,x, total, visited):
    global ans
    if len(visited) == 4:
        ans = max(ans,total)
        return
    else:
        for k in range(4):
            newx = x + dx[k]
            newy = y + dy[k]
            if 0 <= newx<m and 0<=newy<n:
                if [newy,newx] not in visited:
                    visited.append([newy,newx])
                    dfs(newy,newx, total + arr[newy][newx], visited)
                    visited.pop()


n,m = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for y in range(n):
    for x in range(m):
        dfs(y,x, arr[y][x], [[y,x]])
        other(y,x) #  ㅏㅓㅗㅜ

print(ans)