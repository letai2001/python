list=[]
k = int(input())
print("Nhap so phan tu cua mang")
n = int(input())
count  = 0;
while n>99 or n<0:
    print("Nhap lai n ")
    n = int(input())
if k>n:
    print("khong hop le")
for i in range (n):
    list.append(int(input()))

del list[k]
for i in range (n-1):
    print(list[i])
