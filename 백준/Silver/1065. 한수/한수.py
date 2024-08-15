n=int(input())
hansu=0
for i in range(1,n+1):
    if i<100:
        hansu+=1
    else:
        str_n=str(i)
        temp1 = int(str_n[2])-int(str_n[1])
        temp2 = int(str_n[1])-int(str_n[0])
        if temp1==temp2:
            hansu+=1
print(hansu)