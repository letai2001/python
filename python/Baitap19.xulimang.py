print("Nhap do cao h")
h = int(input())
while(h<0 or h>20):
    print("Nhap lai h")
    h = int(input())

def tohop(k,n):
    if k==n : 
       return 1
    if k==1 : 
        return n
    if k==0 :
        return 1
    else: 
        return tohop(k-1,n-1)+tohop(k,n-1)
for i in range (h):
    j = h
    while(j>i):
        print(" ",end = " ")
        j-=1
    for j in range (i+1):

        print(tohop(j,i),end = "   ")
    print()



