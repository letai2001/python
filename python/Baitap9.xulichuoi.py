"""Xây dựng hàm nhận đầu vào là 2 chuỗi s1 và s2. Hàm sẽ xóa các "từ" s2 xuất hiện trong s1
. Hàm trả về chuỗi s1. Sau đó viết chương trình minh họa hàm này"""
def xoaKiTu(str1,str2):
    list = []
    for i in range (len(str1)):
         if str1[i] in str2:
             i+=1
         else:
              list.append(str1[i])
    newstring = ''.join(list)
    return newstring
print("nhap str1 =  ",end = " ")
str1 = input()
print("nhap str2 =  ",end = " ")
str2 = input()

print("ki tu sau khi da xoa: ")
print(xoaKiTu(str1,str2))
