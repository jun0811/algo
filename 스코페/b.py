n = int(input())
arr = list(input())
ans = 1
end = n-1
cur = 0
dp = [0] * 50
dp[0] = 1
dp[1] = 1 if arr[1] =="1" else 0
for i in range(2,n):
    dp[i] = dp[i-1] +dp[i-2] 
    if arr[i] == "0":
        dp[i] = 0

print(dp[end])