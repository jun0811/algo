x , y = map(int,input().split())
n= int(input())
w_slice = [0]
h_slice = [0]
for _ in range(n):
    d , index = map(int,input().split())
    if d==0: # 가로로 자르기
        h_slice.append(index)
    else:
        w_slice.append(index)
w_slice.sort()
h_slice.sort()
w_slice.append(x)
h_slice.append(y)
print(w_slice, h_slice)
width = []
height = []
for i in range(1,len(w_slice)):
    width.append(w_slice[i]-w_slice[i-1])
for i in range(1,len(h_slice)):
    height.append(h_slice[i]-h_slice[i-1])
print(max(width) *  max(height))