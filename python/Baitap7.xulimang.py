list=[]
list1 = []
j = 0
print("Nhap so k ")
k = int(input())
print("Nhap so phan tu cua mang")
n = int(input())
count  = n
while n>99 or n<0:
    print("Nhap lai n ")
    n = int(input())
for i in range (n):
    print("Nhap a["+str(i)+"]")
    list.append(int(input()))
for i in range (n):
    if list[i]!= k:
        list1.append(list[i])
        j+=1
print("mang sau khi xoa")
for i in range (j):
    print(list1[i])

print("so phan  da xoa: "+str(n-j))


