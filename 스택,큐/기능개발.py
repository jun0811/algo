import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    days = [0] * len(progresses)
    for p in range(len(progresses)):
        days[p] = math.ceil((100 - progresses[p]) / speeds[p])
    print(days)
    # tc1: [7, 3, 9]
    # tc2: [5, 10, 1, 1, 20, 1]
    
    days_q = deque(days)
    print(days_q)
    cnt = 1
    while days_q:
        day = days_q.popleft()
        
        if days_q and day >= days_q[0]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
    print(answer)
    return answer
solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])