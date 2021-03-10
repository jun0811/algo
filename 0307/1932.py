n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

dp = [[] for _ in range(len(arr))] 
for i in range(len(arr)):
    for _ in range(len(arr[i])):
        dp[i].append(0)


dp[0][0] = arr[0][0]
for i in range(1,len(arr)):
    # i번째 dp 구하기 
    for j in range(len(arr[i])):
        if  j==0: dp[i][j] = dp[i-1][j] +arr[i][j]
        elif (j+1) == len(arr[i]): dp[i][j] = dp[i-1][j-1] +arr[i][j]
        else:
            temp1 = dp[i-1][j-1] +arr[i][j]
            temp2 = dp[i-1][j] + arr[i][j]
            if temp1 > temp2:
                dp[i][j] = temp1
            else: dp[i][j] = temp2
print(max(dp[len(arr)-1]))
