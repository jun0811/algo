n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

dp = [[[0]*3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
# 첫줄
for i in range(2,n):
    if arr[0][x] == 0:
        dp[0][i][0] = 1
# 이동하기
for y in range(n):
    for x in range(2,n):
        if arr[y][x] == arr[y][x-1] == arr[y-1][x] == 0:
            #