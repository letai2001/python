n =0
list = []
temp = 0
for i in range(99):
    list.append(int(input()))
    n+=1
    if list[i]==-1 :
        break
for i in range(n-2):
    for j in range (i+1,n-1):
        if list[i]>list[j] :
            temp = list[i]
            list[i] = list[j]
            list[j] = temp

for i in range(n-1):
    print(list[i])


