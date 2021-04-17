n = int(input())
arr = list(map(int,input().split()))
b, c = map(int,input().split())

ans = 0 # 감독관 수

for a in arr:
    num = a
    num -= b
    ans += 1
    if num <= 0:
        continue
    if num%c:
        ans += (num//c +1)
    else:
        ans += num//c
print(ans)

