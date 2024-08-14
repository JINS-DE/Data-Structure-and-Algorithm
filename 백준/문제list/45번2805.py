N=4
M=7
a=[20,15,10,17]
end=max(a)
start=0

while start < end : 
    mid=(start+end)//2
    log = sum([i-mid for i in a if i>mid])
    if log >= M :
        start=mid+1
    else:
        end=mid-1
print(end)


# 이진 탐색 재귀        
def bianary_search(start,end,M,a):
    if start>end:
        return end
    mid = (start+end)//2
    log = sum(i-mid for i in a if i >= mid)
    if log >= M:
        return bianary_search(mid+1,end,M,a)
    else:
        return bianary_search(start,mid-1,M,a)

result=bianary_search(start,end,M,a)
print(result)