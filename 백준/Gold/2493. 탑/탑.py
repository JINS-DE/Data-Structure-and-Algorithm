import sys
input=sys.stdin.readline
n=int(input())
li = list(map(int,input().split()))
stack=[]
ans=[0]*len(li)
for i,val in enumerate(li):
    while stack:
        if stack[-1][1]>val:
            ans[i]=stack[-1][0]+1
            break
        else:
            stack.pop()
    stack.append((i,val))
print(*ans) 
          
   