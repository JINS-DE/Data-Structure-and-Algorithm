import sys
input = sys.stdin.readline
n= int(input())
arr = [int(input())]
for _ in range(n-1):
    inp = list(map(int,input().split()))
    inp[0] += arr[0]
    i=1
    while i < len(inp):
        if i==len(inp)-1:
            inp[i]+=arr[-1]
        else:
            inp[i] += max(arr[i-1],arr[i])
        i+=1
    
    arr = inp
print(max(arr))
