def check(arr,ans):
    
    cnt = []
    for i in range(len(ans)):
        if arr[i] == ans[i]:
            cnt.append(ans[i])
    return cnt

def solution(answers):
    
    a = [1,2,3,4,5] * len(answers)
    b = [2,1,2,3,2,4,2,5] * len(answers)
    c = [3,3,1,1,2,2,4,4,5,5] * len(answers)
    
    res1 = check(a, answers)
    res2 = check(b, answers)
    res3 = check(c, answers)
    
    max_cnt = max(len(res1), len(res2), len(res3))
    res = [res1,res2,res3]
    answer = []
    for i in range(3):
        print(max_cnt, len(res[i]))
        if max_cnt == len(res[i]):
            answer.append(i+1)
    return answer

print(solution([1,2,3,4,5]))