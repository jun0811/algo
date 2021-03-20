def prim():
    u.append(0)
    D[0] = 0
    curV = 0

    for i in range(V + 1):
        D[i] = G[0][i]

    while len(u) < V + 1:
        minV = maxV
        for i in range(V + 1):
            if i in u:
                continue

            if minV > D[i]:
                minV = D[i]
                curV = i

        for i in range(V + 1):
            if i in u:
                continue
            
            D[i] = min(D[i], G[curV][i])
            
            # 다익스트라
            D[i] = min(D[i], D[curV] + G[curV][i])

        u.append(curV)
T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    maxV = 0xffffffffff
    G = [[maxV] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        G[n1][n2] = w
        G[n2][n1] = w

D = [maxV] * (V + 1)
u = []

prim()
result = sum(D) - maxV
print('#{} {}'.format(tc, result))