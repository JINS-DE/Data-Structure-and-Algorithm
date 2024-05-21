from math import sqrt
r1=2
r2=3
cnt=0

# for i in range(r2):
#     r2_max=sqrt(r2*r2-i*i)
#     r1_max=sqrt(r1*r1-i*i)
#     if r2_max%1==0 :
#         cnt+= int(r2_max-r1_max)+1
#     else:
#         cnt+= int(r2_max-r1_max)

for i in range(1,r2+1):
        r1_max=int(sqrt(r1*r1-i*i-1)) if r1>i else -1 
        r2_max=int(sqrt(r2*r2-i*i))
        cnt+=r2_max-r1_max
print(cnt*4)


# def solution(r1, r2):
#     quar = 0
#     for i in range(0, r1):
#         quar += int(sqrt(r2**2 - i**2)) - int(sqrt(r1**2 - i**2 - 1))
#     for i in range(r1, r2):
#         quar += int(sqrt(r2**2 - i**2))
#     return quar * 4