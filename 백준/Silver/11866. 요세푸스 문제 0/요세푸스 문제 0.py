import sys
from collections import deque
input=sys.stdin.readline
n,k=map(int,input().split())
li=deque()
answer=[]
for i in range(1,n+1):
    li.append(str(i))

for i in range(n):
    for i in range(k-1):
        li.append(li.popleft())
    answer.append(li.popleft())

print('<'+', '.join(answer)+'>')