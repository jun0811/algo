
import sys
sys.setrecursionlimit(100000)
match = {0:5 , 5:0, 1:3,3:1,4:2,2:4}

def search(button,top,cur,value):
    global maxV
    tmp = 0
    # 최대값 찾기
    for i in range(6):
        if i!=button and i!=top:
            tmp = max(tmp,arr[cur][i])
    
    if n-1 <= cur:
        maxV = max(maxV, value+tmp )
        return
    next_dice = arr[cur+1]
    next_button_index = next_dice.index(arr[cur][top])
    
    next_top_index = match[next_button_index]
    search(next_button_index, next_top_index, cur+1, value+tmp)

n = int(input())
arr = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    arr.append(tmp)
maxV = 0 
search(0,5,0,0)
search(5,0,0,0)
search(1,3,0,0)
search(3,1,0,0)
search(2,4,0,0)
search(4,2,0,0)
print(maxV)

