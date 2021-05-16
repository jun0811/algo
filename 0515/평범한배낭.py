# https://www.acmicpc.net/problem/12865

n,k = map(int,input().split())
dp = [[0]*(k+1) for _ in range(k+1)] # dp
arr = [[0,0]]
for i  in range(n):
    w, v = map(int,input().split())
    arr.append([w,v])


for i in range(1,n+1):
    for j in range(1,k+1):
        if j >= arr[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i][0]] + arr[i][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])