# from collections import deque

def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        while progresses[0] <100:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]

        for i in range(len(progresses)):
            if progresses[i] >=100:
                cnt+=1
            else: break
        for i in range(cnt):
            speeds.pop(0)
            progresses.pop(0)

        answer.append(cnt)
    return answer

print(solution([95, 90, 99, 99, 80, 99]	, [1, 1, 1, 1, 1, 1]))