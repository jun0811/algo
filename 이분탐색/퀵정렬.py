def quick_sort(arr):
    if len(arr) <=1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left_side = [x for x in tail if x<=pivot] # 작은건 왼쪽
    right_side = [x for x in tail if x> pivot] # 큰건 오른쪽 

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)



arr = [7, 6, 5, 0, 3, 2, 1, 4, 9]
print(quick_sort(arr))
