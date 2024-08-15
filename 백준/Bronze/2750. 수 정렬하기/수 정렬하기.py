n=int(input())
a=[int(input()) for i in range(n)]

for i in range(n-1):
    min_ = i
    for j in range(i+1,n):
        if a[j] < a[min_]:
            min_ = j
    a[i],a[min_] = a[min_],a[i]
for i in a:
    print(i)