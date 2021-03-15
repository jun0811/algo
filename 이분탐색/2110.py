n, c =map(int,input().split())

x = [int(input()) for _ in range(n)]
x.sort()
res = 0
start = 1 # 최소 거리 
end = x[-1] - x[0]
while (start<=end):
    mid = (start+end) // 2
    count = 1 
    cur = x[0] # 공유기 설치
    for i in range(1,n):
        if mid <= x[i]-cur:
            count+=1
            cur = x[i]
    # print(count)
    # 공유기 갯수 구함
    if count < c: # 공유기 갯수가 모자라면....
        # 간격을 좁힌다. 
        end = mid -1 
    else:
        res = mid
        start = mid +1

print(res)