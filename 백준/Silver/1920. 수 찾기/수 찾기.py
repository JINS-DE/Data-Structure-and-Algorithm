import sys
input=sys.stdin.readline
n=int(input())
n_li=list(map(int,input().split()))
m=int(input())
m_li=list(map(int,input().split()))
n_li.sort()
def binary_search(num):
    
    pl=0
    pr=len(n_li)-1
    while True:
        pc=(pl+pr)//2
        if n_li[pc]==num:
            return 1
        elif n_li[pc]<num:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl>pr:
            break
    return 0 

for i in m_li:
    print(binary_search(i))
