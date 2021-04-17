import heapq

arr= [1, 2, 3, 9, 10, 12]
k = 7

def heapsort(arr):
    h = []
    res = []
    for a in arr:
        heapq.push(h,a)
    for i in range(len(h)):
        res.append(heapq.heappop(h))
    return res

res = heapsort(arr)
