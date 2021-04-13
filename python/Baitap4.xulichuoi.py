"""Viết chương trình đọc vào một chuỗi s từ bàn phím sau đó hiển thị số ký tự trắng ra màn hình"""
print("Nhap xau: ")
s = input()
count = 0
for i in range (len(s)):
    if(s[i]==" "):
        count+=1
print("So khoang trang la: "+str(count))

