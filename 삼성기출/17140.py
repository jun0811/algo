 # https://www.acmicpc.net/problem/17140
from collections import Counter
arr = [[2,3,4,2,2,2,1,5],[4,5,6]]
c = list(Counter(arr[0]).items())
c.sort(key= lambda x: (x[1], x[0]) )
print(c)
arr = list(map(list, zip(*arr)))
print(arr)