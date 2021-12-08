def calcu(cur, cur_weight):
    tmp = dp[cur][cur_weight]
    if (tmp != 0) : return
    
    dp[cur][cur_weight] = 1 
    if cur >= n: return
    
    calcu(cur+1, cur_weight + chu[cur])
    calcu(cur+1, cur_weight)
    calcu(cur+1, abs(cur_weight - chu[cur]))

n = int(input()) # 추 갯수
chu = list(map(int,input().split()))
num = int(input()) # 구슬 갯수 
gu = list(map(int,input().split()))
# 고려 사항 
# 1. 구슬이 없는 저울에 추를 추가  | 2. 추가하지 않는 경우  |  3. 구슬이 있는 저울에 추를 추가 
max_weigh = sum(chu)
dp = [[0 for _ in range(500*300+1)] for _ in range(31)] 


calcu(0,0)

last_arr = dp[n]
for g in gu:
    if last_arr[g] == 1:
        print('Y', end=" ")
    else: print('N', end=" ")