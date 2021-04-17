def find_parent(x): # 특정 원소가 속한 집합을 찾기
    # 루트 노드를 찾을 때 까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent[x])
    return x

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1,v+1):
    parent[i] = i

for i in range(e):
    a,b = map(int,input().split())
    union_parent(a,b)

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합")
for i in range(1,v+1):
    print(find_parent(i))

print()

print('부모테이블')
for i in range(1,v+1):
    print(parent[i])