from math import sqrt

def solution(r1, r2):
    cnt = 0
    for i in range(1,r2+1):
        r1_max=int(sqrt(r1*r1-i*i-1)) if r1>i else -1 
        r2_max=int(sqrt(r2*r2-i*i))
        cnt+=r2_max-r1_max
        


    return cnt*4