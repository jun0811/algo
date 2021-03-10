arrs = [list(map(int, input().split())) for _ in range(10)]
res = arrs[0][1]

cur = arrs[0][1]

for arr in arrs[1:]:
    cur -= arr[0]
    cur += arr[1]

    if res < cur:
        res = cur
print(res)
