def solution(routes):
    routes.sort(key=lambda x : x[1])
    answer=1
    start=routes[0][0]
    end=routes[0][1]
    
    for i in range(1,len(routes)):
        if routes[i][0] <= end:
            continue
        start=routes[i][0]
        end=routes[i][1]
        answer+=1
    return answer