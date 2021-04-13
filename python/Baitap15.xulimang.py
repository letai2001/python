print("Nhap so phan tu cua mang")
n =  int(input())
list = []
sum = 0
for i in range(n):
    list.append(int(input()))
for i in range(n):
    if list[i]%2==0:
        sum+=list[i]
print(sum)
