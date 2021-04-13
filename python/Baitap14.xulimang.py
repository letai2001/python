print("Nhap so phan tu cua mang")
n =  int(input())
list = []
temp = 0
for i in range(n):
    list.append(int(input()))
check = 0
for i in range (n):
    if(list[i]!=list[n-i-1]):
        check+=1
if check>0:
    print("no")
else:
    print("yes")