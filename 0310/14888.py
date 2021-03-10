def plus(a, b):
    return a+b


def sub(a, b):
    return a-b


def multi(a, b):
    return a*b


def div(a, b):
    return int(a/b)

def insert(i, tmp, c):
    if len(nums) == i+1:
        res.append(tmp)
         
    else:
        for j in range(4):
            if j == 0 and c[j]:
                c[j] -= 1
                insert(i+1, plus(tmp, nums[i+1]), c)
                c[j] += 1
            if j == 1 and c[j]:
                c[j] -= 1
                insert(i+1, sub(tmp, nums[i+1]), c)
                c[j] += 1
            if j == 2 and c[j]:
                c[j] -= 1
                insert(i+1, multi(tmp, nums[i+1]), c)
                c[j] += 1
            if j == 3 and c[j]:
                c[j] -= 1
                insert(i+1, div(tmp, nums[i+1]), c)
                c[j] += 1


n = int(input())
nums = list(map(int, input().split()))
# + - * / 순
arr = list(map(int, input().split()))
res = []

insert(0, nums[0], arr)

print(max(res))
print(min(res))
