n = int(input())

def 우박수(n):
    if n == 1:
        print(n)
        return
    elif n%2: 
        # 홀수 
        우박수(3*n+1)
        print(n)
    else:
        우박수(n//2)
        print(n)

(우박수(n))