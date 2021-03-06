arr = [int(input()) for _ in range(9)]

res = []
for i in range(1<<len(arr)):
    temp = []
    for j in range(len(arr)):
        if i&1<<j:
            temp.append(arr[j])
    if len(temp) == 7 and sum(temp)==100:
        res = temp
        break

res.sort()
for r in res:
    print(r)