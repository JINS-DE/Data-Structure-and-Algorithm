C=int(input())
for i in range(C):
    stu=list(map(int,(input().split())))

    N=stu[0]
    score=stu[1:]

    avg=sum(score)/len(score)
    print(str(round((len(list(filter((lambda x: x>avg),score)))/N)*100,3))+'%')