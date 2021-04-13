
dem = 0

print("Nhap so phan tu cua mang")
n = int(input())
while n>99 or n<0:
    print("Nhap lai n ")
    n = int(input())
a = []
for i in range (n):
    print("Nhap a["+str(i)+"]")
    a.append(int(input()))
print("Day con tang dan: ")
for i in range (n):
    dem = 0
    while (a[i] < a[i + 1]):
        if (dem == 0):
             print(str(a[i])+" "+str(a[i+1]), end =" ")
        else: 
            print( str(a[i + 1]),end = " ");
        i+=1
        dem+=1

    print();

 


