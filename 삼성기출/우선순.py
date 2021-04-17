import heapq
# 최소힙 -> - 인자를 붙이면 최대힙
def heapsort(arr):
    h = []
    res = []
    for v in arr:
        heapq.heappush(h,v) # -v
    for i in range(len(h)):
        res.append(heapq.heappop(h)) # - heapq  -> 최대힙
    return res

n = int(input())
arrs =[]
for i in range(n):
    arrs.append(int(input()))

res = heapsort(arrs)
for i in range(n):
    print(res[i])

