a = float(input("Nhap vao so a: "))
b = float(input("Nhap vap so b: "))
if a==0:
    if b==0.0:
        print(" Bất Phương trình vô nghiệm!")
    elif b > 0.0:
        print(" Bất phương trình ax+b>0 vô số nghiệm ")
        print("Bất phương trình ax+b<0 vô  nghiệm")
    elif b < 0.0:
        print("Bất phương trình ax+b<0 vô số nghiệm")
        print(" Bất phương trình ax+b>0 vô  nghiệm ")
else:
    x = -b/a
    print("Bất Phương trình  ax+b>0 có nghiệm  x > "+str(-b/a))
    print("Bất Phương trình  ax+b<0 có nghiệm  x < "+str(-b/a))

