from math import sqrt
number=10
limit = 3
power = 2

answer=0
for i in range(1,number+1):
    cnt=0
    s=sqrt(i)
    for j in range(1,int(s)+1):
        if i%j==0:
            cnt+=1
    
    if s%1==0:
        cnt=cnt*2-1
    else:
        cnt=cnt*2
    
    if cnt>limit:
        answer+=power
    else:
        answer+=cnt
print(answer)
# print(sum(map(lambda x:x if x<=limit else power,li)))
      
