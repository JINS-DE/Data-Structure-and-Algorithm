from collections import Counter
def solution(points, routes):
    def search(route):
        cnt=0
        arr=[]
        for i in range(len(route)-1):
            sr,sc = points[route[i]-1]
            gr,gc = points[route[i+1]-1]
        
            while sr!=gr:
                arr.append((sr,sc,cnt))
                if sr>gr:
                    sr-=1
                else:
                    sr+=1
                cnt+=1

            while sc != gc:
                arr.append((sr,sc,cnt))
                if sc>gc:
                    sc-=1
                else:
                    sc+=1
                cnt+=1
        arr.append((sr, sc, cnt))
        return arr
    
    memo=[]
    for route in routes:
        memo.extend(search(route))
        
    answer = 0
    tmp = Counter(memo)
    
    for value in tmp.values():
        if value >= 2:  # 같은 위치에 2대 이상 있으면 충돌 발생
            answer += 1

    return answer