import sys

n = int(input())  # 작업장의수
lines = []
for i in range(n-1):
    # a 작업 시간 | b 작업시간  |  a->b 이동시간 |  b->a 시간
    arr = list(map(int, input().split()))
    lines.append(arr)
finalA, finalB = map(int, input().split())

dp = [[0] for _ in range(n)]
if lines[0][0] < lines[0][1]:
    dp[0][0] = lines[0][0]
    dp[0].append("A")
else:
    dp[0][0] = lines[0][1]
    dp[0].append("B")

for i in range(1, n):
    tmp = 0
    loc = dp[i-1][1]  # 현재 위치
    if dp[i-1][1] == 'A':
        if i < n-1:
            a_to_b = lines[i-1][2] + lines[i][1]  # a에서 b 이동 + b 작업시간
            a = lines[i][0]
        else:
            a_to_b = lines[i-1][2] + finalB
            a = finalA
        if a_to_b < a:
            tmp = a_to_b
            loc = "B"
        else:
            tmp = a

    else:
        if i < n-1:
            b_to_a = lines[i-1][3] + lines[i][0]
            b = lines[i][1]
        else:
            b_to_a = lines[i-1][3] + finalA
            b = finalB
        if b_to_a < b:
            tmp = b_to_a
            loc = "A"
        else:
            tmp = b
    dp[i][0] = dp[i-1][0] + tmp
    dp[i].append(loc)
# 마지막 작업장


print(dp[n-1][0])
