arr = [7,6,5,0,3,2,1,4,9]

for i in range(len(arr)):
    min_v = i
    for j in range(i+1,len(arr)):
        if arr[min_v] > arr[j]:
            min_v = j
    arr[i], arr[min_v] = arr[min_v], arr[i]
print(arr)