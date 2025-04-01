from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q=deque()
    for city in cities:
        city=city.upper()
        if city in q:
            answer+=1
            del q[q.index(city)]
            q.append(city)
        elif len(q) < cacheSize:
            q.append(city)
            answer+=5
        else:
            if len(q)>0:
                q.popleft()
                q.append(city)
            answer+=5
        
    return answer