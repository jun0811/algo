arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

m = 4
n = 3


def combination(start, cnt):
    if len(cnt)== 3:
        print(cnt)
    else:
        for i in range(start,m*n):
            y = i//m
            x = i%m
            # cnt.append([y,x])
            combination(i+1, cnt + [[y,x]] )
            # cnt.pop()
combination(0,[])