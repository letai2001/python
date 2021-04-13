print("Nhap so phan tu cua mang")
n = int(input())
while n>99 or n<0:
    print("Nhap lai n ")
    n = int(input())
print("Nhap so muon chen ")
x = int(input())
k = 0
list = [1,3,5,8,9,17,18,19]

for i in range (len(list)):
    if(list[i]<=x and x<=list[i+1]):
        k = i
list.insert(k,x)
for i in range (len(list)+1):
    print(list[i])


    




    



