"""Lưu trữ thông tin 10 người (gồm id và name) (dữ liệu tự khởi tạo). 
Cho phép nhập vào id của một người và in ra tên ứng với id đó"""
class Person:
    Id = 0
    Ten = " "
    def __init__ (self, Id, Ten):
        self.Id = Id
        self.Ten = Ten
        
    def getId(self):
        return self.Id
        
    def getTen(self):
        return self.Ten
        
list = [Person(1,"Tai"),Person(2,"duc"),Person(3,"quan"),Person(4,"hung"),Person(5,"Van"),Person(6,"toan"),Person(7,"duong")
,Person(8,"phat"),Person(9,"nhan"),Person(10,"danh")]
print("Nhap id: ",end = " ")
id = int(input())
j = -1
for i in list:
    if i.Id== id:
        print("Ten cua nguoi co id do: "+i.Ten)
        j+=1
if(j==-1):
    print("Khong ton tai!")