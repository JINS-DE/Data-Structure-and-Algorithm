import sys
input=sys.stdin.readline
n=int(input())
array=[]
for _ in range(n):
    num=int(input())
    if num>0:
        array.append(num)
    else:
        if len(array)>0:
            array.pop()
print(sum(array))