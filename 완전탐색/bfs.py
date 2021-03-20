import collections

def solution(numbers, target):
    
    q = collections.deque()
    answer=0
    q.append([0,0])
    while q:
        idx, value = q.popleft()
        if idx ==len(numbers):
            if value == target:
                answer +=1
            continue
        q.append([idx+1,value+numbers[idx]])
        q.append([idx+1,value-numbers[idx]])
    return answer

a = solution([1,1,1,1,1],3)

print(a)