print("Nhap so phan tu cua mang")
n =  int(input())
list = []
temp = 0
print("Nhap so k")
k = int(input())
for i in range(n):
    list.append(int(input()))
for i in range(n-1):
    for j in range (i+1,n):
        if list[i]>list[j] :
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
for i in range(n):
        if(i==k-1):
            print(list[i])



