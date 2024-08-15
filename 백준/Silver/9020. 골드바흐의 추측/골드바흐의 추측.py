T=int(input())
def sosu(n):
    bool = True
    for i in range(2,n):
        if n%i==0: return False
    return bool

for i in range(T):
    n=int(input())
    for i in range(n//2,1,-1):
        if sosu(i) and sosu(n-i):
            print(i,n-i)
            break