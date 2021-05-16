from collections import deque

dy = [0, 1, -1, 0]
dx = [1, 0, 0, -1]


def bfs(y, x, arr):
    q = deque()
    q.append([y, x, [arr[y][x]], [[y, x]]])
    while q:
        cy, cx, distance, v = q.popleft()
        if len(distance) == 3:
            if distance.count("P") == 2 and ("X" not in distance):
                return -1
        else:
            for k in range(4):
                ny = cy + dy[k]
                nx = cx + dx[k]
                if 0 <= ny < 5 and 0 <= nx < 5 and [ny,nx] not in v:
                    q.append([ny, nx, distance + arr[ny][nx], v + [[ny, nx]]])
    return 1


def solution(places):
    answer = []
    for place in places:
        # 강의 실
        state = 0  # 강의 실별 거리두기 여부
        for j in range(5):
            for i in range(5):
                if place[j][i] == "P":
                    bfs(j, i, place)
                if tmp == -1:
                    break
            if tmp == -1:
                break
        if tmp == -1:
            answer.append(0)
        else:
            answer.append(1)
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))