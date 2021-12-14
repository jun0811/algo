n = int(input())
m = int(input())
vips = []
for _ in range(m):
    vips.append(int(input()))
dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]

start = 1
res = 1
for i in range(m):
    cur = vips[i]
    res *= dp[cur-start]
    start = cur+1
res *= dp[n-start+1]
print(res)