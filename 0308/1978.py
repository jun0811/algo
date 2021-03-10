a,b =map(int,input().split())

dp = [] 
for i in range(1,b+1):
    for _ in range(i):
        dp.append(i)

arr_b = dp[:b]
arr_a = dp[:a-1]
print(sum(arr_b)-sum(arr_a))