n = int(input())
ans = 0

for i in range(1,n-1):
    for j in range(i,n-1):
        for k in range(j,n-1):
            if i+j > k and i+j+k == n:
                ans+=1

print(ans)