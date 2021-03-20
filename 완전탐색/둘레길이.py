def solution(brown, yellow):
    answer = []
    tmp = []
    for i in range(1, yellow+1):
        print(i)
        if yellow // i < i:
            break
        if yellow % i == 0:
            tmp.append([yellow//i, i])
    for t in tmp:
        x, y = t
        if (x+2)*2 + (y*2) == brown:
            answer.append(x+2)
            answer.append(y+2)

    return answer
