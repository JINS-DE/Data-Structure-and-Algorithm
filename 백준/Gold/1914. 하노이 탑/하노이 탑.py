import sys
input=sys.stdin.readline
n=int(input())

def hanoi(n,fr,tmp,end):
    if n==1:
        print(f"{fr} {end}")
    else:
        hanoi(n-1,fr,end,tmp)
        print(f"{fr} {end}")
        hanoi(n-1,tmp,fr,end)
print(2**n-1)
if n<=20:
    hanoi(n,'1','2','3')
