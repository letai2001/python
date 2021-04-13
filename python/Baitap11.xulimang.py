print("Nhap so phan tu cua mang")
n = int(input())
temp = 0
left = 0
right =  n-1
while n>99 or n<0:
    print("Nhap lai n ")
    n = int(input())

list = []
for i in range (n):
    print("Nhap a["+str(i)+"]")
    list.append(int(input()))
while(left<right):
    temp = list[left]
    list[left] = list[right]
    list[right] = temp
    left+=1
    right-=1
for i in range(n):
        print(list[i],end=" ")