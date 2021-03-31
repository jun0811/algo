n, time = input().split()
playlist = []
for i in range(int(n)):
    playlist.append(input())

res = 0
cur = 0
arr = list(map(int,time.split(":")))
total_time = arr[0]*3600 + arr[1] *60 + arr[2]
# print(total_time)

for i in range(int(n)):
    tmp = 0
    cnt = 0
    for j in range(i,int(n)):
        tmp += int(playlist[j][:2]) * 60 # 분 
        tmp += int(playlist[j][3:5]) # 시간
        if total_time > tmp:
            cnt +=1
        else:
            cnt+=1
            if cnt > res:
                res = cnt
                cur = i
            break
print(res, cur+1)
