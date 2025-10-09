def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery = 0
    pickup = 0
    # 맨 끝에서부터 있으면 무조건 다녀와야 됨.
    # 맨 끝부터 loop를 돌면서 빚을 추가
    for i in range(n-1,-1,-1):
        delivery+=deliveries[i]
        pickup+=pickups[i]
        
        # 빚이 생기면 빚을 다 갚을 때까지 loop
        while delivery>0 or pickup>0:
            delivery-=cap
            pickup-=cap
            answer+=(i+1)*2
              
    return answer