import sys
input=sys.stdin.readline
test='(()())((()))'
def vps_valid(vps):
    li=[]
    for i in vps:
        if i=='(':
            li.append(i)
        else:
            if len(li)<=0:
                return 'NO'
            else:
                li.pop()
                
            
    if len(li)>0:
        return 'NO'
    else:
        return 'YES'
    


n=int(input())
for _ in range(n):
    vps=input().strip()
    print(vps_valid(vps))