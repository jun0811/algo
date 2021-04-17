import sys
from collections import deque
from heapq import heappop, heappush
sys.stdin= open('test')

dx = [0,1,0,-1]
dy = [1,0,-1,0]

n,m,k = map(int,input().split())
# 0은 빈킨 1은 벽
# arr : 활동 지도
arr = [list(map(int,input().split())) for _ in range(n)]

# 운전 시작 행 열
taxi_x, taxi_y = map(int,input().split())
#
s = [] # 시작
e = [] # 도착

for _ in range(m):
    s_y, s_x, e_y, e_x = map(int,input().split())
    s.append([s_y,s_x])
    e.append([e_y,e_x])

visited = [0] * m

def isin(y,x):
    if -1<y<n:
        if -1<x<n: return True
    return False

def bfs():
    global 