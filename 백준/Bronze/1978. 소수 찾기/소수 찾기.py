N=int(input())
li=list(map(int,input().split()))
ans_cnt=0
for i in li:
    cnt=0
    if i==1:
        continue
    for j in range(2,i):
        if i%j==0:
            cnt+=1
    if cnt==0:
        ans_cnt+=1
print(ans_cnt)    