n = int(input())
origin = list(map(int,input().split()))
sample = origin[::]
standard = []
for _ in range(n):
    sample = sample[1:] + [sample[0]]
    standard.append(sample[::])
# print(sample)
for i in range(n):
    sample[i] = sample[i]+2 if (sample[i]+2) <= 4 else (sample[i]+2)%4
# print(sample)
sample.reverse()
for _ in range(n):
    sample = sample[1:] + [sample[0]]
    standard.append(sample[::])
    
t = int(input())
res = []
for _ in range(t):
    tmp = list(map(int,input().split()))
    if tmp in standard:
        res.append(tmp)
        
print(len(res))
for arr in res:
    for a in arr:
        print(a,end=" ")
    print("")
    