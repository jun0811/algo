
ans = "0"

def dfs(v,visit,numbers,value):
    global ans
    visit[v]= 1
    if 0 not in visit:
        if int(value) > int(ans):
            ans = value
    for i in range(len(visit)):
        if not visit[i]:
            visit[i] = 1
            dfs(i,visit,numbers ,value + numbers[i])
            visit[i] = 0


def solution(numbers):
    global ans
    for i in range(len(numbers)):
        visit = [0] * len(numbers)
        visit[i] = 1
        dfs(i,visit,numbers,str(numbers[i]))
    
    return ans
solution([6,10,2])