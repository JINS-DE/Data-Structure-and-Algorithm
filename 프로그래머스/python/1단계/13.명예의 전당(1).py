k=3
score=[10, 100, 20, 150, 1, 100, 200]
result=[]
li=[]

for i in score:
    li.append(i)
    if len(li)==k+1:
        li.remove(min(li))
    result.append(min(li))
