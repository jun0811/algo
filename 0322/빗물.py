h, w = map(int, input().split())

arr = list(map(int, input().split()))
maxV = max(arr)
max_idx = arr.index(maxV)

    
res = 0
tmp = 0

for i in range(max_idx+1):
    if arr[i] > tmp:
        tmp = arr[i]
    res += tmp


print(res)
