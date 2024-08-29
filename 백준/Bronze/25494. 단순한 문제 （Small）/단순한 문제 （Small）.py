import sys
input=sys.stdin.readline

T=int(input())

for i in range(T):
    li=list(map(int,input().split()))
    print(min(li))
