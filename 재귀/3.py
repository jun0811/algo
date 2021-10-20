# dp 재귀형 

n = int(input())
# n = 6
dp = [0] * (n+1)
dp[1]= 1


def fibo(n):
    if n<=1:
        return n 
    if dp[n] == 0:
        dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]        

print(fibo(n)%10009)