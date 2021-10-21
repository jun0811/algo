a, b = map(int,input().split())

if b<a:
    a,b =b,a 

while True:
    n = a%b 
    if n ==0:
        print(b)
        break
    else:
        a = b
        b = n
        