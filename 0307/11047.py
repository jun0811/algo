n,k = map(int,input().split())
arr = [int(input()) for _ in range(n)]
cnt = 0
for i in range(len(arr)-1,-1,-1):
    # 제일 큰 동전부터 고른다. 
    # 동전이 더 크면 
    temp = (k//arr[i])

    k -= (arr[i]*temp)
    cnt += temp
    if k==0:
        break
print(cnt)