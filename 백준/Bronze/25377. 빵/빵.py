n=int(input())
li=[]
for i in range(n):
    a,b=map(int,input().split())
    li.append((a,b))

min_time=float('inf')
for a,b in li:
    if a>b:
        continue
    if min_time>b:
        min_time=b
if min_time==float('inf'):
    print(-1)
else:
    print(min_time)