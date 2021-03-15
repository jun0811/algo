def bin_search(arr,start,end):
    global res
    if start ==end:
        return    
    mid = (start+end) // 2 # 절단 높이
    tmp = 0 # 떡 길이
    for a in arr:
        if (a-mid)>0:
            tmp += (a-mid)
    
    if (m<=tmp): # 요구사항보다 떡 길이가 크면 
        if mid>res: res = mid # res가 커지면 바꿔주고
        bin_search(arr,mid+1,end)
    else:
        bin_search(arr,start,mid)



n, m = map(int,input().split())
arr = list(map(int,input().split()))


res = 0 # 절단기 높이
bin_search(arr,0,max(arr))
print(res)