print("Nhap so phan tu cua mang")
n = int(input())
while n>99 or n<0:
    print("Nhap lai n ")
    n = int(input())

print("Nhap so muon chen ")
x = int(input())
print("Nhap vi tri muon chen")
k = int(input())
if k>n:
    print("khong hop le")
    
list = []
for i in range (n):
    print("Nhap a["+str(i)+"]")
    list.append(int(input()))
list.insert(k,x)
for i in range (n+1):
    print(list[i])

















