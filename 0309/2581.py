def check(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1


m = int(input())
n = int(input())

arr = []

for i in range(m,n+1):
    if check(i) and i>1:
        arr.append(i)

if len(arr):
    print(sum(arr))
    print(arr[0])
else:
    print(-1)