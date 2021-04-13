list=[]
print("Nhap so phan tu cua mang")
n = int(input())
count  = [];
index = []
temp = 0
while n>9 or n<0:
    print("Nhap lai n ")
    n = int(input())
print("nhap cac phan tu cua mang")
for i in range (n):
    list.append(int(input()))
for i in range(n):
    temp = 0
    for j in range(n):
        if(list[j]==list[i]):
            temp+=1;
    count.append(temp)
for i  in range (n):
    if(count[i]==max(count)):
        print("Phan tu xuat hien nhieu nhat: "+str(list[i]))
        print("Xuat hien: "+str(count[i])+" lan")
        break

