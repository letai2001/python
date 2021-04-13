a = float(input("Nhap vao so a: "))
b = float(input("Nhap vap so b: "))
if a==0:
    if b==0:
        print(" Phương trình vô nghiệm!")
else:
    x = -b/a
    print("Bất Phương trình có nghiệm duy nhất x > "+str(-b/a)) 

