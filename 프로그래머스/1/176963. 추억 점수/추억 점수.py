def solution(name, yearning, photo):

    result=[]

    x={ na : yearning[nu] for nu , na in enumerate(name) }
    
    for i in photo:
        sum=0
        for j in i:
            if j in x:
                sum+=x[j]
        result.append(sum)

    print(result)
    return result