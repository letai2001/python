"""Đếm số ký tự thường/hoa/số trong 1 mật khẩu"""
print("Nhap xau: ")
s = input()
demThuong = 0
demHoa = 0
demSo = 0
for c in s:
    if c.isupper():
            demHoa += 1
    if c.islower():
            demThuong += 1
    if c.isnumeric():
            demSo += 1

print("So ki tu thuong la: "+str(demThuong))
print("So ki tu hoa la: "+str(demHoa))
print("So ki tu so la: "+str(demSo))