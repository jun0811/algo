def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)

def LCM(a,b):
    g = GCD(a,b) # 최대공약수로 나눈 값은 서로소  
    return g*(a/g)*(b/g) # 서로소를 곱하고 최대공약수를 곱하면 최소공배수 

a,b = map(int,input().split())
print(GCD(a,b))
print(int(LCM(a,b)))