a = int(input("Nhap vao so a: "))
b = int(input("Nhap vap so b: "))
c = int(input("Nhap vao so c: "))
d = int(input("Nhap vao so d: "))
max1 = a
max2 = c
if(max1<b):
    max1 = b
if(max2<d):
    max2 = d
if(max1>max2):
    print("Số lớn nhất là: "+str(max1))
else:
    print("Số lớn nhất là: "+str(max2))





