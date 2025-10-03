import sys, math
input = sys.stdin.readline

n=int(input())

i=2
while i <= math.sqrt(n):
    while n%i==0:
        print(i)
        n//=i
    i+=1

if n>1:
    print(n)