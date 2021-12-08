n = int(input()) # 추 갯수
chu = list(map(int,input().split()))
num = int(input()) # 구슬 갯수 
gu = list(map(int,input().split()))

s,e = 0, 0
p = set()
while s != n and e !=n:
    for i in range(e,n):
        tmp = sum(chu[s:i+1])
        print(tmp)
        p.add(tmp)
    s+= 1
    e+= 1
p = list(p)
# print(p)
for g in gu:
    if g in p:
        print('Y')
    else:
        print('N')