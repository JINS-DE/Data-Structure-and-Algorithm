m,n = map(int,input().split())
snack = list(map(int,input().split()))
snack.sort()
def check(target):
    num = m
    for i in range(n):
        idx = (n-1)-i
        num -= snack[idx] // target
        if num<=0:
            return True
        if snack[idx]//target == 0:
            return False
    return False

low=1
high=snack[-1]
max_num = float("-inf")
while low<=high:
    mid = (low+high)//2
    if check(mid):
        low=mid+1
        max_num=max(max_num,mid)
    else:
        high=mid-1

if max_num <= 0:
    print(0)
else:
    print(max_num)
