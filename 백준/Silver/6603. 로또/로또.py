import sys
input = sys.stdin.readline

def dfs(depth,s,lst):

    if depth==6:
        answer.append(lst)
        return
    for i in range(s,k):
        dfs(depth+1,i+1,lst+[li[i]])

while True:
    lotto = list(map(int,input().split()))
    k=lotto[0]
    li = lotto[1:]
    if k==0:
        break
    v=[0]*k
    answer=[]
    dfs(0,0,[])
    for i in answer:
        print(*i)
    print()
    