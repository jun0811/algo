n = int(input())
guest = [0]+list(map(int,input().split()))
mini_train = int(input())

dp = [[0 for _ in range(n+1)] for _ in range(4)]

for i in range(1,4):
    for j in range(mini_train*i, n+1):
        # print(guest[j-mini_train] , guest[j-mini_train +1])
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-mini_train] + sum(guest[j-mini_train+1:j+1]) )
print(dp[3][n])