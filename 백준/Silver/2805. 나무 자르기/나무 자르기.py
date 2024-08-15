N, M = map(int, input().split())
a = list(map(int, input().split()))
end=max(a)
start=0

while start<=end:
    mid = (start+end)//2
    log=0
    for i in a:
        if i >= mid:
            log += i-mid

    if log>=M:
        start = mid +1
    else:
        end= mid-1
    
print(end)

        