# 7
# 1 2
# 8 7
# 20 10
# 20 20
# 15 12
# 12 14
# 11 12

n = int(input())
paper = []
dp = [0] *n

for _ in range(n):
    a,b = map(int,input().split())
    paper.append(sorted([a,b]))
    # 짧은게 세로
paper.sort(key=lambda x:(x[0],x[1])) 
# print(paper)
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if paper[i][1] >= paper[j][1]:
            dp[i] = max(dp[j]+1,dp[i])
print(max(dp))