"""Xây dựng hàm đếm số từ trong một chuỗi, sau đó viết chương trình minh họa"""
def soTu(string):

    count={}
    for i in string:
        if(i !=" "):
            if i in count:
                count[i] +=1
            else:
                count[i] = 1
    return count
print("Nhap chuoi: ")
string = input()
print("Danh sach cac tu va so lan xuat hien:")
print(soTu(string))