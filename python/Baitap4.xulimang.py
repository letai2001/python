list=[]
a = float(input())
n = int(input())
count  = 0;
while n>99 or n<0:
    print("Nhap lai n ")
    n = int(input())

for i in range (n):
    list.append(float(input()))
    if list[i]==a:
        count+=1
if count>0:
    print("yes")
else:
    print("no")
