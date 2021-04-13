"""Xây dựng hàm chuanHoa nhận đầu vào là một chuỗi họ tên và đầu ra (giá trị trả về) là chuỗi sau khi đã chuẩn hóa.
 Để chuẩn hóa một chuỗi họ tên trước hết cần xóa các khoảng trắng thừa sau đó các ký tự đều chuyển sang dạng THƯỜNG
 ngoại trừ các ký tự đầu của mỗi từ là dạng HOA. Viết chương trình minh họa."""
# print(s.strip())
def  isWhiteSpace(s):
    return s == " " or s=="\t"or s=="\n"
def ChuanHoa(a):
    list = []
    s = []
    list2 = []
    for i in range (len(a)):
        s.append(a[i])
    length= len(a)
    for i in range (length):
        if i<length-1:
            if(s[i] == s[i+1] and s[i+1] == " ") :
                continue
            else:
                list.append(s[i])
        elif s[i]!=" ":
            list.append(s[i])
    newstring = ''.join(list)
    string = newstring.strip()
    string2 = string.lower()
    for i in range (len(string2)):
        if(i>=1):
            if(string2[i-1]==" "):
                list2.append(string2[i].upper())
            else:
                list2.append(string2[i].lower())
        else:
                list2.append(string2[i].upper())

            
    newstring2 = ''.join(list2)
    
            
            
        
    return newstring2

a = input()
print(ChuanHoa(a))