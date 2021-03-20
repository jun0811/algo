import heapq
# 최소 힙
def heapsort(arr):
    h = []
    result=  []
    for v in arr:
        heapq.heappush(h,v)
    print(h)
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,2,7,4,6])
print(result)