n, k = map(int,input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()
dp = [0] * 10001
dp[0] = 1

for a in arr:
    for j in range(a, k+1):
        if j -a >=0:
            dp[j] += dp[j-a]

print(dp[k])