h, w = map(int, input().split())

arr = list(map(int, input().split()))

water = 0

for i in range(1,w-1):
    # 왼쪽 
    left = arr[i]
    for j in range(i-1, -1, -1):
        if left < arr[j]:
            left = arr[j]
    # 오른쪽 
    right = arr[i]
    for j in range(i+1,w):
        if right < arr[j]:
            right = arr[j]
    final = min(left,right)
    water += final - arr[i]
print(water)