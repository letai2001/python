print("Nhap so x")
x = int(input())
print("Nhap so phan tu cua mang")
n = int(input())
while n>99 or n<0:
    print("Nhap lai n ")
    n = int(input())

print("Nhap so muon chen ")
x = int(input())
list = []
for i in range (n):
    print("Nhap a["+str(i)+"]")
    list.append(int(input()))
for i in range(n):
    if list[i]<= x:
        print(list[i])