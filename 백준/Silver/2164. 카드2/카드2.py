
import sys
from collections import deque
input = sys.stdin.readline
n=int(input())
li=deque()
for i in range(1,n+1):
    li.append(i)
for i in range(n-1):    
    del li[0]
    li.append(li.popleft())
print(*li)    