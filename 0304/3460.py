for _ in range(int(input())):
    n = int(input())
    res=""
    while n!=0:
        res+=str(n%2)
        n//=2
    print(res)
    for i in range(len(res)):
        if res[i] =="1":
            print('{}'.format(i),end=" ")