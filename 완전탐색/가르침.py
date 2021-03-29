def dfs(cnt,learn,index):
    global maxval
    if index > 26:
        return
    if cnt == K:
        total = 0
        for i in range(N):
            t = word[i]
            ok = True
            for j in range(len(t)):
                if (1<< ord(t[j])-97) & learn != 0:
                    continue
                ok = False
                break
            total += int(ok)
        maxval = max(maxval,total)
        return
    #만약 인덱스가 a,n,t,i,c라면
    if index == 0 or index == 2 or index == 8 or index == 13 or index == 19:
        dfs(cnt,learn,index+1)
    else:
        #배울경우
        dfs(cnt+1,learn|(1<<index),index+1)
        #배우지 않을 경우
        dfs(cnt,learn,index+1)
 
 
N, K =map(int,input().split())
K -= 5
word = [input() for _ in range(N)]
index = 0
#a,n,t,i,c은 이미 배운것으로 처리
index |= (1<< (ord('a')-97))
index |= (1<< (ord('n')-97))
index |= (1<< (ord('t')-97))
index |= (1<< (ord('i')-97))
index |= (1<< (ord('c')-97))
maxval = -1
dfs(0,index,0)
print(maxval)