l=5
r=555

answer=[]
li=[]
i=0
while True:
    i+=1
    li.append(5*int(bin(i)[2:]))
    if li[-1] > r:
        break
    if li[-1]>=l:
        answer.append(li[-1])
print(answer)