import sys
input=sys.stdin.readline
N,M=map(int,input().split())
a=list(map(int,input().split()))

tmp=[0]*3
sum_li=[]

def dfs(depth,start):
    if depth==3:
        sum_li.append(sum(tmp))
        return
    else:
        for i in range(start,len(a)):
            tmp[depth]=a[i]
            dfs(depth+1,i+1)
dfs(0,0)

closest =None
for i in sum_li:
    if i <= M:
        if closest is None or i > closest:
            closest = i
print(closest)