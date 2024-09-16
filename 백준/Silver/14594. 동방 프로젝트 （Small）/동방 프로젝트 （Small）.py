import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
li=[0]*(N+1)
for _ in range(M):
    x,y = map(int,input().split())
    for i in range(x,y):
        li[i] = 1

print(li.count(0)-1)
