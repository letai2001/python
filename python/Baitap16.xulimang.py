list=[]
a = []
b = []
print("Nhap so phan tu cua mang")
n = int(input())
count  = 0;
while n>9 or n<0:
    print("Nhap lai n ")
    n = int(input())

for i in range (n):
    list.append(int(input()))
for i in range(n):
    if(list[i]%2==0):
        a.append(list[i])
    else:
        b.append(list[i])
print("a = ",end = " ")
print(a)
print("b = ",end = " ")

print(b)
