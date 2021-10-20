n = int(input())

def binary(n):
    if n == 1:
        return "1"
    if n == 0:
        return 0
    return binary(n//2) + str(n%2)

print(binary(n))