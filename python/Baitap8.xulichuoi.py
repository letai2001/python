"""Xây dựng hàm nhận đầu vào là chuỗi s và hai số nguyên k, n sau đó xóa chuỗi con độ dài n bắt đầu từ vị trí k ra khỏi chuỗi s
. Viết chương trình minh họa"""
def xoaKiTu(string,k,n):
    list = []
    for i in range (k):
         list.append(string[i])
    newstring = ''.join(list)
    return newstring
print("nhap k = ",end = " ")
k = int(input())
print("nhap n = ",end = " ")
n = int(input())
print("nhap  string co do dai bang n , string =  ",end = " ")
string = input()
while(len(string)!=n):
    print("Nhap lai chuoi")
    string = input()
print("ki tu sau khi da xoa: ")
print(xoaKiTu(string,k,n))
