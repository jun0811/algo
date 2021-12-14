def backpack(cur, weight,cur_value):# cur : 인덱스 , cur_value: 가치 
    # cur == 4
    print(cur, weight)
    if cur >= n or weight > k: return
    if cur != 0: dp[cur][weight] = max(dp[cur-1][weight] , dp[cur-1][weight] +cur_value )     
    # 넣고  cur 3이면 끝 4 되면 아웃 
    backpack(cur+1, weight + arr[cur][0], cur_value +arr[cur][1]) 
    # 안넣고
    backpack(cur+1, weight, cur_value)

n, k = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

# 1. for문 
for i in range(1,n+1):
    w, v = arr[i-1]
    for j in range(1,k+1):
        if w <=j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][k])


#