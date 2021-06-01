n, s = map(int,input().split())

arr = list(map(int, input().split()))


start = 0 
end = 1
inf = 100000000
ans = inf

v = arr[start]

while not(start == end == n):
    if v < s and end < n: # 목표값보다 작고 끝점이 끝에 도달하기 전
        v += arr[end]
        end += 1
    else:
        v -= arr[start]
        start += 1
    if v >= s:
        ans = min(ans, end-start)

if inf == ans:
    print(0)
else:
    print(ans)