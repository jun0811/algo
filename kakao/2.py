def solution(t, r):
    answer = []
    car = 0  # 시간
    for i in range(len(t)):
        # 시간 별로 체크
        tmp = -1
        for j in range(len(t)):
            if j in answer:
                continue
            if t[j] == i and tmp == -1:  # 첫
                tmp = j  # 케이블카 확인
            elif tmp != -1 and t[j] == i:
                # 티켓 등급 비교
                if r[tmp] > r[j]: tmp = j
            elif tmp == -1 and i > t[j]:
                tmp = j

        answer.append(tmp)
    print(answer)
solution([0,1,3,0], [0,1,2,3])