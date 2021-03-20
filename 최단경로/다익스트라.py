
INF  = int(1e9)
#n : 노드 m : 간선 
n, m = map(int, input().split())
start = int(input())
# 각 노드에 연결되어 있는 노드 정보 리스트
graph = [[] for _ in range(n+1)]

visited= [0] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])

def dijkstra(s):
    distance[s] = 0
    visited[s] = 1
    for j in graph[s]:
        distance[j[0]] = j[1]
    for i in range(n-1):
        minV = INF
        index = 0 # 가장 최단 거리가 짧은 인덱스 
        for j in range(1,n+1):
            if distance[j] < minV and not visited[j]:
                minV= distance[j]
                index= j
    visited[index] = 1
    for k in graph[index]:
        cost = distance[index] + k[1]
        if cost <distance[k[0]]:
            distance[k[0]] = cost

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF :
        print("갈수없음")

    else:
        print(distance[i])