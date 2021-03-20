
def isWall(y,x):
    if 0<=y<n and 0<=x<n:
        return False
    else: return True

def check(s, y,x):
    endx = x+s
    endy = y+s
    if isWall(endy-1,endx-1):
        return 0
    for j in range(y,endy):
        for i in range(x,endx):
            if arr[j][i] == "0":
                return 0
    return 1

n = int(input()) # 한변의 길이
arr = [input() for _ in range(n)] #공간 입력 
size = [0] * (n+1)

for y in range(n):
    for x in range(n):
        if int(arr[y][x]) == 1:
            size[1] +=1 

for s in range(2,n+1):
    for y in range(n):
        for x in range(n):
            size[s] += check(s,y,x)

print("total: {}".format( sum(size)))
for i in range(1,n+1):
    if size[i]:
        print("size[{}]: {}".format(i,size[i]))