


def solution(k, ranges):
    u_bak = [(0,k)]
    x=1
    while k != 1:
        if k%2==0:
            k//=2
        else:
            k=k*3+1
        u_bak.append((x,k))
        x+=1
    
    n=len(u_bak)
    
    integral=[]
    for i in range(1,n):
        min_ = min(u_bak[i-1][1],u_bak[i][1])
        max_ = max(u_bak[i-1][1],u_bak[i][1])
        integral.append(min_ + abs(max_-min_)/2)
    print(integral)
    
    answer=[]

    for x1,x2 in ranges:
        print("x1, n+x2 : ", x1, n+x2-1)
        if x1 > n+x2-1:
            answer.append(-1)
        else:
            answer.append(sum(integral[x1:n+x2-1]))
    
    
    return answer