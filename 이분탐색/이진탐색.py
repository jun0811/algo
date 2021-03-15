# def bin_search(arr,goal, start,end):
#     global res
#     if start > end:
#         return False
    
#     mid = (start+end)//2
#     if arr[mid] == goal: 
#         print(arr[mid])
#         return arr[mid]
#     elif arr[mid]> goal:
#         return bin_search(arr,goal,start,mid-1)
#     else:
#         return bin_search(arr,goal, mid+1,end)

# arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
# goal = 11

# res = bin_search(arr,goal, 0, len(arr)-1)
# print(res)

from bisect import bisect_left, bisect_right

def count_by (a, left, right):
    r_id = bisect_right(a, right)
    l_id = bisect_left(a,left)
    return r_id - l_id

a = [1,2,3,3,3,3,4,4,5,7]
# 4의 갯수
print(count_by(a,4,4))
# [-1,3] 범위 수
print(count_by(a,-1,3))