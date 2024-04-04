ing=[1, 3, 2, 1, 2, 1, 3,1, 1,2,3,1,2,3,1,3]

answer=0
total_3=ing[2:-1].count(3)
num=2

for i in range(total_3):
    num=ing.index(3,num)
    print(ing)
    if ing[num-2:num+2]==[1,2,3,1]:
        del ing[num-2:num+2]
        answer+=1
        num-=2
    else:
        num+=1

print(answer)