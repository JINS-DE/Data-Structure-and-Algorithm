def solution(bandage, health, attacks):
    last_attacked_time = attacks[-1][0]
    attacks_dic = dict()
    for time, damage in attacks:
        attacks_dic[time]=damage
    time=0
    bandage_stack=0
    hp=health
    
    while True:
        time+=1
        if time>last_attacked_time or hp<0:
            break
        
        if time in attacks_dic:
            hp-=attacks_dic[time]
            bandage_stack=0
            continue
        
        bandage_stack+=1 # 초당 회복량
        if bandage_stack == bandage[0]: # 시전 시간
            hp+= bandage[1]+bandage[2] # 추가 회복량까지
            bandage_stack=0
        else:
            hp+= bandage[1]

        if hp>health:
            hp=health

    return hp if hp>0 else -1