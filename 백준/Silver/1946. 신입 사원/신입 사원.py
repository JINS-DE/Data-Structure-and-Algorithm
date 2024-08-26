import sys
input=sys.stdin.readline
t=int(input())


for i in range(t):
    n=int(input())
    li=[]
    for j in range(n):
        li.append(tuple(map(int,input().split())))
    li.sort()
    # 1차의 1등을 기준으로 잡는다. 합격하기 위해서는 1등의 2차 등수보다 높아야 한다. 
    # 1등은 이미 포함되어 있으니 cnt=1로 시작
    cnt=1
    max_=li[0][1]
    for i in range(1,n):
        if max_ > li[i][1]:
            cnt+=1
            max_=li[i][1]
    print(cnt)
