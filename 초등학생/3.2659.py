def check(a, n):
    minV = n
    for _ in range(4):
        t = a[1:] + [a[0]]
        a = t
        minV = min(minV, int(''.join(t)))
    if minV == n:
        return True
    return False        

arr = list(input().split())
minV = 99999
res = 0 
clock_num = []
# 시계수 구하기 
for _ in range(4):
    tmp = arr[1:] + [arr[0]]
    arr = tmp
    minV = min(minV, int(''.join(tmp)))

for i in range(1111, minV):
    tmp = list(str(i))
    if "0" in tmp:
        continue
    isWhat = check(tmp, i)
    if isWhat:
       res += 1
print(res+1)