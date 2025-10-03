import sys
input = sys.stdin.readline

n=int(input())

idx=2
answer=[]
while n>1:
    for i in range(idx,n+1):
        if n%i==0:
            idx=i
            n//=i
            answer.append(i)
            break

answer.sort()
for a in answer:
    print(a)