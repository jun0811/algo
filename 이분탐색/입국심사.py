def solution(n, times):
    left = (n//len(times)) * min(times)
    right = (n//len(times)) * max(times)
    answer = 10 ** 10
    while left <=right:
        mid = (left +right)//2
        # print(mid,left,right)
        tmp = 0
        for time in times:
            tmp += mid//time # 심사대당 통과가능한 사람수
            
        if tmp >= n:
            answer = mid
            right = mid -1      
                
        elif tmp < n: # 통과못한 사람이 있으면
            left = mid+1
    return answer