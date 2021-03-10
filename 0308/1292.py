def check(n):
    global cnt
    c = 0
    for i in range(1, n):
        if n % i == 0:
            c += 1
        if c == 2:
            return
    cnt += 1


cnt = 0
n = int(input())
arr = list(map(int,input().split()))

for a in arr:
    if a != 1: 
        check(a)
print(cnt)
