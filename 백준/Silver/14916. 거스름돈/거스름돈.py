n=int(input())
q,r = divmod(n,5)
if r%2==1:
    q-=1
    r+=5
if q<0:
    print(-1)
else:
    print(q+r//2)
