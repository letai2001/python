list=[]
print("Nhap so phan tu cua mang")   #1,2,3,4,5-> 4,2,3,1,5->4,5,3,1,2->3,5,4,1,2->3,1,4,5,2->3,1,2,5,4
n = int(input())
print("Nhap k")
k = int(input())
temp = 0
while n>90 or n<0:
    print("Nhap lai n ")
    n = int(input())
for i in range (n):
    list.append(int(input()))
for i in range(n):
    if(i+k<=n-1) :
       # temp = list[i]
        list[i] = list[i+k]
        #list[i+k] = temp
    else:
        #temp = list[i]
        list[i] = list[i+k-n]
       # list[i+k-n]=  temp
print(list)
