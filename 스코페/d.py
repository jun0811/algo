like = list(map(float, input().split()))  # 유저 선호도

dic = {"A": like[0], "B": like[1], "C": like[2], "D": like[3], "E": like[4]}

n, m = map(int, input().split())
contents = [list(input()) for _ in range(n)]
category = [list(input()) for _ in range(n)]

order = []

# 1.유저가 열람 ㅎ나적없는 컨텐츠를 선호도가 높은 장르의 컨텐츠 순으로
for y in range(n):
    for x in range(m):
        if contents[y][x] =="W":
            continue
        else:
            tmp = 1
            if contents[y][x] == "O":
                tmp = 0
            order.append([tmp, category[y][x], y,x ])



for i in range(len(order)):
    maxV = i
    for j in range(i+1,len(order)):
        # 유저가 열람한 적 업는 게 있으면 무조건 바꿔주고
        if order[maxV][0] < order[j][0]:
            maxV = j
        elif order[maxV][0] == order[j][0]: # 열람 조건이 같으면 
            # 선호도 비교를 하는데 선호도가 같은 장르면 먼저 온
            if dic[order[maxV][1]] == dic[order[j][1]]:
                if order[maxV][2] > order[j][2]:
                    maxV = j
                elif order[maxV][2] == order[j][2]:
                    if order[maxV][3] > order[j][3]:
                        maxV = j
            elif dic[order[maxV][1]] < dic[order[j][1]]:
                maxV = j
    order[maxV], order[i] = order[i], order[maxV]

for o in (order):
    print("{} {} {} {}".format(o[1], dic[o[1]], o[2],o[3]))



        


# 2. 유저가 열람햇으나 끝까지 못본 컨텐츠 