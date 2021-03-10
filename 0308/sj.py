N = int(input())
nums = list(map(int, input().split()))

if 1 in nums:
    nums.remove(1)

for num in nums:
    print(num)
    for i in range(2, num):
        if num % i == 0:
            nums.remove(num)
            break
print(nums)
print(len(nums))
